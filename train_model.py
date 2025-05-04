import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Example mock data (sensor readings and maintenance requirement)
X = np.array([
    [0.1, 25, 100],
    [0.5, 28, 120],
    [0.7, 30, 150],
    [0.3, 26, 110],
    [0.9, 35, 130],
])

y = np.array([0, 0, 1, 0, 1])  # Labels (0 = no maintenance, 1 = maintenance needed)

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, 'predictive_model.pkl')
print("Model trained and saved as 'predictive_model.pkl'")
