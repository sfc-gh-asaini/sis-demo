import streamlit as st

from streamlit_lexical import streamlit_lexical

st.title('Rich Text Editor')
st.write('Leverage Lexical, a rich text editor in your app')

rich_text_dict = streamlit_lexical(value="initial value in **markdown**",
                             placeholder="Enter some rich text", 
                             height=400,
                             debounce=500,
                             key='1234', 
                             on_change=None
                            )


st.markdown(rich_text_dict)