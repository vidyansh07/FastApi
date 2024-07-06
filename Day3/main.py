from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()
"""path parmeter"""
# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs'}
# @app.get("/blog/{id}")
# def read_root(id : int):
#     return {"message": f"Hello you id is {id}"}
"""predefind paramenter"""

# class BlogType(str, Enum):
#     short = 'short'
#     story = 'story'
#     howto = 'howto'
    
# @app.get('/blog/type/{type}')
# def get_blog_type(type: BlogType):
#     return {'message': f'Blog type {type}'}

'''query parameter'''

@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int]= None):
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}')
def get_comments(id: int, sort: Optional[str]= None):
    return {'message': f'All comments for blog {id}'}