import streamlit as st
from random import randint

rnum_ = randint(0,255)
yes = {"y","yes","yeah","ok","sure"}
no = {"n","no","nope","bye"}
welcome = "Welcome to this randow number generator, please pick a number between 0 and 255.\nHit q or type quit when you have had enough :)\n"
turns = (0)

def yournum():
    global turns
    ans = st.text_input("What is your number?: ", key="num_input")
    turns += 1
    if ans in ("q","quit"):
        quit()
    else:
        try:
            rnum(int(ans))
        except:
            st.write("Try a number...\n")
            yournum()

def rnum(x):
    if x > rnum_:
        hi = x - rnum_
        st.write("Your number is ", hi, " higher than the random number")
        st.write("Turn number: ", turn)
        yournum()
    elif x < rnum_:
        lo = rnum_ - x
        st.write("Your number is ", lo, " lower than the random number")
        st.write("Turn number: ", turn)
        yournum()
    elif x == rnum_:
        st.write("Your number is exactly the random number, awesome!")
        ta()

def ta():
    ta_ = st.text_input("Do you want to try again?: ", key="try_again_input").lower()
    if ta in yes:
        rs()
    elif ta in no:
        quit()
    else:
        yournum()

def rs():
    global rnum 
    global turns
    rnum_ = randint(0,255)
    turns = (0)
    st.write(welcome)
    yournum()

#--- MAIN RUN CODE ---#
st.write(welcome)
yournum()
