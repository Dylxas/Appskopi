from curses import window
import io
import os
import cv2
import pickle
import random
import sys
import tkinter
import customtkinter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import sklearn.metrics as metrics

from os import listdir
from PIL import Image, ImageTk
from threading import Thread
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score, f1_score
from tkinter import ttk, filedialog

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")

text_var = tkinter.StringVar(value="CTkLabel")
label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=350,
                               height=350,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label.place(relx=0.25, rely=0.35, anchor=tkinter.CENTER)

text_var1 = tkinter.StringVar(value="CTkLabel")
label1 = customtkinter.CTkLabel(master=app,
                               textvariable=text_var1,
                               width=350,
                               height=350,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label1.place(relx=0.75, rely=0.35, anchor=tkinter.CENTER)

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=app,
                                 width=350,
                                 height=60,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Proses Citra",
                                 command=button_event)
button.place(relx=0.25, rely=0.75, anchor=tkinter.CENTER)

app.mainloop()