from flask import Flask,request,render_template
import numpy as np
from tensorflow.keras.models import load_model


app=Flask(__name__)

# load the model
model=load_model("E:\DEEP_LEARNING_PROJECTS\Potato_disease\model(1).h5")

# routes
@app.route("/")
def home():
    return render_template("home.html")


if __name__=="__main__":
    app.run(debug=True)