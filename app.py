import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

page_bg_img = """
<style>
[class="css-10trblm"] {
    background-color=#e5e5f7
}

</style>
"""

# ------ HEADER SECTION -------------
    
with st.sidebar: 
    st.image("https://newtomstestbucket2.s3.amazonaws.com/FONDO_AZUL_LETRAS__AZUL_CLARO-removebg-preview.png")
    st. header("GenAI Content Analyzer")
    st.selectbox('Select the count of auto-promts to consider', ['1', '2','3'])

    st. header("Generated auto-prompts")
    st.button("What type of furniture is in the room?")
    st.button("How does the room's decor reflect the homeowner's personality")

with st.container():
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.image("https://newtomstestbucket2.s3.amazonaws.com/Screenshot+2023-07-10+212505.jpg")
    st.write("---")
    
with st.container():
    st.write ("Instructions:")
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