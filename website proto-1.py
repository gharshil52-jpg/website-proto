import streamlit as st
st.title(":red[A simple e-commerce website prototype]")
st.subheader("This is a simple e-commerce website prototype built using Streamlit.")
st.write("You can use this prototype to add products to the cart and allow users to browse and purchase them.")
st.image("modiji-17605779 (1).png", caption="Modiji")
selected_option = st.selectbox("Select an option", ["OG mantra", "To Meloni bhabhi", "Modi swear_1","Modi saiyara"])
if selected_option == "OG mantra":
    st.write("You selected the OG mantra!")
    st.audio("modih_ringtone.mp3", autoplay=True)
elif selected_option == "To Meloni bhabhi":
    st.write("You selected To Meloni bhabhi!")
    st.audio("kuchu-puchu-tum-kaha-ho.mp3", autoplay=True)
elif selected_option == "Modi swear_1":
    st.write("You selected Modi swear_1!")
    st.audio("modi-ji-bkl.mp3", autoplay=True)
elif selected_option == "Modi saiyara":
    st.write("You selected Modi saiyara!")
    st.audio("Saiyaara Modi Ji Version _ Faheem Abdullah _ {Modi ji Version} _ Yo Yo Modi Ji _ Covered By Modi Ji.mp3", autoplay=True)
