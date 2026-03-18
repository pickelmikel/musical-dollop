import streamlit as st
from random import randint

rnum_ = 5#randint(0,255)
yes = {"y","yes","yeah","ok","sure"}
no = {"n","no","nope","bye"}
welcome = "Welcome to this random number generator, please pick a number between 0 and 255.\n" #Hit q or type quit when you have had enough :)\n"
turns = 0
blank = ''

if 'player_name' not in st.session_state:
    st.session_state['player_name'] = None
if 'high_scores' not in st.session_state:
    st.session_state['high_scores'] = []
if 'turns' not in st.session_state:
    st.session_state['turns'] = 0

def clear_text_input():
    st.session_state['last_num'] = st.session_state['num_input']
    st.session_state['num_input'] = ''

def save_high_score(score):
    #st.session_state['player_name'] =
    st.session_state['player_name'] = st.text_input("Nice going! What is your name?")
    with open("high_scores.txt", "a") as file:
        file.writelines(str(st.session_state['player_name']) + " ..... " + str(score) + "\n")
    

def paste_score():
    st.session_state['high_scores'].append(str(st.session_state['player_name']) + " ..... " + str(st.session_state['turns']) + "\n")

def show_top_scores():
    scores = []
    with open("high_scores.txt", "r") as file:
        for line in file:
            scores.append(int(line.strip()))
    scores.sort()
    st.write("Top 10 High Scores:")
    for i, score in enumerate(scores[:10]):
        st.write(f"{i+1}. {score}")

def yournum():
    global turns
    global ans
    st.session_state['player_name'] = ans = st.text_input("What is your number?: ", key="num_input", on_change=clear_text_input)
    
    try:
        rnum(int(st.session_state['last_num']))
    except ValueError:
        st.write("Try a number...")
    except KeyError:
        st.write('Ready and waiting...')

def rnum(x):
    global rnum_
    global turns
    st.session_state['turns'] += 1
    
    try:
        if x > rnum_:
            hi = x - rnum_
            st.write("Your number is ", hi, " higher than the random number")
        elif x < rnum_:
            lo = rnum_ - x
            st.write("Your number is ", lo, " lower than the random number")
        elif x == rnum_:
            st.write(f"Your number is exactly the random number in {st.session_state['turns']} trys, awesome!")
            st.balloons()
            #save_high_score(st.session_state['turns'])
            st.session_state['turns'] = 0
            
            #show_top_scores()
            rnum_ = None
    except AttributeError:
        st.write("Pick another one...")
    #st.write(st.session_state['high_scores'])

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
    turns = 0
    st.write(welcome)
    yournum()

#--- MAIN RUN CODE ---#
st.write(welcome)
yournum()
