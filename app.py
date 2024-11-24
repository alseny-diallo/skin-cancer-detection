from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import os
import numpy as np

app = Flask(__name__)

model = load_model('skin_cancer_model.h5')

classes_list = [
    'actinic keratosis',
    'basal cell carcinoma',
    'dermatofibroma',
    'melanoma',
    'nevus',
    'seborrheic keratosis',
    'squamous cell carcinoma',
    'vascular lesion'
]

@app.route('/')
def home():
    return render_template('main.html')

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        file = request.files['file']

        if file:
            filename = file.filename
            file_path = os.path.join('static/images', filename)
            file.save(file_path)

            img = load_img(file_path, target_size=(224, 224))
            x = img_to_array(img) / 255.0
            x = np.expand_dims(x, axis=0)

            # Prédiction
            predictions = model.predict(x)
            print (predictions)
            predicted_class_index = np.argmax(predictions)
            label = classes_list[predicted_class_index]

            # Afficher le résultat
            return render_template("result.html", label=label, file_path=file_path)

if __name__ == '__main__':
    app.run(debug=True)
