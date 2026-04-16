import streamlit as st
import random

choices={
    "Rock":"stone.jpeg",
    "Paper":"paper.jpeg",
    "Scissor":"scissor.jpeg"
}
user_choice=st.selectbox("Choose your option",choices.keys())
com_choice=random.choice(list(choices.keys()))

if st.button("PLAY"):
    col1,col2,col3=st.columns([1,1,1])
    with col1:
        st.write("My Choice:")
        st.image(choices[user_choice])
    with col2:
        st.write("V/S")
    with col3:
        st.write("Computer Choice:")
        st.image(choices[com_choice])

     # Determine the winner
    if user_choice == com_choice:
        st.markdown("### It's a tie! 🤝")
    elif (user_choice == "Rock" and com_choice == "Scissor") or \
         (user_choice == "Paper" and com_choice == "Rock") or \
         (user_choice == "Scissor" and com_choice == "Paper"):
             st.markdown("### You win! 🏆")
    else:
        st.markdown("### You lose! 😢")
