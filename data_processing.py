import pandas as pd
from database import save_to_db, load_from_db
 
def load_data(file):
    return pd.read_csv(file)
 
def preprocess(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df = df.dropna()
    return df
 
def create_monthly(df, date_col, vendor_col, sales_col,
                   brand_col=None, product_col=None):
 
    df['month'] = df[date_col].dt.to_period('M')
 
    group_cols = [vendor_col]
    if brand_col:
        group_cols.append(brand_col)
    if product_col:
        group_cols.append(product_col)
    group_cols.append('month')
 
    monthly = df.groupby(group_cols)[sales_col].sum().reset_index()
    monthly['month'] = monthly['month'].dt.to_timestamp()
 
    save_to_db(monthly)
    return monthly
 
def create_lags(df, group_cols, sales_col):
    df = df.sort_values(group_cols + ['month'])
 
    for lag in [1, 2, 3]:
        df[f'lag_{lag}'] = df.groupby(group_cols)[sales_col].shift(lag)
 
    df = df.dropna()
    return df
 
def add_features(df):
    df['month_num'] = pd.to_datetime(df['month']).dt.month
    return df
 
def prepare_data(file, date_col, vendor_col, sales_col,
                 brand_col=None, product_col=None):
 
    df = load_data(file)
    df = preprocess(df, date_col)
 
    # ✅ FIXED: was called twice before, now called once
    monthly = create_monthly(df, date_col, vendor_col, sales_col,
                             brand_col, product_col)
 
    group_cols = [vendor_col]
    if brand_col:
        group_cols.append(brand_col)
    if product_col:
        group_cols.append(product_col)
 
    monthly = add_features(monthly)
    lagged = create_lags(monthly, group_cols, sales_col)
 
    return lagged, group_cols