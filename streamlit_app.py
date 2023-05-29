

import streamlit as st
from random import randint

rnum_ = randint(0,255)
yes = {"y","yes","yeah","ok","sure"}
no = {"n","no","nope","bye"}
welcome = "Welcome to this randow number generator, please pick a number between 0 and 255.\nHit q or type quit when you have had enough :)\n"
turns = (0)

def yournum():
    global turns
    ans = st.text_input("What is your number?: ", key = "ans")
    turns += 1
    while turns < 3:
        if ans in ("q","quit"):
            quit()
        else:
            try:
                rnum(int(ans))
            except:
                st.text("Try a number...\n")
                yournum()
    else:
        st.text("You are out of turns")
        rs()

def rnum(x):
    if x > rnum_:
        hi = x - rnum_
        st.text("Your number is ", hi, " higher than the random number")
    elif x < rnum_:
        lo = rnum_ - x
        st.text("Your number is ", lo, " lower than the random number")
    elif x == rnum_:
        st.text("Your number is exactly the random number, awesome!")
        ta()
    yournum()

def ta():
    ta_ = st.text_input("Do you want to try again?: ").lower()
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
    st.text(welcome)
    yournum()

#--- MAIN RUN CODE ---#
st.text(welcome)
yournum()
