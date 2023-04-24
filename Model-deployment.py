import numpy as np
import streamlit as st
import joblib

# Load the pipeline


Loaded_pipeline= joblib.load('pipeline.joblib')

# define an input function 

def life_ladder_prediction(input_data):
    #turning the data into a list
    data_input= list(input_data)
    prediction = Loaded_pipeline.predict(data_input)
    return prediction

def main():
    
    
    # giving a title
    st.title('Life ladder Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Country_Name = st.text_input('Country Name')
    Regional_Indicator = st.text_input('Regional Indicator')
    Year = st.text_input('Year')
    Log_GDP_Per_Capita = st.text_input('Log GDP Per Capita')
    Social_Support = st.text_input('Social Support')
    Healthy_Life_Expectancy_At_Birth = st.text_input('Healthy Life Expectancy At Birth')
    Freedom_To_Make_Life_Choices = st.text_input('Freedom To Make Life Choices')
    Generosity = st.text_input('Generosity')
    Perceptions_Of_Corruption = st.text_input('Perceptions Of Corruption')
    Positive_Affect = st.text_input('Positive Affect')
    Negative_Affect = st.text_input('Negative Affect')
    Confidence_In_National_Government = st.text_input('Confidence In National Government')


# code for Prediction
    score = ''
    
    # creating a button for Prediction
    
    if st.button('life Ladder Score'):
        score= life_ladder_prediction([[Country_Name, Regional_Indicator, Year, Log_GDP_Per_Capita, Social_Support, Healthy_Life_Expectancy_At_Birth, Freedom_To_Make_Life_Choices, Generosity, Perceptions_Of_Corruption,Positive_Affect,Negative_Affect,Confidence_In_National_Government]])
       

        
        st.success(score)
    

    
    
    
    
    
if __name__ == '__main__':
    main()