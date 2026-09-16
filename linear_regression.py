#linear regression
from sklearn.linear_model import LinearRegression
import joblib
x=[[2],[4],[6],[8]]
y=[40,55,70,85]
model=LinearRegression()
model.fit(x,y)
joblib.dump(model, "linear_regression_model.joblib")
prediction=model.predict([[7]])
print("Predicted marks:",prediction)