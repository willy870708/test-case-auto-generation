# api/v1/routers/test_generator.py
from fastapi import APIRouter
from celery.result import AsyncResult
from api.models import TestGenerationRequest, TaskCreationResponse, TaskStatusResponse
from tasks.test_generation import generate_tests_task
from tasks.celery import celery_app

router = APIRouter()

@router.post("/generate", response_model=TaskCreationResponse, status_code=202)
def submit_generation_task(request: TestGenerationRequest):
    task = generate_tests_task.delay(request.code, request.language, request.framework)
    return TaskCreationResponse(task_id=task.id)

@router.get("/results/{task_id}", response_model=TaskStatusResponse)
def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.ready():
        if task_result.successful():
            return TaskStatusResponse(status="SUCCESS", result=task_result.get())
        else:
            return TaskStatusResponse(status="FAILURE", result={"error": str(task_result.info)})
    else:
        return TaskStatusResponse(status="PENDING")