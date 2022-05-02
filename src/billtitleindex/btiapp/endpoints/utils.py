from billtitleindex.billtitleindex.celery import app as celery_app
from fastapi import APIRouter

router = APIRouter()


@router.get("/scrape/", tags=["utils"], status_code=200)
def run_celery_scrape():
    """Run scrape process in background, using celery worker."""
    celery_app.send_task("btiapp.tasks.scrape_bills")
    return {"result": "running task scrape_bills"}


@router.get("/pipeline/", tags=["utils"], status_code=200)
def run_celery_pipeline():
    """Run pipeline process in background, using celery worker."""
    celery_app.send_task("btiapp.tasks.run_pipeline")
    return {"result": "running task run_pipeline"}
