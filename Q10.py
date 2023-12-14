import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


# Generate some sample data (replace this with your dataset)
X = np.random.rand(100, 2)  # Features
y = np.random.randint(0, 2, 100)  # Target labels (binary classification)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Create a KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)


# Fit the classifier to the training data
knn.fit(X_train, y_train)


# Make predictions on the test data
y_pred = knn.predict(X_test)


# Calculate and print the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)


# Calculate and print the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
# Print the classification report (including precision, recall, f1-score, and support)
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)


