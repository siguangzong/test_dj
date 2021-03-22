# 导入Celery对象
from scripts.task_main import celery_app


# @celery_app.task("任务名称")
@celery_app.task(name="send_sms_code")
def send_sms_code(a, b):
    """封装任务函数代码"""
    print("发送短信任务函数代码执行完成...")
    return a + b


@celery_app.task(name="send_sms_code111")
def send_sms_code111(a, b):
    """封装任务函数代码"""
    print("发送短信任务函数代码执行完成111...")
    return a + b
