import customtkinter as ctk
import pyperclip

# Initialize root window
root = ctk.CTk()
root.geometry("650x600")
root.title("Color Picker")
root.iconbitmap('favicon.ico') # "https://www.flaticon.com/fr/icones-gratuites/dessin" title="dessin icônes" icône créée par Freepik - Flaticon.io

# Initial RGB values - British Racing Green
r_value = [0]
g_value = [66]
b_value = [37]

rgb_label = ctk.CTkLabel(root, text=f"RGB: ({r_value[0]}, {g_value[0]}, {b_value[0]})")

# Function to update RGB values and change the background color of preview
def slider_event(value, color):
    if color == "red":
        r_value[0] = int(value)
    elif color == "green":
        g_value[0] = int(value)
    elif color == "blue":
        b_value[0] = int(value)
    
    # Update the preview color based on current RGB values
    updated_color = f'#{r_value[0]:02x}{g_value[0]:02x}{b_value[0]:02x}'
    preview_frame.configure(fg_color=updated_color)
    
    # Update RGB label
    rgb_label.configure(text=f"RGB: ({r_value[0]}, {g_value[0]}, {b_value[0]})")

# Create labels and sliders for RGB values
red = ctk.CTkLabel(root, text="R").pack()
red_slider = ctk.CTkSlider(root, from_=0, to=255, command=lambda value: slider_event(value, "red"))
red_slider.set(r_value[0])
red_slider.pack()

green = ctk.CTkLabel(root, text="G").pack()
green_slider = ctk.CTkSlider(root, from_=0, to=255, command=lambda value: slider_event(value, "green"))
green_slider.set(g_value[0])
green_slider.pack()

blue = ctk.CTkLabel(root, text="B").pack()
blue_slider = ctk.CTkSlider(root, from_=0, to=255, command=lambda value: slider_event(value, "blue"))
blue_slider.set(b_value[0])
blue_slider.pack()

# Preview frame 
preview_frame = ctk.CTkFrame(root, width=220, height=220, corner_radius=30)
preview_frame.pack(pady=30)

# Initial color update
slider_event(r_value[0], "red")
slider_event(g_value[0], "green")
slider_event(b_value[0], "blue")

# RGB Label

rgb_label.pack()

# Function to save RGB values (can be modified for a file saving mechanism)
def save_rgb_values():
    pyperclip.copy(f"Saved RGB Values: {r_value[0]}, {g_value[0]}, {b_value[0]}")
    print(f"Saved RGB Values: {r_value[0]}, {g_value[0]}, {b_value[0]}")

# Save button
save_button = ctk.CTkButton(root, command=save_rgb_values, text="Save RGB Values")
save_button.pack(pady=10)

# Quit button
quit_button = ctk.CTkButton(root, command=root.quit, text="Quit")
quit_button.pack()

root.mainloop()
