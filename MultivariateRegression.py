import pandas as pd
import statsmodels.api as sm

if __name__ == '__main__':
    df = pd.read_excel('./data/cars.xls')
    print df.head()
    df['Model_ord'] = pd.Categorical(df.Model).codes
    X = df[['Mileage', 'Model_ord', 'Doors']]
    y = df[['Price']]
    X1 = sm.add_constant(X)
    est = sm.OLS(y, X1).fit()
    print est.summary()
