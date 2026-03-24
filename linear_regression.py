from sklearn.linear_model import LinearRegression
from utils import evaluate

def run_model(X_train, y_train, X_test, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return model, *evaluate(y_test, preds)