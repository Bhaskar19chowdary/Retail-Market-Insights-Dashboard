
import pandas as pd
def load_data(sales_path, competitors_path, promotions_path):
    sales = pd.read_csv(sales_path, parse_dates=['date'])
    competitors = pd.read_csv(competitors_path)
    promotions = pd.read_csv(promotions_path, parse_dates=['start_date','end_date'])
    return sales, competitors, promotions

def clean_sales(sales):
    # Basic cleaning: remove negative/zero totals, fill missing categories
    sales = sales.copy()
    sales = sales[sales['total'] > 0]
    sales['category'] = sales['category'].fillna('Unknown')
    sales['price'] = sales['price'].fillna(sales['total'] / sales['quantity'].replace(0, np.nan))
    return sales

if __name__ == '__main__':
   sales, competitors, promotions = load_data('../data/sales_data.csv','../data/competitors.csv','../data/promotions.csv')
    cleaned_sales = clean_sales(sales)
    print('Cleaned Sales rows:', len(cleaned_sales))
    print("\nCleaned Sales Info:")
    cleaned_sales.info()
    print("\nCheck for remaining missing values:")
    print(cleaned_sales.isnull().sum())
