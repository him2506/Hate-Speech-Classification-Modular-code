from hate.pipeline.train_pipeline import TrainPipeline
from fastapi import FastAPI
import uvicorn
import sys
import streamlit as st
import requests
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from hate.pipeline.prediction_pipeline import PredictionPipeline
from hate.exception import CustomException
from hate.constants import *

# text:str = "I can't believe how stupid some people are."

# train_pipeline = TrainPipeline()
# train_pipeline.run_pipeline()
# print("Training successful !!")

# obj = PredictionPipeline()
# text1 = obj.run_pipeline("I can't believe how stupid some people are.")
# print('-------- text1------->',text1)

# text2 = obj.run_pipeline("All immigrants are criminals and should be kicked out of the country.")
# print('-------- text2------->',text2)

# text3 = obj.run_pipeline(" Everyone should have access to quality education and healthcare.")
# print('-------- text3------->',text3)



app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")


# @app.get("/train")
# async def training():
#     try:
#         train_pipeline = TrainPipeline()
#         train_pipeline.run_pipeline()
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")


# @app.post("/predict")
# async def predict_route(text):
#     try:

#         obj = PredictionPipeline()
#         text = obj.run_pipeline(text)
#         return text
#     except Exception as e:
#         raise CustomException(e, sys) from e


# if __name__=="__main__":
#     uvicorn.run(app, host=APP_HOST, port=APP_PORT)



# Define the base URL of your FastAPI server
BASE_URL = "http://localhost:8000"  # Adjust the URL based on your FastAPI server configuration

st.title("Sentiment Detection App")

# Function to call the FastAPI training endpoint
def train_model():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Function to call the FastAPI predict endpoint
def predict(text):
    try:

        obj = PredictionPipeline()
        text = obj.run_pipeline(text)
        return text
    except Exception as e:
        raise CustomException(e, sys) from e

# Streamlit UI elements
train_button = st.button("Train Model")
if train_button:
    st.write("Training...")
    train_result = train_model()
    st.success(train_result)

st.header("Detect Sentiment")
text_input = st.text_area("Enter text for Analysis:")
predict_button = st.button("Go")
if predict_button:
    if text_input:
        prediction = predict(text_input)
        st.success(f"Prediction: {prediction}")
    else:
        st.warning("Please enter some text for prediction.")

# if __name__=="__main__":
#     uvicorn.run(app, host="localhost", port=8001, log_level="debug")




I recently visited the new cafe downtown and was pleasantly surprised. The ambiance was warm and inviting, with cozy seating and soft jazz music playing in the background. The staff were incredibly friendly and attentive, making sure every detail was perfect. I ordered a cappuccino and a croissant, both of which were delicious and beautifully presented. The coffee was rich and aromatic, and the croissant was flaky and buttery. Overall, it was a delightful experience, and I can’t wait to go back. This place is a gem, and I highly recommend it to anyone looking for a great spot to relax.


"I believe in respect for all people. However, some individuals from certain communities are constantly causing problems. It's frustrating to deal with their behavior. On the other hand, promoting understanding and tolerance is crucial for a harmonious society. We should strive to overcome our biases and prejudices."