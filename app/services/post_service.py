from app.models.post_model import blogSchema
from app.db.base import blogs,database

async def post(payload:blogSchema):
    query = blogs.insert().values(title=payload.title,content=payload.content)
    return await database.execute(query)

async def get_all():
    query = blogs.select()
    return await database.fetch_all(query)