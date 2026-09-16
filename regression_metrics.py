from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
actual=[100,80,60]
predicted=[90,85,65]
mae=mean_absolute_error(actual,predicted)
mse=mean_squared_error(actual,predicted)
rmse=np.sqrt(mse)
print("MSE:",mse)
print("MAE:",mae)
print("RMSE:",rmse)