# api/models.py
from pydantic import BaseModel
# Python 3.8 requires importing Union from the typing module
from typing import Literal, Optional, Dict, Any, Union 

class TestGenerationRequest(BaseModel):
    code: str
    language: Literal["python", "javascript"]
    framework: Literal["pytest", "jest"]

class TestGenerationResponse(BaseModel):
    test_cases_doc: str
    test_cases_code: str

class TaskCreationResponse(BaseModel):
    task_id: str

class TaskStatusResponse(BaseModel):
    status: str
    # Use Union as an alternative to Python 3.10+'s | operator
    result: Optional[Union[TestGenerationResponse, Dict[str, Any]]] = None