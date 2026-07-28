print("Spotify Churn Analysis") 
import numpy as np # performs fast numerical calculations.
import pandas as pd # used to read, organize, clean and analyze data.
import matplotlib.pyplot as plt # used to create graphs and charts to visualize data.
import seaborn as sns # used to create more advanced visualizations and heatmaps.

# this functions reads the dataset and stores it in a variable called df.
df = pd.read_csv('spotify_churn_dataset.csv') 
print(df.head())  # shows the first 5 rows
print(df.columns) # shows all the column names
print(df.info())  # data types and non-null values
print(df.isnull().sum()) # missing values 
print(df.shape) # summary statistics for numerical columns
print(df.duplicated().sum()) # check for duplicate records 
print(df['is_churned'].value_counts())  # number of churned vs retained users
churn_counts = df['is_churned'].value_counts()
total_users = len(df) # returns the number of rows that our dataset has
churned_users = df['is_churned'].sum() # shows the number of people who churned
churn_rate = (churned_users / total_users)*100 # churned percentage
print(f"Total Users: {total_users}") # prints total users
print(f"Churned Users:{churned_users}") 
print(f"Overall Churn Rate: {churn_rate:.2f}%") #.2f = f means floating point and .2 means show exactly 2 digits after the decimal

# creating the piechart.
plt.figure(figsize=(8,4)) # set the size of the figure
labels = ['Not Churned', 'Churned'] # labels for the pie slices
plt.pie(churn_counts, labels=labels, autopct='%1.1f%%', colors=sns.color_palette('Set2',2), startangle=55) 
# create the pie chart , churn_counts = number of customers in each category.
# label adds category names to the slices, autopct displays % values on the chart.
# colors assigns colors to each slice. startangle rotates the chart for better presntation.
plt.title("Overall Customer Churn Rate") # adds a title to the chart
plt.tight_layout() # adjust the layout to prevent overlapping
plt.savefig("churn_rate.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.show() # display the pie chart



# now, I will create a bar chart to visualize the churn rate by subscription type.
churn_rate = df.groupby('subscription_type')['is_churned'].mean() * 100
# groups the dataset by subscription type and calculates the mean of the 'is churned' column for each group, then multiplies by 100 to get the churn rate as a percentage.
plt.figure(figsize=(8,6))
churn_rate.plot(kind='bar', color=['cornflowerblue'], edgecolor='black', alpha=0.9, width=0.8, zorder=2)
for i, v in enumerate(churn_rate):
    plt.text(i, v + 1, f"{v:.2f}%", ha='center', fontsize=10, fontweight='bold') # adds the churn rate value on top of each bar in the bar chart.
plt.title("Churn Rate by Subscription Type", fontsize=16, fontweight='bold', pad=20) # title of the graph.
plt.xlabel("Subscription Type", fontsize=10, fontweight='bold') # label for the x-axis of the graph.
plt.ylabel("Churn Rate (%)", fontsize=10, fontweight='bold') # label for the y-axis of the graph.
plt.xticks(rotation=0) # rotates the x-axis labels to be horizontal.
plt.ylim(0,35) # sets the y-axis limits from 0 to 35.
plt.grid(axis='both', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0.5) # adds a grid to the graph for better readability.
plt.tight_layout() # adjusts the layout of the graph to prevent labels and titles getting cut off.
plt.savefig("churn_by_subscription.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.show() # displays the graph on the screen.


# creating a count plot to compare offline listening with customer churn
plt.figure(figsize=(8,5)) # sets the size of the figure
sns.countplot(data=df, x='offline_listening', hue='is_churned',palette='Set2') 
# creates the count plot showing the number of users based on : offline listening , churn status , color separates reatained and churned users.
plt.xticks([0,1], ["Online Listening", "Offline Listening"]) #  replace numerical values with meaningful category labels
plt.title("Offline Listening vs Customer Churn", fontsize=16, fontweight='bold') # adds a chart title 
plt.xlabel("Offline Listening", fontsize=10, fontweight='bold') # label for x-axis
plt.ylabel("Number of Users", fontsize=10, fontweight='bold') # label for y-axis 
plt.legend(title="Churn Status", labels=["Retained","Churned"]) # customize legend to make churn categories easier to understand 
plt.grid(axis='y', linestyle='--', alpha=0.5) # adds horizontal grid lines to improve readability
plt.tight_layout() #adjusts layout to avoid overlapping 
plt.savefig("offline_vs_churn.png", dpi=300, bbox_inches="tight") #saves the chart as high resolution png images.
plt.show() # displays the chart
