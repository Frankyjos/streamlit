import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# ------ HEADER SECTION -------------
    
with st.sidebar: 
    st.image("logonewtoms_remove.png")
    st.selectbox('Select the count of auto-prompts to consider', ['1', '2','3'])

    st. header("Generated auto-prompts")
    st.write("1. What type of furniture is in the room?")
    st.write("2. How does the room's decor reflect the homeowner's personality")

with st.container():
    st.image("GenAI Contect Analyzer (4).png")

with st.container():
    st.subheader ("Instructions:")
    st.write(
        """
        1. Browse ans select an input file in one of the supported formats.
        2. Select and output language, default is English.
        3. Click Upload button.
        4. You will see a text summary.
        5. Type your query in the search bar to get more insights.
        """
    )
    st.file_uploader("Select file")

    st.selectbox('Select and output Language', ['English', 'Spanish'])

    st.text_input('What insights would you like?') 
    st.button('Upload')
