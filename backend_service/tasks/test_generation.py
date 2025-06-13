import asyncio
from .celery import celery_app
from services.llm_service import generate_test_cases_from_llm

@celery_app.task(bind=True)
def generate_tests_task(self, code: str, language: str, framework: str) -> dict:
    """
    Defines the Celery background task for generating test cases.
    This version uses a robust method to run an async function from a sync context
    by creating a new event loop for each task.
    """
    # Create a new event loop for each task, and close it when execution is complete.
    # This is the most reliable pattern for safely calling asynchronous code from a synchronous Celery worker.
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    try:
        result = loop.run_until_complete(
            generate_test_cases_from_llm(code, language, framework)
        )
        return result
    except Exception as e:
        self.update_state(state='FAILURE', meta={'exc_type': type(e).__name__, 'exc_message': str(e)})
        raise
    finally:
        loop.close()