import pandas as pd
import numpy as np
from data_cleaning import clean_sales, load_data

def monthly_aggregates(sales):
    df = sales.copy()
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
    monthly = df.groupby('month').agg({'total':'sum','quantity':'sum'}).reset_index()
    monthly['rolling_mean_3'] = monthly['total'].rolling(window=3, min_periods=1).mean()
    return monthly

def top_categories(sales, n=5):
    return sales.groupby('category')['total'].sum().nlargest(n)

if __name__ == '__main__':
    sales, _, _ = load_data('../data/sales_data.csv','../data/competitors.csv','../data/promotions.csv')
    cleaned_sales = clean_sales(sales)
    monthly_trends = monthly_aggregates(cleaned_sales)
    print("Monthly Trends (Tail):")
    print(monthly_trends.tail())

    print("\nTop Categories:")
    top_cats = top_categories(cleaned_sales)
    print(top_cats)