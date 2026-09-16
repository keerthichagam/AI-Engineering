from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
model=joblib.load("linear_regression_model.joblib")
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "My first AI API"}
# Step 7: POST request with request body
from pydantic import BaseModel
class Student(BaseModel):
    hours_studied: float
@app.post("/predict")
def predict(student: Student):
    prediction=model.predict([[student.hours_studied]])
    return {
        "hours_studied": student.hours_studied,
        "predicted_marks": prediction[0]
    }