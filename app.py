from typing import Union
import class_use
import function_enc as fe
from fastapi import FastAPI
import OTPv1 as otp
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post('/encryption')
async def encrypt(k:class_use.encrypt):
    key = k.key 
    value = k.value
    s = k.secretkey
    return { "data": fe.encrypt_key(key,value) }

@app.post('/decryption')
async def decrypt(k:class_use.encrypt):
    key = k.key 
    value = k.value
    s = k.secretkey
    return { "data": fe.decrypt_key(key,value) }

@app.post('/otpkey')
async def otpkey():
    return { "data_chr": otp.generate_chr() , "data_key":otp.generate_key() }

@app.post('/otpenc')
async def otpenc(c:class_use.otp):
    return { 'data': otp.interface_en(c.value,c.c,c.k) }

@app.post('/otpde')
async def otpde(c:class_use.otp):
    return { 'data': otp.interface_de(c.value,c.c,c.k) }

    #        'data_chr': otp.generate_chr(),
    #    'data_key': otp.generate_key()

