import os
import ctypes
import time
import subprocess
import winsound
import ctypes
import threading

from PIL import Image

image_path = "wallpaper.png"

batch_script_path = "setup.bat"

sound_file_path = "sound.wav"

delay_seconds = 5

import ctypes

def minimize_all_windows():
    def enum_handler(hwnd, lParam):
        if ctypes.windll.user32.IsWindowVisible(hwnd) and not ctypes.windll.user32.IsIconic(hwnd):
            ctypes.windll.user32.ShowWindow(hwnd, 6)
        return True

    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_ulong, ctypes.c_ulong)
    enum_handler_type = WNDENUMPROC(enum_handler)
    ctypes.windll.user32.EnumWindows(enum_handler_type, None)

def set_wallpaper(image_path):
    try:
        image = Image.open(image_path)

        screen_width, screen_height = image.size

        image = image.resize((screen_width, screen_height), resample=Image.BICUBIC)

        temp_file_path = os.path.join(os.path.dirname(__file__), "temp_wallpaper.bmp")
        image.save(temp_file_path, "BMP")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, temp_file_path, 0)
    except Exception as e:
        print(f"Error setting wallpaper: {e}")

def run_batch_script(batch_script_path):
    subprocess.run(batch_script_path, shell=True)

def play_sound(sound_file_path):
    winsound.PlaySound(sound_file_path, winsound.SND_FILENAME)

def main():
    set_wallpaper(image_path)
    minimize_all_windows()
    time.sleep(delay_seconds)
    play_sound(sound_file_path)
    run_batch_script(batch_script_path)
if __name__ == "__main__":
    main()