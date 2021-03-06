from PIL import Image, ImageOps
import streamlit as st
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
#import tensorflow as tf
#from keras.preprocessing import image
from werkzeug.utils import secure_filename
st.set_option('deprecation.showfileUploaderEncoding', False)
#from keras.models import load_model

html_temp = """
   <div class="" style="background-color:salmon;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;"></p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing End-Term Examination</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp, unsafe_allow_html=True)

st.title("""
        Various Image Transformation
         """
         )


img1 = st.file_uploader("Please upload image 1", type=("jpg", "png"))
option = st.selectbox('Choose Appropriate option',
                      ("Trasnlation", "Scaling ", "Zooming", "Shearing", "Reflection", "Rotation", "Cropping", "Affine Transformation", "Inverse Transformation"))
scaling_factor = st.number_input(
    'Scaling_factor', min_value=0, max_value=10, value=2, step=1)
if img1 is None:
    st.text("Please upload an Image ")
else:
    file_bytes = np.asarray(bytearray(img1.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(img1, caption='Uploaded Image 1', use_column_width=True)


st.write('You selected:', option)


def import_and_predict():
    file_bytes1 = np.asarray(bytearray(img1.read()), dtype=np.uint8)
    opencv_image1 = cv2.imdecode(file_bytes1, 1)
    if option == "Scaling":
        resized = cv2.resize(opencv_image1, dim, interpolation=cv2.INTER_AREA)
    else:
        st.write('Please choose scaling')
    st.image(resized,  use_column_width=True)
    return 0


if st.button("Click To Perform Operation"):
    result = import_and_predict()

html_temp = """
   <div class="" style="background-color:white;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:black;margin-top:10px;">Digital Image processing EndTerm Lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp, unsafe_allow_html=True)
