import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\srikr\Downloads\archive\age_gender.csv'
column_name = 'age'
data = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))

data[column_name].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')

plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')

plt.savefig('age_distribution_plot.png')
plt.show()  # Display the plot


