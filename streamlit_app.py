import streamlit as st
from random import randint

rnum_ = randint(0,255)
yes = {"y","yes","yeah","ok","sure"}
no = {"n","no","nope","bye"}
welcome = "Welcome to this random number generator, please pick a number between 0 and 255.\n" #Hit q or type quit when you have had enough :)\n"
turns = (0)
blank = ''

def clear_text_input():
    ans.empty()


def yournum():
    global turns
    global ans
    ans = 0
    ans.empty()
    ans = st.text_input("What is your number?: ", key="num_input")
    turns += 1
    
    try:
        rnum(int(ans))
    except ValueError:
        st.write("Try a number...")

def rnum(x):
    global rnum_
    try:
        if x > rnum_:
            hi = x - rnum_
            st.write("Your number is ", hi, " higher than the random number")
        elif x < rnum_:
            lo = rnum_ - x
            st.write("Your number is ", lo, " lower than the random number")
        elif x == rnum_:
            st.write("Your number is exactly the random number, awesome!")
            rnum_ = None
    except AttributeError:
        st.write("Pick another one...")

def ta():
    ta_ = st.text_input("Do you want to try again?: ", key="try_again_input").lower()
    if ta in yes:
        rs()
    elif ta in no:
        quit()
    else:
        yournum()

def rs():
    global rnum_ 
    global turns
    if rnum_ is None:
        rnum_ = randint(0,255)
    turns = (0)
    st.write(welcome)
    yournum()

#--- MAIN RUN CODE ---#
st.write(welcome)
yournum()
