import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for income and education level
np.random.seed(42)  # for reproducibility
num_samples = 100
education_level = np.random.uniform(0, 20, num_samples)  # Simulated education levels
income = 1000 * education_level + np.random.normal(0, 5000, num_samples)  # Simulated income

# Plot distribution charts for each variable
plt.figure(figsize=(12, 5))

# Distribution chart for education level
plt.subplot(1, 2, 1)
plt.hist(education_level, bins=15, edgecolor='black', alpha=0.7, color='skyblue')
plt.xlabel('Education Level')
plt.ylabel('Frequency')
plt.title('Distribution of Education Level')

# Distribution chart for income
plt.subplot(1, 2, 2)
plt.hist(income, bins=15, edgecolor='black', alpha=0.7, color='orange')
plt.xlabel('Income')
plt.ylabel('Frequency')
plt.title('Distribution of Income')

plt.tight_layout()

# Scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(education_level, income, color='blue', alpha=0.7)
plt.xlabel('Education Level')
plt.ylabel('Income')
plt.title('Income vs. Education Level')
plt.grid(True)

plt.show()
