import keyboard
import tkinter as tk
import pygame
import pymem.exception
import webbrowser
from threading import Thread
from pymem import *
from pymem.process import *
from pymem.ptypes import RemotePointer

# Password
while True:
    password = input("Enter password ")
    if password == "2033":
        print("Welcome")
        break
    else:
        print("Try again retard")

# Game were hacking
mem = Pymem("metro")

# DLL of said game
module1 = module_from_name(mem.process_handle, "metro.exe").lpBaseOfDll

primary_offsets = [0X8, 0XC8, 0X8, 0X8, 0X440]


def getpointeraddress(base, offsets):
    remote_pointer = RemotePointer(mem.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(mem.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


# Threads
def multi_run_primary():
    new_thread = Thread(target=primary, daemon=True)
    new_thread.start()


def primary():
    addr1 = getpointeraddress(module1 + 0x00D01E50, primary_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x100)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


pygame.init()
pygame.mixer_music.load("music/mod.mp3")
pygame.mixer_music.play(1)

root = tk.Tk()
photo = tk.PhotoImage(file="back/155.png")
root.wm_iconphoto(False, photo)
root.attributes("-topmost", True)
root.title("Fragging Terminal")
root.configure(background='dark red')
root.geometry("370x230")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# New graphics
button1 = tk.Button(root, text="Bullet go brrr", bg='black', fg='white', command=multi_run_primary)
button1.grid(row=1, column=0)

# Hot keys
keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("K", root.destroy)
root.mainloop()