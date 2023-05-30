import streamlit as st
import time

class Timer:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
    
    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
    
    def pause(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
    
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

class TimerApp:
    def __init__(self):
        self.timers = [Timer(f"Timer {i+1}") for i in range(4)]
        self.create_widgets()
    
    def create_widgets(self):
        self.timer_labels = []
        self.start_buttons = []
        self.pause_buttons = []
        self.reset_buttons = []
        
        for i in range(4):
            timer_label = st.empty()
            self.timer_labels.append(timer_label)
            
            start_button = st.button(f"Start Timer {i+1}", key=f"start_{i}")
            self.start_buttons.append(start_button)
            
            pause_button = st.button(f"Pause Timer {i+1}", key=f"pause_{i}")
            self.pause_buttons.append(pause_button)
            
            reset_button = st.button(f"Reset Timer {i+1}", key=f"reset_{i}")
            self.reset_buttons.append(reset_button)
    
    def start_timer(self, i):
        self.timers[i].start()
        self.update_timers()
    
    def pause_timer(self, i):
        self.timers[i].pause()
        self.update_timers()
    
    def reset_timer(self, i):
        self.timers[i].reset()
        self.update_timers()
    
    def update_timers(self):
        for i in range(4):
            if self.timers[i].running:
                elapsed_time = self.timers[i].elapsed_time + time.time() - self.timers[i].start_time
            else:
                elapsed_time = self.timers[i].elapsed_time
            
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
            self.timer_labels[i].text(f"{self.timers[i].name}: {minutes:02d}:{seconds:02d}:{milliseconds:03d}")
        
        time.sleep(0.01)
        self.update_timers()

app = TimerApp()
for i in range(4):
    if app.start_buttons[i]:
        app.start_timer(i)
    if app.pause_buttons[i]:
        app.pause_timer(i)
    if app.reset_buttons[i]:
        app.reset_timer(i)
app.update_timers()
