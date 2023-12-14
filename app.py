from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess
import ctypes
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_batch_file_as_admin(batch_file_path):
    if is_admin():
        subprocess.run([batch_file_path], check=True, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )

window = Tk()
window.iconbitmap("icon.ico")
window.title("System Multi Tool")

def gui_main():
    OUTPUT_PATH = resource_path(Path(__file__).parent)
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window.geometry("546x572")
    window.configure(bg = "#62775E")


    canvas = Canvas(
        window,
        bg = "#62775E",
        height = 572,
        width = 546,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        273.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        507.0,
        49.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sys.exit,
        relief="flat"
    )
    button_1.place(
        x=72.0,
        y=465.0,
        width=185.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=power,
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=379.0,
        width=183.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=browser,
        relief="flat"
    )
    button_3.place(
        x=71.0,
        y=295.0,
        width=189.0,
        height=80.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_5.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_6.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        234.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        45.0,
        253.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        44.0,
        171.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        46.0,
        420.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        43.0,
        333.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        45.0,
        500.0,
        image=image_image_9
    )
    window.resizable(False, False)
    window.mainloop()

def volume():
    OUTPUT_PATH = resource_path(Path(__file__).parent)
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window.geometry("546x572")
    window.configure(bg = "#62775E")


    canvas = Canvas(
        window,
        bg = "#62775E",
        height = 572,
        width = 546,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        273.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        507.0,
        49.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sys.exit,
        relief="flat"
    )
    button_1.place(
        x=72.0,
        y=465.0,
        width=185.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=power,
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=379.0,
        width=183.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=browser,
        relief="flat"
    )
    button_3.place(
        x=71.0,
        y=295.0,
        width=189.0,
        height=80.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_5.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_6.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        234.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        45.0,
        253.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        44.0,
        171.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        46.0,
        420.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        43.0,
        333.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        45.0,
        500.0,
        image=image_image_9
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\volumedown.bat'),
        relief="flat"
    )
    button_7.place(
        x=282.0,
        y=301.0,
        width=226.0,
        height=202.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\volumeup.bat'),
        relief="flat"
    )
    button_8.place(
        x=282.0,
        y=179.0,
        width=220.0,
        height=175.0
    )
    window.resizable(False, False)
    window.mainloop()

def wifi():
    OUTPUT_PATH = resource_path(Path(__file__).parent)
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window.geometry("546x572")
    window.configure(bg = "#62775E")


    canvas = Canvas(
        window,
        bg = "#62775E",
        height = 572,
        width = 546,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        273.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        507.0,
        49.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sys.exit,
        relief="flat"
    )
    button_1.place(
        x=72.0,
        y=465.0,
        width=185.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=power,
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=379.0,
        width=183.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=browser,
        relief="flat"
    )
    button_3.place(
        x=71.0,
        y=295.0,
        width=189.0,
        height=80.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_5.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_6.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        234.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        45.0,
        253.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        44.0,
        171.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        46.0,
        420.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        43.0,
        333.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        45.0,
        500.0,
        image=image_image_9
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\disablewifi.bat'),
        relief="flat"
    )
    button_7.place(
        x=315.0,
        y=349.0,
        width=158.0,
        height=103.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\enablewifi.bat'),
        relief="flat"
    )
    button_8.place(
        x=315.0,
        y=189.0,
        width=158.0,
        height=103.0
    )
    window.resizable(False, False)
    window.mainloop()

def browser():
    OUTPUT_PATH = resource_path(Path(__file__).parent)
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window.geometry("546x572")
    window.configure(bg = "#62775E")


    canvas = Canvas(
        window,
        bg = "#62775E",
        height = 572,
        width = 546,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        273.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        507.0,
        49.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sys.exit,
        relief="flat"
    )
    button_1.place(
        x=72.0,
        y=465.0,
        width=185.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=power,
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=379.0,
        width=183.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=browser,
        relief="flat"
    )
    button_3.place(
        x=71.0,
        y=295.0,
        width=189.0,
        height=80.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_5.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_6.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        234.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        45.0,
        253.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        44.0,
        171.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        46.0,
        420.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        43.0,
        333.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        45.0,
        500.0,
        image=image_image_9
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\facebook.bat'),
        relief="flat"
    )
    button_7.place(
        x=297.0,
        y=305.0,
        width=101.0,
        height=102.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\youtube.bat'),
        relief="flat"
    )
    button_8.place(
        x=394.0,
        y=194.0,
        width=101.0,
        height=102.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\gmail.bat'),
        relief="flat"
    )
    button_9.place(
        x=398.0,
        y=294.0,
        width=101.0,
        height=102.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\twitter.bat'),
        relief="flat"
    )
    button_10.place(
        x=298.0,
        y=410.0,
        width=101.0,
        height=102.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\instagram.bat'),
        relief="flat"
    )
    button_11.place(
        x=397.0,
        y=401.0,
        width=101.0,
        height=102.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\google.bat'),
        relief="flat"
    )
    button_12.place(
        x=286.0,
        y=190.0,
        width=101.0,
        height=102.0
    )
    window.resizable(False, False)
    window.mainloop()

def power():

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    window.geometry("546x572")
    window.configure(bg = "#62775E")


    canvas = Canvas(
        window,
        bg = "#62775E",
        height = 572,
        width = 546,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        394.0,
        337.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        273.0,
        49.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        507.0,
        49.0,
        image=image_image_3
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=sys.exit,
        relief="flat"
    )
    button_1.place(
        x=72.0,
        y=465.0,
        width=185.0,
        height=81.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=power,
        relief="flat"
    )
    button_2.place(
        x=74.0,
        y=379.0,
        width=183.0,
        height=80.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=browser,
        relief="flat"
    )
    button_3.place(
        x=71.0,
        y=295.0,
        width=189.0,
        height=80.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_4.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=wifi,
        relief="flat"
    )
    button_5.place(
        x=69.0,
        y=210.0,
        width=191.0,
        height=82.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_6.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=volume,
        relief="flat"
    )
    button_7.place(
        x=69.0,
        y=130.0,
        width=186.0,
        height=80.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        234.0,
        49.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        45.0,
        253.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        44.0,
        171.0,
        image=image_image_6
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7.png"))
    image_7 = canvas.create_image(
        46.0,
        420.0,
        image=image_image_7
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8.png"))
    image_8 = canvas.create_image(
        43.0,
        333.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9.png"))
    image_9 = canvas.create_image(
        45.0,
        500.0,
        image=image_image_9
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\restart.bat'),
        relief="flat"
    )
    button_8.place(
        x=275.0,
        y=372.0,
        width=224.0,
        height=85.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: run_batch_file_as_admin(r'assets\batchfiles\shutdown.bat'),
        relief="flat"
    )
    button_9.place(
        x=276.0,
        y=235.0,
        width=239.0,
        height=87.0
    )
    window.resizable(False, False)
    window.mainloop()

gui_main()
window.mainloop()