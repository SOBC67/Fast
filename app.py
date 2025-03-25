from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import class_use
import function_enc as fe
from fastapi import FastAPI
import OTPv1 as otp
app = FastAPI()
# Allowed origins (frontend domains)
origins = [
    "http://localhost:3000",  # React/Vue/Angular on local dev
    "https://example.com",  # Production frontend domain
    "*",  # Allow all (use carefully)
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specified origins
    allow_credentials=True,  # Allow sending cookies/auth headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)




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

    Key_return,LenWord,replaced_key,sort_Key,data,cc = fe.encrypt_key(key,value)
    return { "data": data ,"Key_Return":Key_return,"Len_word":LenWord,"Replace_Key":replaced_key,"Sort_Key":sort_Key,"cc":cc }

@app.post('/decryption')
async def decrypt(k:class_use.encrypt):
    key = k.key 
    value = k.value
    s = k.secretkey
    return { "data": fe.decrypt_key(key,value) }

@app.get('/otpkey')
def otpkey():
    return { "data_chr": otp.generate_chr() , "data_key":otp.generate_key() }

@app.post('/otpenc')
async def otpenc(c:class_use.otp):
    return { 'data': otp.interface_en(c.value,c.c,c.k) }

@app.post('/otpde')
async def otpde(c:class_use.otp):
    return { 'data': otp.interface_de(c.value,c.c,c.k) }

    #        'data_chr': otp.generate_chr(),
    #    'data_key': otp.generate_key()

