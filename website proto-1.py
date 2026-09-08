import streamlit as st # type: ignore
st.title(":red[A simple e-commerce website prototype]")
st.subheader("Modiji")
st.image("modiji-17605779 (1).png", caption="Modiji")
selected_option = st.selectbox("Select an option", ["OG mantra", "To Meloni bhabhi", "Modi swear_1","Modi saiyara"])
if selected_option == "OG mantra":
    st.audio("modih_ringtone.mp3", autoplay=True)
elif selected_option == "To Meloni bhabhi":
    st.audio("kuchu-puchu-tum-kaha-ho.mp3", autoplay=True)
elif selected_option == "Modi swear_1":
    st.audio("modi-ji-bkl.mp3", autoplay=True)
elif selected_option == "Modi saiyara":
    st.audio("Saiyaara Modi Ji Version _ Faheem Abdullah _ {Modi ji Version} _ Yo Yo Modi Ji _ Covered By Modi Ji.mp3", autoplay=True)
st.success(f"you selected: {selected_option}")
st.subheader("Jaldi,the late")
st.video("videoplayback.mp4")