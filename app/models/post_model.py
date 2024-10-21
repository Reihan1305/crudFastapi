from pydantic import BaseModel,Field

class blogSchema(BaseModel):
    title:str = Field(...,min_length=3,max_length=50)
    content:str = Field(...,min_length=3,max_length=50)

class blogDB(blogSchema):
    id:int
    title:str
    content:str
