import numpy as np
from flask import Flask, request, render_template
import pickle

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def Home():
    return render_template("index.html")



@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)[0]
    mapping = {0:'setosa', 1:'versicolor', 2:'virginica'}
    prediction = mapping[prediction]
    return render_template("index.html", prediction_text = "The flower species is {}".format(prediction))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
