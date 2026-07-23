from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class numberInput(BaseModel):
    num1: int
    num2: int
    operation: str

@app.post("/calculate")
def run_calculator(data: numberInput):
    if data.operation == "add":
       total = data.num1 + data.num2
    elif data.operation == "sub":
       total = data.num1 - data.num2
    elif data.operation =="mul":
       total = data.num1 * data.num2
    else:
       return {"error": "invalid opeartion ! please 'add', 'sub', or 'mul'."}

    return {"result": total, "operation_used": data.operation}
       

