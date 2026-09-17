# AI-Based Student Marks Prediction
This is a machine learning project that predicts a student's expected marks based on the number of hours they studied.
I built this project to understand how a machine learning model can be connected to a real application instead of using the model only inside a notebook.
## About the Project
The project uses Linear Regression to find the relationship between study hours and marks.
The user enters their study hours through a simple webpage. The input is sent to a FastAPI backend, which uses the trained model to predict the expected marks and sends the result back to the webpage.
### How it works
User enters study hours  
↓  
Frontend sends the input  
↓  
FastAPI receives the input  
↓  
Trained ML model makes the prediction  
↓  
Prediction is displayed on the webpage
The prediction is only an estimate and does not guarantee actual marks.
## Technologies I Used
- Python
- Scikit-learn
- FastAPI
- Joblib
- NumPy
- HTML
- CSS
- JavaScript
- Jupyter Notebook
- Git & GitHub
## Project Structure
```text
AI-Engineering/
│
├── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── api.py
├── linear_regression.py
├── linear_regression_model.joblib
├── regression_metrics.py
├── test_ai.ipynb
├── ai_learning.py
├── dsa.py
├── main.py
├── hello.py
└── .gitignore
```
## Screenshots

### FastAPI Swagger API

![FastAPI Swagger API](Screenshot%202026-09-16%20070039.png)

### Student Marks Prediction

![Student Marks Prediction](Screenshot%202026-09-16%20070115.png)
## What I Learned
While building this project, I learned and practiced:
- Training a Linear Regression model
- Making predictions using a trained model
- Evaluating a model using MAE, MSE and RMSE
- Saving and loading a trained model with Joblib
- Creating a basic API using FastAPI
- Connecting a frontend with a backend API
- Sending and receiving JSON data
- Basic input validation
- Using Git and GitHub for version control
## Running the Project
First, open the project folder in the terminal and run:
```bash
python -m uvicorn api:app --reload
```
Then open the API documentation:
```text
http://127.0.0.1:8000/docs
```
The frontend can be opened from:
```text
Frontend/index.html
```
## Example
Input:
```json
{
    "hours_studied": 7
}
```
Output:
```json
{
    "hours_studied": 7,
    "predicted_marks": 77.5
}
```
## Future Improvements
I plan to improve this project by:
- Using a larger real-world dataset
- Adding more factors that can affect student performance
- Comparing different ML models
- Improving the user interface
- Adding charts and visualizations
- Deploying the application online
