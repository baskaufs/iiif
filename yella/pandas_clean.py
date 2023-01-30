import pandas as pd


def csv_read(path, **kwargs):
    """Loads a CSV table into a Pandas DataFrame with all cells as strings and blank cells as empty strings
    
    Keyword argument:
    rows -- the number of rows of the table to return when used for testing. When omitted, all rows are returned.
    """
    dataframe = pd.read_csv(path, na_filter=False, dtype = str)
    if 'rows' in kwargs:
        return dataframe.head(kwargs['rows']).copy(deep=True)
    else:
        return dataframe
            
