import streamlit as st

from main import extract_details

st.set_page_config(
    page_title="JD Skill Extractor",
    page_icon="📄"
)

st.title("📄 AI Job Description Skill Extractor")
st.markdown(
    "Extract Skills, Experience and Education from Job Descriptions using Generative AI."
)
jd = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Extract Information"):

    if not jd.strip():
        st.warning("Please enter a Job Description")
    else:
        try:
            result = extract_details(jd)

            st.success("Extraction Completed")

            st.json(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")