from pydantic import BaseModel

class OauthException(BaseModel):
    detail: str

class OauthToken(BaseModel):
    access_token: str
    

class UnauthorizedException(BaseModel):
    detail: str = "Unauthorized"
    status_code: int = 401