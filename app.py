from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# initialise our streamlit app
# st.set_page_config(page_title = "Calories Advisor App")
# st.header("Calories Advisor App")
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Calories Advisor App")
st.header("Calories Advisor App")

# Use st.form for form submission
with st.form(key='file_upload_form'):
    st.write("Upload an image file:")
    uploaded_file = st.file_uploader(label='Choose an image...',
                                      type=['jpg', 'jpeg', 'png'])

    submit_button = st.form_submit_button(label='Submit')

# Process the uploaded file after form submission
if submit_button and uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
    # Additional processing or analysis could be done here


# input=st.text_input("Input Prompt: ",key="input")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image= None
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)
# submit= st.button("Tell me about the total calories")

# submit=st.button("Tell me the total calories")    
# initialise our streamlit app
# st.set_page_config(page_title = "Calories Advisor App")

# st.header("Calories Advisor App")
# uploaded_file = st.file_uploader("Choose an image...", type = ["JPG","JPEG","jpeg","png"])
# image = ""
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption = "Uploaded image", use_column_width = "True")
submit= st.button("Tell me about the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format
               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)

