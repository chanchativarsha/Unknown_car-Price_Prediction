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
        fields = ['id', 'mark', 'model', 'year', 'mileage', 'engine_capacity', 'transmission', 'drive', 'hand_drive', 'fuel']
        input_features = [float(request.form[field]) for field in fields]
        final_input = [input_features]

        predicted_price = model.predict(final_input)[0]
        return render_template('index.html', prediction_text=f"Predicted Car Price: {round(predicted_price, 2)}")
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
