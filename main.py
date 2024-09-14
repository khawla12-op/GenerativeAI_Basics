import streamlit as st
import langchain_helper
st.title("Hotels Name Generator")
destination= st.sidebar.selectbox("Pick a Country",
                              ("Moroccan","Indian","Mexican","Italian"))

if destination:
    response= langchain_helper.generate_destination_name_and_hotels(destination)
    st.header(response['destination_name'].strip())
    hotels= response['destination_hotels'].strip().split(",")
    st.write("**Hotels**")

    for item in hotels:
        st.write("-",item)