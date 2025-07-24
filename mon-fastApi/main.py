from fastapi import FastAPI,Request
from starlette.responses import Response, JSONResponse



app = FastAPI()

@app.get("/hello")
def say_hello():
    
 return JSONResponse(
            content={"message": "Hello, world!"},
            status_code = 200
        ) 

@app.get("/welcome")
def read_hello(request: Request): 
    names = request.headers.get("name") 
    if names == "str":
        return JSONResponse(
            content={"Welcome": "Soa"},
            status_code = 200
        ) 
   