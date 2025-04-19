import pyautogui as pyautogui
import pyperclip as pyperclip
import time
from geminiAI import chatResponse


def checkIfResponseFromSender(chat, user_name="Mohammed"):
    messages = chat.strip().split('/2025] ')[-1]
    if user_name in messages:
        return False
    return True


# Click on the chrome icon at the respective coordinates
pyautogui.click(1209, 1045)
time.sleep(1)

while True:
    # Drag mouse to select text of chat
    pyautogui.moveTo(720, 278)
    pyautogui.dragTo(678, 955, duration=1, button='left')

    # Copy the selected chat text to clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(690, 820) # To deselect the text

    chatHistory = pyperclip.paste()
    botResponse = chatResponse(chatHistory)

    if checkIfResponseFromSender(chatHistory):
        # Click at the response bar on whatsapp
        pyautogui.click(1027, 956)
        time.sleep(1)

        # Paste the generated response on to the reponse bar 
        pyperclip.copy(botResponse)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press("enter")
    else:
        print("No response")