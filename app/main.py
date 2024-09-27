from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home_view():
    return {"hello":"world"}

@app.post("/")
def home_details_view():
    return {"hello":"world this is post"}