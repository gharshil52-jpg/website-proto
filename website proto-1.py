import streamlit as st
st.title(":red[A simple e-commerce website prototype]")
st.subheader("This is a simple e-commerce website prototype built using Streamlit.")
st.write("You can use this prototype to add products to the cart and allow users to browse and purchase them.")
st.image("modiji-17605779 (1).png", caption="Modiji")
buttoninput=st.button("Modiji is the best")
if buttoninput:
    st.write("Yes, Modiji is the best!")
    st.audio("modih_ringtone.mp3",autoplay=True)
