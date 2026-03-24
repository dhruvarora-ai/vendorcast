from data_processing import prepare_data


def run_pipeline(file, date_col, vendor_col, sales_col,
                 brand_col=None, product_col=None):

    # ✅ Lazy imports (safe for Flask)
    from linear_regression import run_model as lr
    from lasso import run_model as lasso
    from random_forest import run_model as rf
    from gradient_boosting import run_model as gb
    from xgboost_model import run_model as xgb

    df, group_cols = prepare_data(
        file, date_col, vendor_col, sales_col,
        brand_col, product_col
    )

    X = df.drop(columns=[sales_col, 'month'])
    y = df[sales_col]

    X_train, X_test = X[:-3], X[-3:]
    y_train, y_test = y[:-3], y[-3:]

    # --------------------------
    # BASE MODELS (ALWAYS)
    # --------------------------
    models = {
        "Linear": lr,
        "Lasso":  lasso,
        "RF":     rf,
        "GB":     gb,
        "XGB":    xgb,
    }

    # --------------------------
    # AUTO MODEL SELECTION LOGIC
    # --------------------------
    n_rows = len(df)
    n_vendors = df[vendor_col].nunique()
    n_features = X.shape[1]

    group_sizes = df.groupby(group_cols).size()
    min_points = group_sizes.min()

    print(f"📊 Rows: {n_rows}, Vendors: {n_vendors}, Features: {n_features}")
    print(f"📈 Min time points per group: {min_points}")

    # ---------------------------
    # LSTM (STRICT)
    # ---------------------------
    if min_points >= 24 and n_vendors <= 3:
        try:
            from lstm_model import run_model as lstm
            models["LSTM"] = lstm
            print("✅ LSTM added")
        except:
            print("⚠️ LSTM not available")

    # ---------------------------
    # ARIMA
    # ---------------------------
    if n_vendors == 1 and min_points >= 12:
        try:
            from arima_model import run_model as arima
            models["ARIMA"] = arima
            print("✅ ARIMA added")
        except:
            print("⚠️ ARIMA not available")

    # ---------------------------
    # SVM
    # ---------------------------
    if n_features < 20 and n_rows < 20000:
        try:
            from svm_model import run_model as svm
            models["SVM"] = svm
            print("✅ SVM added")
        except:
            print("⚠️ SVM not available")

    # ---------------------------
    # KNN
    # ---------------------------
    if n_rows < 5000 and n_features < 15:
        try:
            from knn_model import run_model as knn
            models["KNN"] = knn
            print("✅ KNN added")
        except:
            print("⚠️ KNN not available")

    # --------------------------
    # TRAIN MODELS (UNCHANGED)
    # --------------------------
    results = {}
    for name, func in models.items():
        try:
            model, mae, r2, acc = func(X_train, y_train, X_test, y_test)
            results[name] = {"model": model, "accuracy": acc}
        except Exception as e:
            print(f"Warning: {name} failed: {e}")
            results[name] = {"model": None, "accuracy": 0}

    # --------------------------
    # SELECT BEST MODEL (UNCHANGED)
    # --------------------------
    valid = {k: v for k, v in results.items() if v["model"] is not None}
    if not valid:
        raise ValueError("All models failed. Check your data columns.")

    best = max(valid, key=lambda x: valid[x]["accuracy"])
    best_model = valid[best]["model"]

    # --------------------------
    # PREDICTION (UNCHANGED)
    # --------------------------
    latest = df.groupby(group_cols).tail(1)
    X_future = latest.drop(columns=[sales_col, 'month'])

    preds = best_model.predict(X_future)

    output = latest[group_cols].copy()
    output['predicted_sales'] = preds

    return output, results, best