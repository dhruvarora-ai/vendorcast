from sklearn.neighbors import KNeighborsRegressor
from utils import evaluate

def run_model(X_train, y_train, X_test, y_test):
    model = KNeighborsRegressor()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    return model, *evaluate(y_test, preds)