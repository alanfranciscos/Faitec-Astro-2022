from os import system

system('cls')
# import xlsxwriter module
import xlsxwriter
import pandas as pd

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('src/ranking/ranking.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')
worksheet.write('B1', 'Geeks')
worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')

worksheet.write('A2', 'Hello..2')
worksheet.write('B2', 'Geeks2')
worksheet.write('C2', 'For2')
worksheet.write('D2', 'Geeks2')

# Finally, close the Excel file
# via the close() method.
workbook.close()

dataframe1 = pd.read_excel('src/ranking/ranking.xlsx')
print(dataframe1.iat[0,0])
