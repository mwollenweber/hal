import os


CELERY_BROKER_URI = os.getenv("CELERY_BROKER_URI", "redis://guest@localhost/")
ENGINE_TIME_LIMIT = 60