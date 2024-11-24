import customtkinter as ctk

root = ctk.CTk()
root.geometry("520x430")
root.title("Color Picker")
root.iconbitmap()

r_value = 0
g_value = 0
b_value = 0 


def slider_event(value):
    print(value)

red = ctk.CTkLabel(root,text="R").pack()
red_slider = ctk.CTkSlider(root, from_=0, to=255, command=slider_event).pack()

green = ctk.CTkLabel(root,text="G").pack()
green_slider = ctk.CTkSlider(root, from_=0, to=255, command=slider_event).pack()

blue = ctk.CTkLabel(root,text="B").pack()
blue_slider = ctk.CTkSlider(root, from_=0, to=255, command=slider_event).pack()

preview_frame = ctk.CTkFrame(root, width= 220, height=220,corner_radius= 50).pack(pady=30)

root.mainloop()