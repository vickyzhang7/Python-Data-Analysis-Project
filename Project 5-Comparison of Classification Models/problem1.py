import xlrd
import pandas as pd

# Load the Excel data into a Pandas dataframe
book = xlrd.open_workbook('CTG.xls')
sheet = book.sheet_by_name('Raw Data')
headers = [cell.value for cell in sheet.row(0)]
rows = []
print("\n ********************     Question 1.1    ******************* ")
print("\n Successfully load the Excel data into Pandas dataframe ")
for i in range(1, sheet.nrows):
    row = [cell.value for cell in sheet.row(i)]
    rows.append(row)
df = pd.DataFrame(rows, columns=headers)

# Combine NSP labels into two groups: N (normal) and Abnormal
df['NSP'] = df['NSP'].apply(lambda x: 1 if x == 1 else 0)

# Print the first few rows of the dataframe to verify the data
print(df.head())

# Print the number of normal and abnormal fetuses in the dataset
normal_count = df['NSP'].sum()
abnormal_count = len(df) - normal_count
print("\n ********************     Question 1.2    ******************* ")
print('Number of normal fetuses: {}'.format(normal_count))
print('Number of abnormal fetuses: {}'.format(abnormal_count))
