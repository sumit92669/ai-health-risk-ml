import joblib
import numpy as np

model = joblib.load("models/trained_model.pkl")

sample_data = np.array([[45, 80, 130, 110]])  # Example values

prediction = model.predict(sample_data)

print("Prediction:", prediction)
