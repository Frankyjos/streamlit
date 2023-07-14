import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# ------ HEADER SECTION -------------
    
with st.sidebar: 
    st.image("logonewtoms_remove.png")
    st.selectbox('Select the number of Suggested Prompts', ['1', '2','3','None'])

    st. header("Suggested Prompts:")
    st.write("1.")
    st.write("2.")
    st.write("3.")

with st.container():
    st.image("GenAI Contect Analyzer (6).png")

with st.container():
    st.subheader ("Follow the instructions:")


col1, col2=st.columns(2)

with col1:
    st.write(
        """
        
        1. Upload your file in the proper format (PDF, .csv, .xlsx, .jpg, .png).
        2. Specify the output language.
        3. Enter a natural language request in the search bar.
        5. Click the send button.
        6. You will get a response to the query
        """
    )

with col2:
    st.file_uploader("Select file")
    st.selectbox('Select and output Language', ['English', 'Spanish'])
    

st.text_input('Enter a request here:') 
st.button('Send')
