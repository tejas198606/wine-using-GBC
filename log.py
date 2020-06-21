import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("model102.pkl","rb") 
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All on Board"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol):
    prediction=classifier.predict([[fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol]])
    
    print(prediction)
    return prediction

def main():
    st.title("WINE")   
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> WINE APP </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    fixedacidity = st.text_input("fixedacidity","")      
    volatileacidity = st.text_input("volatileacidity","")
    citricacid = st.text_input("citricacid","")
    residualsugar = st.text_input("residualsugar","")
    chlorides = st.text_input("chlorides","")      
    freesulfurdioxide = st.text_input("freesulfurdioxide","")
    totalsulfurdioxide = st.text_input("totalsulfurdioxide","")
    density= st.text_input("density","")
    pH = st.text_input("pH","")      
    sulphates = st.text_input("sulphates","")
    alcohol = st.text_input("alcohol","")
    
  
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(fixedacidity,volatileacidity,citricacid,residualsugar,chlorides,freesulfurdioxide,totalsulfurdioxide,density,pH,sulphates,alcohol)
        
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()