from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
model_filename = 'titanic_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        form_data = request.form
        passenger_class = int(form_data['pclass'])
        sex = int(form_data['sex'])
        age = float(form_data['age'])
        siblings_spouses = int(form_data['siblings_spouses'])
        parents_children = int(form_data['parents_children'])
        embarked = int(form_data['embarked'])
        fare = float(form_data['fare'])  # Add this line for Fare

        data = pd.DataFrame({
            'Pclass': [passenger_class],
            'Sex': [sex],
            'Age': [age],
            'SibSp': [siblings_spouses],
            'Parch': [parents_children],
            'Fare': [fare],  # Include Fare
            'Embarked': [embarked]
        })

        prediction = model.predict(data)
        if prediction[0] == 0:
            result = "Did not survive"
        else:
            result = "Survived"

        return render_template('index.html', prediction_result=result)

if __name__ == '__main__':
    app.run(debug=True)
