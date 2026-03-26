import streamlit as st
st.set_page_config(
    page_title="User Form App",
    page_icon="📝"
)

# Centered Title
st.markdown(
    "<h1 style='text-align: center;'>User Form 📝</h1>",
    unsafe_allow_html=True
)

with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, max_value=100)
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    email = st.text_input("Enter your email")
    college = st.text_input("Enter your college name")

    submit = st.form_submit_button("Submit")

if submit:
    # Validation
    if name == "" or email == "" or age == 0 or gender == "" or college == "":
        st.error("⚠️ Please fill all the details!")
    else:
        st.success("Form submitted successfully! 🎉")
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Gender:", gender)
        st.write("Email:", email)        
        st.write("College:", college)