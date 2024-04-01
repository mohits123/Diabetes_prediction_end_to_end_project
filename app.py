import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings("ignore")

with open("model.pkl","rb") as pkl:
    classifier=pickle.load(pkl)


def main():
    #st.write("Diabetes Prediction")
    style = '''
    <div style = "background-color:red">
    <h1 style = "color:white">
    <center> Diabetes Prediction </center>
    <h1>
'''
    st.header("Diabetes Prediction")
    left,right = st.columns((2,2))

    Preagnencies = left.number_input("Enter Preagnencies in number",step=1,value=0)
    Glucose = right.number_input("Enter Glucose in number",step=1,value=0)
    BloodPressure = left.number_input("Enter BloodPressure in number",step=1,value=0)
    SkinThickness = right.number_input("Enter SkinThickness in number",step=1,value=0)
    Insuline = left.number_input("Enter Insuline in number",step=1,value=0)
    BMI = right.number_input("Enter BMI in number",step=1,value=0)
    DiabetesPedigreeFunction = left.number_input("Enter DiabetesPedigreeFunction in number",step=1,value=0)
    Age = right.number_input("Enter Age in number",step=1,value=0)
 
    Predict_Button = st.button("Am i Diabetic ??")

    if Predict_Button:
        res = classifier.predict([[Preagnencies,Glucose,BloodPressure,SkinThickness,Insuline,BMI,DiabetesPedigreeFunction,Age]])
        if res[0]==0:
            st.success("you are not diabetic")
        else:
            st.success("you are Diabetic")
            
if __name__ == "__main__":
    main()



