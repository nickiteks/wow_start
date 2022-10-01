import subprocess

import pyautogui
import time
import os
from settings import File_Path,Password


subprocess.Popen(f'{File_Path}')
time.sleep(3)
pyautogui.write(Password)
pyautogui.press('enter')
