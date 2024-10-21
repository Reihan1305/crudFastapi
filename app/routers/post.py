from typing import Any,List
from fastapi import APIRouter,HTTPException,Path,FastAPI

from app.services import post_service
from app.models.post_model import blogSchema,blogDB

router = APIRouter()

@router.post("/",response_model=blogDB, status_code= 201)
async def create(payload:blogSchema):
    note_id = await post_service.post(payload)

    response_obj = {
        "id":note_id,
        "title":payload.title,
        "content":payload.content
    }

    return response_obj

@router.get("/",response_model=List[blogDB])
async def get_all():
    return await post_service.get_all()
