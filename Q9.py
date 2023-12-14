import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde  # Corrected import

# Generate synthetic data for population, income, and education level by city
np.random.seed(42)  # for reproducibility
num_cities = 100
population = np.random.randint(10000, 500000, num_cities)
income = np.random.randint(30000, 90000, num_cities)
education_level = np.random.uniform(0, 20, num_cities)

# Create a bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(income, education_level, s=population/1000, c=population, alpha=0.7, cmap='viridis')
plt.xlabel('Income')
plt.ylabel('Education Level')
plt.title('Bubble Chart: Income vs. Education Level (Bubble size represents Population)')
plt.colorbar(label='Population')
plt.grid(True)
plt.show()

# Create a density chart (2D density plot)
plt.figure(figsize=(10, 6))
k = gaussian_kde(np.vstack([income, education_level]))
xi, yi = np.mgrid[min(income):max(income):100j, min(education_level):max(education_level):100j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.viridis)
plt.colorbar(label='Density')
plt.xlabel('Income')
plt.ylabel('Education Level')
plt.title('Density Chart: Income vs. Education Level')
plt.show()
