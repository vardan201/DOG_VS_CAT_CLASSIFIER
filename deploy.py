import os
from flask import Flask, request, render_template_string, send_from_directory
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Load model
model = load_model('my_model (1).keras')  # Make sure model.h5 is in the same folder

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# HTML Template
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Dog vs Cat Classifier</title>
</head>
<body>
    <h2>Upload an image to classify (Dog or Cat)</h2>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Predict">
    </form>
    {% if result %}
        <h3>Prediction: {{ result }}</h3>
        <img src="{{ url_for('uploaded_file', filename=img_filename) }}" width="300">
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    img_filename = None
    if request.method == 'POST':
        f = request.files['file']
        img_filename = f.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
        f.save(filepath)

        # Preprocess image
        img = image.load_img(filepath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # Prediction
        pred = model.predict(x)[0][0]
        result = 'Dog' if pred > 0.5 else 'Cat'

    return render_template_string(html, result=result, img_filename=img_filename)

# Route to serve uploaded image
@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
