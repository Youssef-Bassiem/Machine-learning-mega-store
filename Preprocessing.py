import pickle

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

encoder = LabelEncoder()
scaler = MinMaxScaler()

# Drop date column and add 3 columns day, month, year
def dateformat(df, date, year, month, day):
    df[date] = pd.to_datetime(df[date])
    df[year] = df[date].dt.year
    df[month] = df[date].dt.month
    df[day] = df[date].dt.day

    df.drop([date], axis=1, inplace=True)
    return df


# Get outliers of column using IQR method
def outlier(df, column):
    q1, q3 = np.percentile(sorted(df[column]), [25, 75])
    iqr = q3 - q1
    lower_range = q1 - (1.5 * iqr)
    upper_range = q3 + (1.5 * iqr)
    df.drop(df[(df[column] > upper_range) | (df[column] < lower_range)].index, inplace=True)
    return df

def scale_save(df, flag):
    if not flag:
        filename = 'Models/Scaler/Regression_Scaling.sav'
        x = pd.DataFrame(scaler.fit_transform(df, columns=df.columns))
        pickle.dump(scaler, open(filename, 'wb'))
        return x
    else:
        filename = 'Models/Scaler/Classification_Scaling.sav'
        df = pd.DataFrame(scaler.fit_transform(df, columns=df.columns))
        pickle.dump(scaler, open(filename, 'wb'))
        return df
    
def scale_load(df, flag):
    if not flag:
        filename = 'Models/Scaler/Regression_Scaling.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        df = loaded_model.transform(df, columns=df.columns)
        return df
    else:
        filename = 'Models/Scaler/Classification_Scaling.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        df = loaded_model.transform(df, columns=df.columns)
        return df
        

# Encode to numeric columns
def encode_save(df, flag):
    df['Region'] = encoder.fit_transform(df['Region'])
    filename = 'Models/Encoding/encoder_Region_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Segment'] = encoder.fit_transform(df['Segment'])
    filename = 'Models/Encoding/encoder_Segment_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['City'] = encoder.fit_transform(df['City'])
    filename = 'Models/Encoding/encoder_City_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['State'] = encoder.fit_transform(df['State'])
    filename = 'Models/Encoding/encoder_State_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Product Name'] = encoder.fit_transform(df['Product Name'])
    filename = 'Models/Encoding/encoder_Product_Name_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Customer Name'] = encoder.fit_transform(df['Customer Name'])
    filename = 'Models/Encoding/encoder_Customer_Name_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Ship Mode'] = encoder.fit_transform(df['Ship Mode'])
    filename = 'Models/Encoding/encoder_Ship_Mode_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['MainCategory'] = encoder.fit_transform(df['MainCategory'])
    filename = 'Models/Encoding/encoder_MainCategory_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['SubCategory'] = encoder.fit_transform(df['SubCategory'])
    filename = 'Models/Encoding/encoder_SubCategory_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Country'] = encoder.fit_transform(df['Country'])
    filename = 'Models/Encoding/encoder_Country_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Order ID'] = encoder.fit_transform(df['Order ID'])
    filename = 'Models/Encoding/encoder_Order_ID_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Customer ID'] = encoder.fit_transform(df['Customer ID'])
    filename = 'Models/Encoding/encoder_Customer_ID_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    df['Product ID'] = encoder.fit_transform(df['Product ID'])
    filename = 'Models/Encoding/encoder_Product_ID_Model.sav'
    pickle.dump(encoder, open(filename, 'wb'))

    if not flag and 'ReturnCategory' in df.columns:
        df['ReturnCategory'] = encoder.fit_transform(df['ReturnCategory'])
        filename = 'Models/Encoding/encoder_ReturnCategory_Model.sav'
        pickle.dump(encoder, open(filename, 'wb'))
    return df


def encode_load(df, flag):
    filename = 'Models/Encoding/encoder_Region_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Region'] = loaded_model.transform(df['Region'])

    filename = 'Models/Encoding/encoder_Segment_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Segment'] = loaded_model.transform(df['Segment'])

    filename = 'Models/Encoding/encoder_City_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['City'] = loaded_model.transform(df['City'])

    filename = 'Models/Encoding/encoder_State_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['State'] = loaded_model.transform(df['State'])

    filename = 'Models/Encoding/encoder_Product_Name_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Product Name'] = loaded_model.transform(df['Product Name'])

    filename = 'Models/Encoding/encoder_Customer_Name_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Customer Name'] = loaded_model.transform(df['Customer Name'])

    filename = 'Models/Encoding/encoder_Ship_Mode_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Ship Mode'] = loaded_model.transform(df['Ship Mode'])

    filename = 'Models/Encoding/encoder_MainCategory_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['MainCategory'] = loaded_model.transform(df['MainCategory'])

    filename = 'Models/Encoding/encoder_SubCategory_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['SubCategory'] = loaded_model.transform(df['SubCategory'])

    filename = 'Models/Encoding/encoder_Country_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Country'] = loaded_model.transform(df['Country'])

    filename = 'Models/Encoding/encoder_Order_ID_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Order ID'] = loaded_model.transform(df['Order ID'])

    filename = 'Models/Encoding/encoder_Customer_ID_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Customer ID'] = loaded_model.transform(df['Customer ID'])

    filename = 'Models/Encoding/encoder_Product_ID_Model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    df['Product ID'] = loaded_model.transform(df['Product ID'])

    if not flag and 'ReturnCategory' in df.columns:
        filename = 'Models/Encoding/encoder_ReturnCategory_Model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        df['ReturnCategory'] = loaded_model.transform(df['ReturnCategory'])

    return df


# From dict to 2 columns
def divide(df, main_category):
    tmp = df[main_category].str.split(',|:', expand=True)
    df.drop([main_category], axis=1, inplace=True)
    df['MainCategory'] = tmp[1].squeeze()
    df['SubCategory'] = tmp[3].squeeze()
    return df


def preprocessing(df, flag, tst):
    count = 0
    for i in range(df['Country'].__len__()):
        if df['Country'][i] != 'United States':
            count += 1

    df = divide(df, 'CategoryTree')
    if tst:
        df = encode_load(df, flag)
    else:
        df = encode_save(df, flag)
    # Date to 3 columns Day, Month, Year
    df = dateformat(df, 'Order Date', 'Order Year', 'Order Month', 'Order Day')
    df = dateformat(df, 'Ship Date', 'Ship Year', 'Ship Month', 'Ship Day')

    df.fillna(df.mean(numeric_only=True).round(1), inplace=True)

    if count == 0:
        df.drop(['Country', 'Ship Month', 'Order Month', 'Order Day', 'Row ID', 'Product Name'],
                axis=1, inplace=True)
    else:
        df.drop(['Ship Month', 'Order Month', 'Order Day', 'Row ID', 'Product Name'],
                axis=1, inplace=True)
    

    if flag:
        df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
        if 'Profit' in df.columns:
            return df.drop(['Profit'], axis=1), df['Profit']
        else:
            return df
    else:
        if 'ReturnCategory' in df.columns:
            y_data = df['ReturnCategory']
            df.drop(['ReturnCategory'], inplace=True, axis=1)
            return pd.DataFrame(scaler.fit_transform(df), columns=df.columns), y_data
        else:
            return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
