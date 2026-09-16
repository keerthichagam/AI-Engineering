from sklearn.linear_model import LinearRegression
hours = [[1], [2], [3], [4], [5], [6]]
marks = [35, 42, 50, 58, 65, 72]
model=LinearRegression()
model.fit(hours,marks)
prediction=model.predict([[7]])
print("Predicted marks for 7 hours of study:", prediction[0])
#mean absolute error
from sklearn.metrics import mean_absolute_error
actual = [80, 70, 90]
predicted = [78, 73, 87]
error=mean_absolute_error(actual,predicted)
print("MAE:",error)
from sklearn.metrics import mean_absolute_error

predicted = model.predict(hours)
error = mean_absolute_error(marks, predicted)

print("MAE:", error)
#model evaluation
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(hours,marks,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
predicted=model.predict(x_test)
error=mean_absolute_error(y_test,predicted)
print("MAE:",error)