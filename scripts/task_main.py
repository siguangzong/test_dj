from celery import Celery
import os

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')  # 加上这句话
# 1. 创建Celery对象
celery_app = Celery('demo')

# 2. 加载config.py的配置
celery_app.config_from_object('scripts.task_config')

# 3. celery worker启动时自动加载任务
celery_app.autodiscover_tasks(['scripts.sms.task'])
