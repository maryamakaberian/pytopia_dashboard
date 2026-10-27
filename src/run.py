import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


 #Login
login_option = st.sidebar.radio('Login/Signup', ('Login', 'Singup'))

if login_option == 'Login':
    with st.sidebar.form('Login'):
        st.write('Login Here')
        username = st.text_input('Enter your username: ')
        password = st.text_input('Enter your password: ', type = 'password')
        
        submitted = st.form_submit_button('Login')
        if submitted:
            pass
else:
    with st.sidebar.form('Signup'):
        st.write('Signup Here')        
        username = st.text_input('Username')
        password = st.text_input('Password')
        email = st.text_input('Email')
        
        submitted = st.form_submit_button('Singup')
        if submitted:
            pass

# banner    
st.image('https://tse1.mm.bing.net/th/id/OIP.HIZZT3I6h0HltUhmYLLyQAHaCG?r=0&rs=1&pid=ImgDetMain&o=7&rm=3')
st.title(':zap: Pythopia Dashboard')

#mertrics
col1, col2 = st.columns(2)
col1.metric(label = 'Pytopia Telegram  Members ', value = '4000', delta = '+100')
col2.metric(label = 'Pytopia Websites  Members ', value = '4000', delta = '+100')

#statistics
with st.expander('Statistics'):
    #uploaded_file = st.file_uploader("Choose a file")
    #if uploaded_file is not None:
        #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        #string_data = stringio.read()
        #st.write(string_data)

        #data = json.loads(string_data)
        #st.json(data)
    fig, ax = plt.subplots(1, 1, figsize= (10, 5))
    sns.histplot(np.random.randn(100), ax= ax)
    st.pyplot(fig)
    plt.close(fig)
    
 # User input   
with st.expander('User Profile: '):
    col1, col2 = st.columns(2)
    col1.text_input('Name: ')
    col2.text_input('Location: ')
    st.camera_input('camera input', key = 'Camera Input')    
    
    
    
    
        
      
