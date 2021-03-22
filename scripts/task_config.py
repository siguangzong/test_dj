# 任务的定时配置
from datetime import timedelta
from scripts.task_main import celery_app


# 配置broker_url 以及结果url
broker_url = 'redis://127.0.0.1:6379/2'
result_backend = "redis://127.0.0.1:6379/1"

# 对beat任务生产做一个配置,这个配置的意思就是每10秒执行一次celery_app.sms_code任务参数是(300,150)
celery_app.conf.beat_schedule = {
    'schedule_task': {  # schedule_task 名字可以随意
        'task': 'scripts.sms.send_sms_code',  # 导入方法的路径
        'schedule': timedelta(seconds=10),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (300, 150),
    }
}

