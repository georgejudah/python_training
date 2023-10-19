# external dependency
import openpyxl
import pandas

# packages - 2 types of packages - 1 is inbuild packages, 2 is external packages(You need to install before importing)

# location of the file
# paths - 2 types - 1 is called Absolute file path, 2 is called Relative file path
excel_data_1_path = r"D:\work\training_Sarah\excel_automations\AmazonBooks.xlsx"
# excel_data_1_path = "./AmazonBooks.xlsx"

# excel_file = openpyxl.load_workbook(excel_data_1_path)
# print(excel_file)

# read a excel file
df = pandas.read_excel(excel_data_1_path)
# print(df.head(15))
# print(df.tail(15))
# print(df.info())
print(df.shape)



