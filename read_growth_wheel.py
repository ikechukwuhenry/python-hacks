import pandas as pd
from IPython.display import display


file_path = 'NUTRITION-Baseline-Analysis-Template.xlsx'
# xls = pd.ExcelFile('path_to_file.xls')
# df1 = pd.read_excel(xls, 'Sheet1')
# df2 = pd.read_excel(xls, 'Sheet2')
xls = pd.ExcelFile(file_path)
df1 = pd.read_excel(xls, 'Child biodata & Feeding habit')

COLS = ['GENDER', 'AGE IN MONTHS','HEIGHT IN CM', 'WEIGHT IN KG']
growth_wheel_df = df1[COLS]
growth_wheel_df.drop(growth_wheel_df.index[210:], inplace=True)
display(growth_wheel_df)

# storing the data in JSON format
growth_wheel_df.to_json('growth_wheel.json', orient = 'index', compression = 'infer', index = 'true')

# determining the name of the file
file_name = 'GROWTH WHEEL SUMMARY.xlsx'
 
# saving the excel
growth_wheel_df.to_excel(file_name)
print('DataFrame is written to Excel File successfully.')