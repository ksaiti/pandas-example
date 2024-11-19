import kagglehub
import pandas as pd
import matplotlib.pyplot as plt


#https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset

# Download latest version
path = kagglehub.dataset_download("valakhorasani/mobile-device-usage-and-user-behavior-dataset")

# print("Path to dataset files:", path)

#read the file
df = pd.read_csv('user_behavior_dataset.csv')

# check for missing data and handle them 

print(df.columns)
# Check for missing data
missing_data = df.isnull().sum()

# Print the missing data count for each column
print(missing_data)

# print(df.info())  # View info about the DataFrame
summary_stats = df.describe() # Get summary statistics
summary_stats.to_csv('summary_statistics.csv')

## visualize data
# df = df.sort_values(by='App Usage Time (min/day)')
df_sorted= df.sort_values(by='Device Model')
plt.figure(figsize=(10, 6)) 
plt.barh(df_sorted['App Usage Time (min/day)'], df_sorted['Screen On Time (hours/day)'], color='skyblue') 
plt.xlabel('Screen On Time (hours/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.ylabel('App Usage Time (min/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.title('Device Model and App Usage Time') 
plt.grid(True) 
plt.show()

df_sorted= df.sort_values(by='Device Model')
plt.figure(figsize=(10, 6)) 
plt.scatter(df_sorted['App Usage Time (min/day)'], df_sorted['Screen On Time (hours/day)'], color='skyblue') 
plt.xlabel('Screen On Time (hours/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.ylabel('App Usage Time (min/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.title('Device Model and App Usage Time') 
plt.grid(True) 
plt.show()

df_sorted= df.sort_values(by='App Usage Time (min/day)')
plt.figure(figsize=(10, 6)) 
plt.plot(df_sorted['App Usage Time (min/day)'], df_sorted['Screen On Time (hours/day)'], color='skyblue') 
plt.xlabel('Screen On Time (hours/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.ylabel('App Usage Time (min/day)', fontdict={'fontsize': 14, 'fontweight': 'bold', 'fontfamily': 'serif'})
plt.title('Device Model and App Usage Time') 
plt.grid(True) 
plt.show()

