import streamlit as st
import re
from PIL import Image


pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
pattern1 = "^.*(?=.{8,20})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&++]).*$"


def main():
    

    st.title(':red[Data Science] Internship')
    st.header(':blue[Login App]')

    menu = ["Home","Sign up",'Login',]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader('Home')

    
    elif choice == "Sign up":
        st.subheader("Create Account")
        email_id = st.sidebar.text_input("Enter your email")
        result1 = re.search(pattern,email_id)
        if (result1):
            st.success('Your email is Valid', icon="✅")

        else:
           st.warning('Incorrect email')
        

        password = st.sidebar.text_input("Enter your password",type='password')
        result= re.findall(pattern1,password)
        if (result):
            st.success('Your password is Valid', icon="✅")
        else:
            st.warning('Incorrect  password')

            
        if st.sidebar.button('submit'):
            st.success('Your Account Created Successfully')
            

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if re.findall(pattern1,password):
            st.success('Your password is Valid', icon="✅")
        else:
            st.warning('Incorrect  password')

        if st.sidebar.button('Login'):
            st.success('Logged In as {}'.format(username))

            my_input = st.text_input("Upload Your Post")
            update = st.button('update')
            if update:
                st.write('Successfuly Updated')
                
            
            if st.button('upload your LinkedIn link'):
                st.text_input("your link is uploaded")
                st.success('Uploaded')

            if st.button('upload your GitHub link'):
                st.success('Uploaded')



if __name__ =='__main__':
    main()