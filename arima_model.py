from statsmodels.tsa.arima.model import ARIMA

def run_model(series):
    try:
        model = ARIMA(series, order=(1,1,1))
        model_fit = model.fit()
        pred = model_fit.forecast(steps=1)
        return float(pred[0])
    except:
        return None