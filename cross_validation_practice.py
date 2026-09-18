from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
X = [[1], [2], [3], [4], [5], [6]]
y = [12, 19, 33, 37, 52, 58]
model = LinearRegression()
tree_model = DecisionTreeRegressor()
scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="neg_mean_absolute_error"
)
mae = -scores.mean()
print(scores)
print("Average MAE:", mae)
tree_scores = cross_val_score(
    tree_model,
    X,
    y,
    cv=5,
    scoring="neg_mean_absolute_error"
)
tree_mae = -tree_scores.mean()
print("Tree scores:", tree_scores)
print("Tree Average MAE:", tree_mae)
