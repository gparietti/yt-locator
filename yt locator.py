import pyautogui
import webbrowser
import time
webbrowser.open("https://www.youtube.com/")
time.sleep(3)
nomevideo = pyautogui.prompt(text="", title="Inserisci il titolo del video che desideri cercare.")
time.sleep(5)
pyautogui.click(3223, 164)
pyautogui.write(nomevideo)
time.sleep(3)
pyautogui.hotkey("enter")




