Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas1.py
Original DataFrame:
    Name  Marks
0  Aditi     85
1  Rohan     90
2  Meera     78

DataFrame after adding new column:
    Name  Marks  Percentage
0  Aditi     85        85.0
1  Rohan     90        90.0
2  Meera     78        78.0



= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas2.py
Original DataFrame:
  Product  Price
0     Pen     10
1    Book     50
2  Pencil      5

Updated DataFrame:
  Product  Price  Total Price
0     Pen     10           20
1    Book     50          100
2  Pencil      5           10

= RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py", line 2, in <module>
    df = pd.read_csv("pandas3 file.csv")
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'pandas3 file.csv'

======================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py ========================
Traceback (most recent call last):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py", line 2, in <module>
    df = pd.read_csv("pandas3.csv")
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 873, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 300, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1645, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\parsers\readers.py", line 1904, in _make_engine
    self.handles = get_handle(
  File "C:\Users\aditi\AppData\Local\Programs\Python\Python314\Lib\site-packages\pandas\io\common.py", line 926, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'pandas3.csv'

======================== RESTART: C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py ========================
Original Data:
     Name  Calories  Price
0  Burger     250.0  120.0
1   Fries       NaN   80.0
2    Coke     150.0    NaN
3   Pizza     300.0  200.0

Missing Values:
    Name  Calories  Price
0  False     False  False
1  False      True  False
2  False     False   True
3  False     False  False

Warning (from warnings module):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py", line 7
    df["Calories"].fillna(df["Calories"].mean(), inplace=True)
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.

See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html

Warning (from warnings module):
  File "C:/Users/aditi/OneDrive/Documents/python lab assignment/lab12/pandas3.py", line 8
    df["Price"].fillna(df["Price"].mean(), inplace=True)
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.

See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html

Data after filling missing values:
     Name  Calories  Price
0  Burger     250.0  120.0
1   Fries       NaN   80.0
2    Coke     150.0    NaN
3   Pizza     300.0  200.0
