import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#STEP-01: Define the data
'''data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value': [4, 7, 1, 8]
}
#STEP-02: Create a dataframe
df = pd.DataFrame(data)

#STEP-03: Plot the bar chart
sns.barplot(x='Category', y='Value', data=df)

#STEP-04: Add titles and labels
plt.title('Simple Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')


#STEP-05: show the plot
plt.show()

#STEP-01: Define the data
data = {
    'Product': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Region': ['North', 'South', 'North', 'South', 'North', 'South'],
    'Sales': [150, 200, 300, 250, 100, 150]
}
#STEP-02: Create a dataframe
df = pd.DataFrame(data)

#STEP-03: Process the data
#Create a pivot table to show the structure
pivot_df = df.pivot(index='Region', columns='Product', values='Sales')
print(pivot_df)

#STEP-04: Plot the bar chart
sns.set_theme(style="whitegrid")
sns.barplot(x='Product', y='Sales', color='red', hue='Region', data=df)

#STEP-05: Add titles and labels
plt.title('Sales by Product and Region')
plt.xlabel('Product')
plt.ylabel('Sales')


#STEP-06: show the plot
plt.show()

tips = sns.load_dataset('tips')
print(tips)
print(tips.head())
print(tips.tail())
print(tips.info())
print(tips.describe())
print(tips.isnull().sum())
sex_counts = tips['sex'].value_counts()
print("\nCounts of each type(Males and Females:")
print(sex_counts)

tips = sns.load_dataset('tips')
plt.figure(figsize=(10,6))
sns.barplot(x='day', y='total_bill',data=tips, estimator=sum, ci=None)
plt.title('Total Bill Amounts By Day')
plt.xlabel('Day of the week')
plt.ylabel('Total Bill Amount($)')
plt.show()'''


# Load the dataset
tips = sns.load_dataset('tips')

# Prepare data for plotting
# Melt the DataFrame to have 'total_bill' and 'tip' in a single column for plotting
melted_data = tips.melt(id_vars='day', value_vars=['total_bill', 'tip'],
                        var_name='category', value_name='amount')

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='day', y='amount', hue='category', data=melted_data, palette='viridis')
plt.title('Total Bill and Tip Amount by Day')
plt.ylabel('Amount')
plt.xlabel('Day')
plt.legend(title='Category')
plt.show()
