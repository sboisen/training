"""
Framework for Week10 programming assignments. Before you can use this, you need several things:

- download the data file: goodreads_seanboisen_read-for-cash.xlsx from Github (Week09). This represents data from Goodreads.com for 75 books I've entered as relevant to Read for Cash. 

- install the xlrd module for reading Excel files: easiest way is
  - go to a terminal (DOS shell on Windows, Terminal on Mac OS X)
  - execute:
    pip install xlrd
  - (if you don't have pip, ask for help: you'll need it)

This file provides the initial framework for reading the data: you'll extend this for the assignments.

There's a lot of functionality in the xlrd module, and much of it goes beyond what we've learned so far. Here are the bits you'll need to know for this assignment (assuming you've already done 'import xlrd'):
- workbook = xlrd.open_workbook(filename): returns a workbook object
- sheet = workbook.sheet_by_index(0): returns the first sheet in the workbook (the only one there is for this data file)
- sheet.nrows returns the number of rows
- sheet.row_values(3): returns the values in the 3rd row of the sheet. The first row has column labels

Using the code below:

# import this code: assumes the code is in the same directory as your Python process
>>> import books
>>> books.sheet_headers()
[u'Book Id',
 u'Title',
 u'Author',
 u'ISBN',
 u'My Rating',
 u'Average Rating',
 u'Publisher',
 u'Number of Pages',
 u'Year Published',
 u'Original Publication Year',
 u'Date Read',
 u'Date Added',
 u'Bookshelves',
 u'Exclusive Shelf']
>>> sm = sheet_matrix()
>>> sm[0]
[84525.0,
 u"What Got You Here Won't Get You There: How Successful People Become Even More Successful",
 u'Marshall Goldsmith',
 u'',
 0.0,
 3.9,
 u'Hyperion',
 256.0,
 2007.0,
 2007.0,
 '',
 42194.0,
 u'business, meta_read-for-cash, to-read',
 u'to-read']
"""

import xlrd

# modify this to match where you put the data file on your local filesystem
DATAFILE = '/Users/sboisen/git/sboisen/training/ThinkPython/Week09/goodreads_seanboisen_read-for-cash.xlsx'


def sheet_headers(file=DATAFILE):
    """Return a list of column headers from DATAFILE. 
    """
    sheet = xlrd.open_workbook(DATAFILE).sheet_by_index(0)
    return sheet.row_values(0)

    
def sheet_matrix(file=DATAFILE):
    """Return the data from DATAFILE as a list of lists. Doesn't include the headers. 
    """
    sheet = xlrd.open_workbook(DATAFILE).sheet_by_index(0)
    rows = []
    for index in range(1, sheet.nrows):
        rows.append(sheet.row_values(index))
    return rows
    
