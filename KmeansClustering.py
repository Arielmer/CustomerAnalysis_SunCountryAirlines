import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load datasets
clustering_data = pd.read_csv("/Users/macbook/Downloads/Clustering Data.csv")
customer_data = pd.read_csv("/Users/macbook/Downloads/sample_data_transformed.csv")

# Drop non-numeric columns for clustering
clustered_data = clustering_data.copy()
clustered_data.drop(columns=['uid', 'PNRLocatorID'], inplace=True, errors='ignore')

# Standardizing the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(clustered_data)

# Define the number of clusters
k = 5
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans.fit(scaled_data)

# Assign cluster labels
clustering_data['Cluster'] = kmeans.labels_

# Ensure 'uid' exists in both datasets before merging
if 'uid' in customer_data.columns and 'uid' in clustering_data.columns:
    # Merge cluster assignments with reservation data
    final_dataframe = customer_data.merge(clustering_data[['uid', 'Cluster']], on='uid', how='left')
else:
    raise KeyError("Column 'uid' is missing in one of the datasets")

# Visualization: Cluster Sizes
plt.figure(figsize=(8,6))
sns.countplot(x=final_dataframe['Cluster'])
plt.title('Cluster Sizes')
plt.xlabel('Cluster')
plt.ylabel('Count')
plt.show()

# Visualization: Group Size by Cluster
if 'group_size' in final_dataframe.columns:
    plt.figure(figsize=(8,6))
    sns.boxplot(x=final_dataframe['Cluster'], y=final_dataframe['group_size'])
    plt.title('Group Size by Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Group Size')
    plt.show()
else:
    print("Warning: 'group_size' column not found in dataset.")

# Visualization: Age Group by Cluster
if 'age_group' in final_dataframe.columns:
    plt.figure(figsize=(8,6))
    sns.histplot(data=final_dataframe, x='age_group', hue='Cluster', multiple='stack')
    plt.title('Age Group by Cluster')
    plt.xlabel('Age Group')
    plt.ylabel('Count')
    plt.show()
else:
    print("Warning: 'age_group' column not found in dataset.")

# Visualization: Booking Channels by Cluster
if 'BookingChannel' in final_dataframe.columns:
    plt.figure(figsize=(8,6))
    sns.countplot(x=final_dataframe['BookingChannel'], hue=final_dataframe['Cluster'])
    plt.title('Booking Channels by Cluster')
    plt.xlabel('Booking Channel')
    plt.ylabel('Count')
    plt.legend(title='Cluster')
    plt.show()
else:
    print("Warning: 'BookingChannel' column not found in dataset.")

# Save the final dataset with clusters
final_dataframe.to_csv("CustomerData_with_Clusters.csv", index=False)