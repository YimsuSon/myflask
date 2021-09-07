from flask import Flask, render_template
from flask import request
from flask import redirect, url_for
import os
import pickle
import numpy as np
import pandas as pd
import scipy
import sklearn
import skimage
import skimage.color
import skimage.transform
import skimage.feature
import skimage.io


app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')


@app.route('/',method=['GET','POST'])
def index():
    if request.method == "POST":
        upload_file =request.files['image_name']
        filename = upload_file.filename
        print('Thefilename',filename)
        
        ext = filename.split('.')[-1]
        print('The extension of the filename = ex',ext)

        if ext.lower() in ['png','jpg','jpeg']:
            path_save=os.path.join(UPLOAD_PATH,filename)
            upload_file.save(path_save)
            
        else:
            print('use')

        return render_template('upload.html')
        
    else:
        return render_template('upload.html')





if __name__ == "__main__":
    app.run(debug=False)
