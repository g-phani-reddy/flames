from fastapi import FastAPI
from input_model import FlamesModel
from logic import find_flames

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is up"}


@app.post("/flames")
def get_flames(flamemodel: FlamesModel):
    try:
        if len(flamemodel.name1) > 0 and len(flamemodel.name2) > 0:
            return {"result" : find_flames(flamemodel.name1, flamemodel.name2)}
        else:
            return {"result": "Improper input provided"}
    except Exception as e:
        return {"result": "Exception occured " + str(e)}


