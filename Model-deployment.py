import numpy as np
import pickle
import streamlit as st
import locale

#Load the pipeline



with open('model_f', 'rb') as f:
    Loaded_pipeline= pickle.load(f)
#  Loaded_pipeline= pickle.load(open('/Users/yad/Desktop/Proj-2/model.p'),'r')

# print(Loaded_pipeline)