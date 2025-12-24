import matplotlib.pyplot as plt

def sales_trend(df):
    monthly_sales = df.groupby('Month')['Sales'].sum()
    monthly_sales.plot(kind='line', title='Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.show()
