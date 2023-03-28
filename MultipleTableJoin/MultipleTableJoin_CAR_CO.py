# -*- coding: UTF-8 -*-

import openpyxl

def remove(sheet, row):
    # iterate the row object
    for cell in row:
          # check the value of each cell in
        # the row, if any of the value is not
        # None return without removing the row
        if cell.value != None:
              return
    # get the row number from the first cell
    # and remove the row
    sheet.delete_rows(row[0].row, 1)


from openpyxl import Workbook, load_workbook
book = load_workbook('C:/Downloads/5de94fdc2fabb.xlsx')
catalog = book['Catalogo']
book.remove(catalog)
sheets = book.sheetnames

'''
sheet = book.active
print(book.worksheets)
print(book.sheetnames)
print(sheet['D8'].value)
'''

for i in sheets:
    print('Processing: %s' %i)
    sheet = book[i]
    sheet.delete_rows(idx=1)  # Delete an specific row
    sheet.delete_rows(1, 15)


book.save('C:/Downloads/CARClean.xlsx')


# Refs
# https://blog.aspose.com/cells/insert-and-delete-rows-and-columns-in-excel-using-python/
# https://www.youtube.com/watch?v=718edSNvKLA
# https://stackoverflow.com/questions/23527887/getting-sheet-names-from-openpyxl
# https://www.geeksforgeeks.org/how-to-delete-one-or-more-rows-in-excel-using-openpyxl/
# https://www.codespeedy.com/delete-rows-of-a-sheet-using-openpyxl/