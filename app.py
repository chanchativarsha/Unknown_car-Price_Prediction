from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Load the model
with open("Car_price.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Input fields
        fields = ['id', 'mark', 'model', 'year', 'mileage', 'engine_capacity', 'transmission', 'drive', 'hand_drive', 'fuel']
        input_features = [float(request.form[field]) for field in fields]
        final_input = [input_features]

        # Prediction
        prediction = model.predict(final_input)[0]  # Example: 874.0999755859375

        # Round and format with 'k'
        formatted_price = f"{round(prediction)}k"

        return render_template('index.html', prediction_text=f"Predicted Car Price: {formatted_price}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
