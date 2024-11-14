# backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fys_interpreter import run_fys_code

app = FastAPI()

class FYSCodeRequest(BaseModel):
    code: str

@app.post("/run-code")
async def run_code(request: FYSCodeRequest):
    try:
        result = run_fys_code(request.code)
        return {"output": result, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e), "status": "error"})
