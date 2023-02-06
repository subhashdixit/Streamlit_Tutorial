import streamlit as st

# Title
st.title("Streamlit complete tutorial")

# Header/Subheader
st.header("Header")

st.subheader("Sub header")

# Text
st.text("This is text")

# Markdown
st.markdown("This is markdown and can be modified using ipynb notebok syntax ")

st.markdown(" # Markdown")
st.markdown(" ## Markdown")
st.markdown(" ### Markdown")

# Error messages/ Colorful text
st.success("Successfullly done")

# Information
st.info("This is information/comment")

# Warning
st.warning("This is a warning")

# Error
st.error("This is a error")

# Exception (Try, except, else and finally block)
st.exception("NameError('name sd is not defined')")

# help of numpy library
import numpy
# st.help(numpy)

# range function
st.help(range)

# Writing text super function
st.write("Write text using write")

st.write(range(0,10,2))

st.markdown("CNN Architectures")
from PIL import Image
img = Image.open("arch.png")
st.image(img)

st.markdown("Changing Width of the image")

#st.image(img)
st.image(img, width = 400, caption = "CNN Architectures")


st.markdown("Adding video")
# Video adding
vid_file = open("D:\My Personal Files\Streamlit\Restaurant Reviews Classification - Google Chrome 2022-12-13 23-49-38.mp4", "rb")
vid_bytes = vid_file.read()
st.video(vid_bytes) # 10m

st.markdown("Adding songs")
# Audio
sudio_file = open("D:\My Personal Files\Streamlit\Jhoome Jo Pathaan(PagalWorld.com.se).mp3", "rb").read()
st.audio(sudio_file)

st.markdown("Adding checkbox")
#Checkbox
# ML ( Gender , M / F)
if st.checkbox("Show / Hide"):
    st.text("Showing or Hiding widget")

st.markdown("Adding radio button")
# Radio Buttons
status = st.radio("What is your Status", ("Active", "Inactive"))


# Link with some function
# Else function
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Activate it")

st.markdown("Adding selectbox/dropdown")
# SelectBox
occupation = st.selectbox("Your Occupation", ["Civil Engineer", "Data Scientist", "Software Engineer", "Data Analyst", "Data Engineer"])
st.write("You Selected this option", occupation)

st.markdown("Adding multi selectbox. Multiple values can be selected at once")
# # India, China, USA, Srilanka
# Multiselect
location = st.multiselect("Where do you work", ("Australia", "India", "USA", "UK"))

st.markdown("Get all the selected location count")
# TO get all selected count
st.write("You Selected", len(location), "locations")

st.markdown("Adding slider")
# Slider
level = st.slider("What is your level", 1,5)

st.markdown(f"Print selected level in the slider")
st.write(f"Selected level is {level}")

st.markdown("Adding run button")
# Buttons
# st.button("Simple Button")
if st.button("Run"):
    st.text("ML model is running")

st.markdown("Adding submit button")
if st.button("Submit"):
    st.text("Sucessful Submited")

st.markdown("Add box to take input")
# text Input
college_name = st.text_input("Enter your college name")
if st.button("Submit", key="1"):
    # result = college_name.title()
    st.success(college_name)

st.markdown("Adding textare to take input as a long text")
# Text Area
message = st.text_area("Enter your message")
if st.button("Submit", key = "2"):
    # result = message.title()
    st.success(message)

st.markdown("Adding date")
# Date Input
import datetime
today = st.date_input("Today is", datetime.datetime.now())
# Time
the_time = st.time_input("The time is", datetime.time())
st.write(f"Today : {today} and Time : {the_time}")

#Display Json Output
st.text("Display json Data")
st.json({"Name":"Subhash Dixit",
        "Gender":"Male",
        "Profession": "Associate Data Scientist"})

# import numpy as np
st.text("Display Raw Code")
st.code("import numpy as np")

# Display row code with dataframe
with st.echo():
    import pandas as pd
    df = pd.DataFrame({"Name":"Subhash Dixit",
        "Gender":"Male",
        "Profession": "Associate Data Scientist"}, index = [1,2,3])

st.markdown("Printing json data as a dataframe")
st.write(df)

st.markdown("Adding progress bar")
# Progress bar
import time
my_bar = st.progress(0)
for p in range(20):
    my_bar.progress( p + 10)

st.markdown("Adding spinner")
#spinner
with st.spinner("Waiting .."):
    st.write("Wait for 5 seconds")
    time.sleep(5)
st.success("Finished!")

st.markdown("Adding ballons. Can be used to celebrate")
# ballon
st.balloons()

st.markdown("Adding sidebar")
# Sidebar
st.sidebar.header("Streamlit Tutorial")
st.sidebar.text("Everyhing is covered here to create a basic webapp")

st.markdown("Adding selectbox to choose ML algorithms")
# Select Box
algoritmhs = st.sidebar.selectbox("Your Algorithm", ["Liner Regression", "Logistic Regression", "Decision tree",
"Random Forest"])