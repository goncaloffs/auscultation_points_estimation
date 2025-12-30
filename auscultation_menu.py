# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from subprocess import Popen

def run_file(file_path):
    process = Popen(['python', file_path])
    process.wait()

def button_clicked(file_path, loading_label):
    loading_label.grid(row=1, column=0, columnspan=3) 
    run_file(file_path)
    loading_label.grid_forget()

def show_main_menu():
    start_frame.pack_forget()
    main_menu_frame.pack()

def show_info_popup(info_text):
    messagebox.showinfo("Information", info_text)

root = tk.Tk()
root.title("Auscultation")

style = ttk.Style()
style.configure("TButton",
                font=('Helvetica', 12, 'bold'),
                padding=(100, 20),
                foreground="#0096FF",
                background="#0096FF",
                borderwidth=5)

style.configure("Leave.TButton",
                font=('Helvetica', 12, 'bold'),
                padding=(10, 5),
                foreground="#0047AB",
                background="#0047AB",
                borderwidth=50)

start_frame = ttk.Frame(root, padding="20")
start_button = ttk.Button(start_frame, text="Start", command=show_main_menu, style="TButton")
start_button.pack(expand=True, fill='both')
start_frame.pack(expand=True, fill='both')

main_menu_frame = ttk.Frame(root, padding="20")

image_path1 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\auscultacao_coronaria.png'
image1 = Image.open(image_path1)
tk_image1 = ImageTk.PhotoImage(image1)

image_path2 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\auscultacao_anterior.png'
image2 = Image.open(image_path2)
tk_image2 = ImageTk.PhotoImage(image2)

image_path3 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\auscultacao_posterior.png'
image3 = Image.open(image_path3)
tk_image3 = ImageTk.PhotoImage(image3)

# Create buttons for each file in the main menu frame
file1_button = ttk.Button(main_menu_frame, text="Cardiac Auscultation", command=lambda: button_clicked(r'C:\Users\PC\Desktop\1200810_1201470_1201173\ausc_coronaria.py', loading_label), style="TButton")
file2_button = ttk.Button(main_menu_frame, text="Anterior Auscultation", command=lambda: button_clicked(r'C:\Users\PC\Desktop\1200810_1201470_1201173\ausc_pulmonar_anterior.py', loading_label), style="TButton")
file3_button = ttk.Button(main_menu_frame, text="Posterior Auscultation", command=lambda: button_clicked(r'C:\Users\PC\Desktop\1200810_1201470_1201173\ausc_pulmonar_posterior.py', loading_label), style="TButton")

file1_button.grid(row=1, column=0, pady=10, padx=10)
file2_button.grid(row=1, column=1, pady=10, padx=10)
file3_button.grid(row=1, column=2, pady=10, padx=10)

# Create a label to display the image
image_label1 = tk.Label(main_menu_frame, image=tk_image1)
image_label1.grid(row=2, column=0, pady=10)

image_label2 = tk.Label(main_menu_frame, image=tk_image2)
image_label2.grid(row=2, column=1, pady=10)

image_label3 = tk.Label(main_menu_frame, image=tk_image3)
image_label3.grid(row=2, column=2, pady=10)

# Create a label for the instruction text
instruction_label = tk.Label(main_menu_frame, text="Choose between the three auscultation modes:", font=('Helvetica', 14), pady=10)
instruction_label.grid(row=0, column=0, columnspan=3)

# Load your information icon using Pillow
info_icon_path1 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\info_icon-removebg-preview.png'
info_icon1 = Image.open(info_icon_path1)
info_icon1 = info_icon1.resize((40, 40), Image.LANCZOS)
tk_info_icon1 = ImageTk.PhotoImage(info_icon1)

info_icon_path2 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\info_icon-removebg-preview.png'
info_icon2 = Image.open(info_icon_path2)
info_icon2 = info_icon2.resize((40, 40), Image.LANCZOS)
tk_info_icon2 = ImageTk.PhotoImage(info_icon2)

info_icon_path3 = r'C:\Users\PC\Desktop\1200810_1201470_1201173\Images\info_icon-removebg-preview.png'
info_icon3 = Image.open(info_icon_path3)
info_icon3 = info_icon3.resize((40, 40), Image.LANCZOS)
tk_info_icon3 = ImageTk.PhotoImage(info_icon3)

# Create labels for the information icons
info_icon_label1 = tk.Label(main_menu_frame, image=tk_info_icon1)
info_icon_label1.grid(row=3, column=0, pady=10, padx=10)
info_icon_label1.bind("<Button-1>", lambda event: show_info_popup("During cardiac auscultation, the patient usually rests in the supine position (on their back), while the examiner stands to the right. The process begins in the aortic area (second right intercostal space), gradually progressing to the pulmonary area (second left intercostal space). It then moves to the left sternal border until it reaches the tricuspid area (lower left edge of the sternum) and finally to the mitral area (apex of the heart). The examiner should use both the diaphragm and the bell of the stethoscope to pick up various heart sounds."))

info_icon_label2 = tk.Label(main_menu_frame, image=tk_info_icon2)
info_icon_label2.grid(row=3, column=1, pady=10, padx=10)
info_icon_label2.bind("<Button-1>", lambda event: show_info_popup("Initially, the patient should be in a comfortable position, preferably seated or, if this is not possible, in the supine or lateral position. The doctor should prepare the stethoscope by warming it between their hands before placing it on the patient's chest. Auscultation begins in the anterior region of the chest, at the level of the lung apexes, descending to the base of the lungs."))

info_icon_label3 = tk.Label(main_menu_frame, image=tk_info_icon3)
info_icon_label3.grid(row=3, column=2, pady=10, padx=10)
info_icon_label3.bind("<Button-1>", lambda event: show_info_popup("Initially, the patient should be in a comfortable position, preferably seated or, if this is not possible, in the supine or lateral position. The doctor should prepare the stethoscope by warming it between their hands before placing it on the patient's chest. Auscultation begins in the posterior region of the chest, at the level of the lung apexes, descending to the base of the lungs."))

# Create a label for the information text
info_text_label = tk.Label(main_menu_frame, text="", font=('Helvetica', 10), foreground="gray")
info_text_label.grid(row=4, column=0, columnspan=3, pady=10, padx=10, sticky=tk.W)

# Create a loading label
loading_label = ttk.Label(main_menu_frame, text="Application Running", font=('Helvetica', 10), foreground="green")
loading_label.grid(row=5, column=0, columnspan=3, pady=10)

# Create a "Leave" button
leave_button = ttk.Button(main_menu_frame, text="Leave", command=root.destroy, style="Leave.TButton")
leave_button.grid(row=6, column=0, columnspan=3, pady=20)

main_menu_frame.pack_forget()

# Set the background color of the root window
root.configure(background='#f0f0f0')

# Open the window in fullscreen mode
root.attributes('-alpha', True)

# Start the Tkinter event loop
root.mainloop()

# Passados 10 segundos, tira print e guarda no PC
