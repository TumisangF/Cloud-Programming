import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle


data = pd.read_csv('train.csv')

# Preprocessing
data.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)

# Fill missing values in 'Age' column with the median
data['Age'].fillna(data['Age'].median(), inplace=True)

# Drop rows with missing 'Embarked' values
data.dropna(subset=['Embarked'], inplace=True)

label_encoder = LabelEncoder()
data['Sex'] = label_encoder.fit_transform(data['Sex'])
data['Embarked'] = label_encoder.fit_transform(data['Embarked'])

X = data.drop('Survived', axis=1)
y = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a RandomForestClassifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Function to save the model in pickle format
def save_model_to_pickle(model, filename):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

# Save the model to a pickle file
model_filename = 'titanic_model.pkl'
save_model_to_pickle(model, model_filename)

print("Model saved as", model_filename)
