import tkinter as tk
import ctypes
import threading
import time

# Function to simulate key press
def press_key():
    ctypes.windll.user32.keybd_event(0x20, 0, 0, 0)  # Press the Space key
    ctypes.windll.user32.keybd_event(0x20, 0, 2, 0)  # Release the Space key

# Function to update the timer display
def update_timer():
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, screen_time_limit - elapsed_time)
    minutes, seconds = divmod(remaining_time, 60)
    timer_label.config(text=f" Alper Kalan Zaman: {minutes:02d}:{seconds:02d}")
    if remaining_time == 0:
        alper.destroy()

# Function to limit screen time
def limit_screen_time():
    global start_time, screen_time_limit
    screen_time_limit = 2 * 60 * 60  # 2 hours in seconds

    start_time = time.time()

    while time.time() - start_time < screen_time_limit:
        # Simulate key press every minute
        time.sleep(60)
        press_key()
        update_timer()

    # Exit the program or perform other actions when the time limit is reached
    print("Screen time limit reached. Exiting program.")
    alper.destroy()

# Create a thread for limiting screen time
screen_time_thread = threading.Thread(target=limit_screen_time)

# Start the thread
screen_time_thread.start()

# Create the main Tkinter window
alper = tk.Tk()
alper.title("Screen Time Limit")

# Create a label to display the timer
timer_label = tk.Label(alper, text="Alper Kalan Zaman: 02:00", font=("Helvetica", 16))
timer_label.pack(pady=20)

# Your additional GUI code goes here

# Start the Tkinter main loop
alper.mainloop()
 