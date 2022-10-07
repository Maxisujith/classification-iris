import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

def iris_flower_prediction_app():
        """iris_flower_prediction_app.user_input_features().value"""
        global iris_flower_prediction_app
        if iris_flower_prediction_app: return iris_flower_prediction_app

def iris_flower_prediction_app_using_RandomForestClassifier():
        """iris_flower_prediction_app.iris_flower_prediction_app().value"""
        global iris_flower_prediction_app_using_RandomForestClassifier
        if iris_flower_prediction_app: return iris_flower_prediction_app_using_RandomForestClassifier

def add_bg_from_url():
    st.markdown(f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/purple-wild-plants-illustration-hand-drawn-set-remixed-from-artworks-by-mary-vaux-walcott_53876-112061.jpg?w=740&t=st=1665141321~exp=1665141921~hmac=16d47971835d9383cf813fe8be3ab61e84abfc2172e4a059d2f998a089ecdcbd");
             background-attachment: fixed;
             background-size: cover}}
             </style>""",unsafe_allow_html=True)
add_bg_from_url()


st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")
st.info("Developed by NANDHAKUMAR S, SUJITH V, MOHAMED RAFEEK S [Team MIDNIGHT HACKER]", icon="©")
st.sidebar.header('User Input Parameters')
st.sidebar.image("iris1.jpg")
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
