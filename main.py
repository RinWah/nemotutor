from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TutorRequest(BaseModel):
    student_background: str
    topic: str

@app.post("/explain")
async def explain(req: TutorRequest):
    # mock for now
    explanation = f"Explaining {req.topic} to someone with: {req.student_background}"
    return {"explanation": explanation}