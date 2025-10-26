import pandas as pd
from data_cleaning import clean_sales, load_data

def compute_kpis(sales):
    if sales['total'].le(0).any() or sales['category'].isnull().any():
         print("Warning: Running KPIs on potentially unclean data. Please clean first.")

    total_revenue = sales['total'].sum()
    avg_item_price = total_revenue / max(1, sales['quantity'].sum())
    promo_revenue_share = sales[sales['promotion']==1]['total'].sum() / max(1, total_revenue)

    return {
        'total_revenue': total_revenue,
        'avg_item_price': avg_item_price,
        'promo_revenue_share': promo_revenue_share
    }

if __name__ == '__main__':
    sales, _, _ = load_data('../data/sales_data.csv','../data/competitors.csv','../data/promotions.csv')
    cleaned_sales = clean_sales(sales)
    kpis = compute_kpis(cleaned_sales)
    print(kpis)