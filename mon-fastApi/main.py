from fastapi import FastAPI
from starlette.responses import Response, JSONResponse


app = FastAPI()

@app.get("/hello")
def say_hello():
    
 return JSONResponse(
            content={"message": "Hello, world!"},
            status_code = 200
        ) 





