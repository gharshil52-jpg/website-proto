import streamlit as st
import pandas as pd
st.title(":red[Legends of chutiyapa]")
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
st.video("videoplayback.mp4", autoplay=True,caption="Money follows my brother")
st.subheader("Rahul Gandhi")
st.image("rahul_gandhi.jpg", caption="Rahul Gandhi")
df=pd.read_csv("Cs.csv")
with st.expander("See season 1 players and their stats"):
    st.write("Mahatma Gandhi: Father of the Nation, played 100 matches, scored 5000 runs.")
    st.write("Jawaharlal Nehru: First Prime Minister of India, played 80 matches, scored 4000 runs.")
    st.write("Bhagat Singh: Freedom fighter, played 60 matches, scored 3000 runs.")
    st.write("Sardar Vallabhbhai Patel: Iron Man of India, played 90 matches, scored 4500 runs.")
    st.write("Subhas Chandra Bose: Leader of the Indian National Army, played 70 matches, scored 3500 runs.")
    st.write("Lal Bahadur Shastri: Second Prime Minister of India, played 50 matches, scored 2500 runs.")
if st.expander:
    st.dataframe(df)
