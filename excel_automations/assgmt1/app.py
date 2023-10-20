# In the AmazonBooks dataframe
# the AmazonBooks excel file which was shared,
# 1. find the number of rows containing null values in 1.)User Rating 2.)Reviews
# 2. If you find any null values, remove that particular rows out of the dataframe and print the number of rows available after deleting
# BONUS questions
# **3. Find the number of books having rating more than 4.5 and print out the names of each books
# **4. Find the number of books having books having 'Non Fiction' genre

#Step 1:
import pandas as pd

AMAZON_DATA_PATH = r'D:\work\training_Sarah\excel_automations\AmazonBooks.xlsx'
data_df  = pd.read_excel(AMAZON_DATA_PATH)
# print(data_df.info())
# print(data_df.head())
# print(data_df.tail())

# 1. find the number of rows containing null values in 1.)User Rating 2.)Reviews
# print(data_df['Reviews'].isnull().sum())
# 2. If you find any null values, remove that particular rows out of the dataframe and print the number of rows available after deleting
data_df.dropna(subset=['Reviews', 'User Rating'], inplace=True)
# print(data_df.shape)

#Find the number of books having rating more than 4.5 and print out the names of each books
# print(len(data_df[data_df['User Rating']>4.5]))

# Find the number of books having having 'Non Fiction' genre
print(len(data_df[data_df['Genre'] == 'Non Fiction']))


