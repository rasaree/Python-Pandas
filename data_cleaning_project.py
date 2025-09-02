import pandas as pd

# Load the CSV file
df = pd.read_csv(r"C:\Users\Administrator\Desktop\Data Analysis\Data Set For Task\1) iris.csv")

# Show the all rows
print("display.max_rows", None)

# Check for number of  missing values in columns
print(df.isnull().sum())

#removing duplicate rows
df = df.drop_duplicates(keep=False)

#show final dataset
print(df)
