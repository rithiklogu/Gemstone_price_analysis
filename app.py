import streamlit as st
import pandas as pd
import pickle
import os 
import sys

import streamlit as st
import pandas as pd
import pickle

import streamlit as st
import pandas as pd
import pickle
import os

# # Define the paths to the preprocessor and model files in the artifacts directory
# preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
# model_path = os.path.join('artifacts', 'model.pkl')

# # Ensure the files exist in the artifacts directory
# if not os.path.exists(preprocessor_path):
#     st.error(f"Preprocessor file not found: {preprocessor_path}")
# if not os.path.exists(model_path):
#     st.error(f"Model file not found: {model_path}")

# # Load preprocessor and model
# try:
#     with open(preprocessor_path, 'rb') as f:
#         preprocessor = pickle.load(f)
# except FileNotFoundError:
#     st.error("Preprocessor file not found. Please check the file path.")

# try:
#     with open(model_path, 'rb') as f:
#         model = pickle.load(f)
# except FileNotFoundError:
#     st.error("Model file not found. Please check the file path.")

# # Title of the app
# st.title('Gold Price Prediction')

# # User inputs
# st.header('Input Features')

# # Numerical features
# carat = st.number_input('Carat', value=0.0)
# depth = st.number_input('Depth', value=0.0)
# table = st.number_input('Table', value=0.0)
# x = st.number_input('X dimension', value=0.0)
# y = st.number_input('Y dimension', value=0.0)
# z = st.number_input('Z dimension', value=0.0)

# # Categorical features with suggestions
# cut_options = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
# color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
# clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

# cut = st.selectbox('Cut', options=cut_options)
# color = st.selectbox('Color', options=color_options)
# clarity = st.selectbox('Clarity', options=clarity_options)

# # Collect input features into a DataFrame
# input_features = pd.DataFrame({
#     'carat': [carat],
#     'depth': [depth],
#     'table': [table],
#     'x': [x],
#     'y': [y],
#     'z': [z],
#     'cut': [cut],
#     'color': [color],
#     'clarity': [clarity]
# })

# # Add a button to trigger the prediction
# if st.button('Predict'):
#     try:
#         # Preprocess the input features
#         preprocessed_features = preprocessor.transform(input_features)
        
#         # Predict the gold price
#         prediction = model.predict(preprocessed_features)
        
#         # Display the prediction
#         st.header('Prediction')
#         st.write(f'The predicted gold price is: ${prediction[0]:.2f}')
#     except Exception as e:
#         st.error(f"Error in preprocessing or prediction: {e}")



import streamlit as st
import pandas as pd
import pickle
import os

# Define the paths to the preprocessor and model files in the artifacts directory
preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
model_path = os.path.join('artifacts', 'model.pkl')

# Ensure the files exist in the artifacts directory
if not os.path.exists(preprocessor_path):
    st.error(f"Preprocessor file not found: {preprocessor_path}")
if not os.path.exists(model_path):
    st.error(f"Model file not found: {model_path}")

# Load preprocessor and model
try:
    with open(preprocessor_path, 'rb') as f:
        preprocessor = pickle.load(f)
except FileNotFoundError:
    st.error("Preprocessor file not found. Please check the file path.")

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")

# Title of the app
st.title('Gold Price Prediction')

# User inputs
st.header('Input Features')

# Numerical features
carat = st.number_input('Carat', value=0.0)
cut_options = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
clarity_options = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
depth = st.number_input('Depth', value=0.0)
table = st.number_input('Table', value=0.0)
x = st.number_input('X dimension', value=0.0)
y = st.number_input('Y dimension', value=0.0)
z = st.number_input('Z dimension', value=0.0)

# Categorical features with suggestions
cut = st.selectbox('Cut', options=cut_options)
color = st.selectbox('Color', options=color_options)
clarity = st.selectbox('Clarity', options=clarity_options)

# Add a button to trigger the prediction
if st.button('Predict'):
    try:
        # Collect input features into a DataFrame with the correct order
        input_features = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'clarity': [clarity],
            'color': [color],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })
        
        # Print input features for debugging
        st.write("Input Features:")
        st.write(input_features)
        
        # Preprocess the input features
        preprocessed_features = preprocessor.transform(input_features)
        
        # Print preprocessed features for debugging
        st.write("Preprocessed Features:")
        st.write(preprocessed_features)
        
        # Predict the gold price
        prediction = model.predict(preprocessed_features)
        
        # Print raw prediction output for debugging
        st.write("Raw Prediction Output:")
        st.write(prediction)
        
        # Display the prediction
        st.header('Prediction')
        st.write(f'The predicted gold price is: ${prediction[0]:.2f}')
    except Exception as e:
        st.error(f"Error in preprocessing or prediction: {e}")
