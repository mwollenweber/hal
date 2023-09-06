import settings
import datetime
from celery import Celery

app = Celery(broker=settings.CELERY_BROKER_URI)
#app.conf.CELERY_TIMEZONE = settings.CELERY_TIMEZONE
#app.conf.CELERYBEAT_SCHEDULE = settings.CELERYBEAT_SCHEDULE
#app.conf.MAX_TASKS_PER_CHILD = settings.MAX_TASKS_PER_CHILD
app.conf.CELERY_IGNORE_RESULT = True
app.conf.CELERY_TASK_SERIALIZER = "pickle"
app.conf.CELERY_RESULT_SERIALIZER = "pickle"
app.conf.CELERY_ACCEPT_CONTENT = ["pickle", "json"]



@app.task(name='run_engine', ignore_result=True, expires=settings.ENGINE_TIME_LIMIT)
def run_engine(engine, api, email):
    try:
        # logger = get_task_logger(__name__)
        # dictConfig(LOGGING)
        # captureWarnings(True)

        start_time = datetime.utcnow()

    except Exception as e:
        print(e)

    return
