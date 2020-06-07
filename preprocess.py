
import pandas as pd


# Lay data tu file .csv vao dataframe
def get_data(filename):
    df = pd.read_csv(filename, encoding='unicode_escape')
    return df

# Tien xu ly du lieu


def data_preprocessing(dataframe):
    # remove space:
    dataframe.columns = dataframe.columns.str.replace(' ', '')
    # rename:
    dataframe.rename(columns={'Country,Other': 'Country', 'Serious,Critical': 'SeriousCritical'}, inplace=True)
    # replace NaN value to 0
    dataframe = dataframe.fillna(0)
    # Xoa row tong hop:
    dataframe = dataframe[:-1]
    # Xoa cot chua du lieu k dung den:
    dataframe = dataframe.drop("#", axis=1)
    # Dat ten quoc gia lam chi muc:
    dataframe.set_index('Country', inplace=True)
    return dataframe
