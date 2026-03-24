import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from utils import evaluate

def create_sequences(X, y, steps=3):
    Xs, ys = [], []
    for i in range(len(X) - steps):
        Xs.append(X[i:(i + steps)])
        ys.append(y[i + steps])
    return np.array(Xs), np.array(ys)

def run_model(X_train, y_train, X_test, y_test):
    try:
        X_train = X_train.values
        X_test = X_test.values
        y_train = y_train.values
        y_test = y_test.values

        X_train_seq, y_train_seq = create_sequences(X_train, y_train)
        X_test_seq, y_test_seq = create_sequences(X_test, y_test)

        model = Sequential()
        model.add(LSTM(50, activation='relu',
                       input_shape=(X_train_seq.shape[1], X_train_seq.shape[2])))
        model.add(Dense(1))

        model.compile(optimizer='adam', loss='mse')
        model.fit(X_train_seq, y_train_seq, epochs=10, verbose=0)

        preds = model.predict(X_test_seq)

        return model, *evaluate(y_test_seq, preds)
    except:
        return None, 9999, 0, 0