from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"Message": "Hello World"}

@app.post("/")
async def post():
    return {"Message": "I am post method"}

@app.put("/")
async def put():
    return {"Message": "I am put method"}
