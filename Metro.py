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
fov_offsets = [0x0]
z_offsets = [0XE0, 0X20, 0X100, 0XEC]
health_offsets = [0X38, 0X2A8]
jump_offsets = [0X38, 0X16F8]
movement_offsets = [0X38, 0X16F0]
dead_z_offsets = [0X10, 0X8, 0X520, 0X738, 0X51C]
money = [0X10, 0XB8, 0X4F4]


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


def multi_run_money():
    new_thread = Thread(target=cash, daemon=True)
    new_thread.start()


def multi_run_fov():
    new_thread = Thread(target=fov, daemon=True)
    new_thread.start()


def multi_run_z():
    new_thread = Thread(target=Z, daemon=True)
    new_thread.start()


def multi_run_zd():
    new_thread = Thread(target=Zd, daemon=True)
    new_thread.start()


def multi_run_z2():
    new_thread = Thread(target=Z2, daemon=True)
    new_thread.start()


def multi_run_z3():
    new_thread = Thread(target=Z3, daemon=True)
    new_thread.start()


def cash():
    addr1 = getpointeraddress(module1 + 0x00D022D0, money)
    while 1:
        try:
            mem.write_int(addr1, 0x42c80000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def primary():
    addr1 = getpointeraddress(module1 + 0x00D01E50, primary_offsets)
    addr2 = getpointeraddress(module1 + 0x00D23550, health_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x100)
            mem.write_int(addr2, 0x3f800000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            break


def Z():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42c80000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def Z2():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def Z3():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x41700000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
            break


def fov():
    addr1 = getpointeraddress(module1 + 0x00D3EFD0, fov_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42b40000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F1"):
            mem.write_int(addr1, 0x424c0000)
            break


def Zd():
    addr1 = getpointeraddress(module1 + 0x00D01EB0, dead_z_offsets)
    while 1:
        try:
            mem.write_int(addr1, 0x42480000)
        except pymem.exception.MemoryWriteError as e:
            print(f"Error writing memory: {e}")
        if keyboard.is_pressed("F2"):
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
root.geometry("180x180")


def callback(url):
    webbrowser.open_new(url)


def show():
    root.deiconify()


def hide():
    root.withdraw()


# New graphics
button1 = tk.Button(root, text="Bullet go brrr", bg='black', fg='white', command=multi_run_primary)
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="Cash", bg='black', fg='white', command=multi_run_money)
button2.grid(row=2, column=0)
button3 = tk.Button(root, text="FOV", bg='black', fg='white', command=multi_run_fov)
button3.grid(row=3, column=0)
button4 = tk.Button(root, text="FLY Tower", bg='black', fg='white', command=multi_run_z)
button4.grid(row=4, column=0)
button5 = tk.Button(root, text="FLY Dead city", bg='black', fg='white', command=multi_run_zd)
button5.grid(row=5, column=0)
button6 = tk.Button(root, text="Exit", bg='white', fg='black', command=root.destroy)
button6.grid(row=6, column=0)
# Hot keys
keyboard.add_hotkey("-", show)
keyboard.add_hotkey("+", hide)
keyboard.add_hotkey("K", root.destroy)
keyboard.add_hotkey("3", multi_run_z)
keyboard.add_hotkey("6", multi_run_z2)
keyboard.add_hotkey("9", multi_run_z3)

root.mainloop()
