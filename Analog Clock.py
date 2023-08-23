import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    # Clear the previous clock hands
    canvas.delete("all")

    # Draw clock face
    center_x = 150
    center_y = 150
    radius = 100
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black")

    # Draw hour hand
    hour_angle = math.radians(90 - hours * 30 - minutes * 0.5)  # Each hour is 30 degrees, each minute is 0.5 degrees
    hour_x = center_x + radius * 0.5 * math.cos(hour_angle)
    hour_y = center_y - radius * 0.5 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, width=6, fill="blue")

    # Draw minute hand
    minute_angle = math.radians(90 - minutes * 6)  # Each minute is 6 degrees
    minute_x = center_x + radius * 0.7 * math.cos(minute_angle)
    minute_y = center_y - radius * 0.7 * math.sin(minute_angle)
    canvas.create_line(center_x, center_y, minute_x, minute_y, width=4, fill="green")

    # Draw second hand
    second_angle = math.radians(90 - seconds * 6)  # Each second is 6 degrees
    second_x = center_x + radius * 0.8 * math.cos(second_angle)
    second_y = center_y - radius * 0.8 * math.sin(second_angle)
    canvas.create_line(center_x, center_y, second_x, second_y, width=2, fill="red")

    # Schedule the next update
    canvas.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Create the canvas to draw the clock
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Start updating the clock
update_clock()

# Run the GUI event loop
root.mainloop()
