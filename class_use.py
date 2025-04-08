from pydantic import BaseModel
class encrypt(BaseModel):
    key: str
    value: str
    secretkey: str

class otp(BaseModel):
    k: str
    value: str
    c: str

class k_c_otp(BaseModel):
    value:str
    types:str