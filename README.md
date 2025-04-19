# WhatsApp Auto-Reply Bot with Python

This project demonstrates how to create a WhatsApp auto-reply bot using Python. It leverages libraries like `pyautogui`, `pyperclip`, and `google-genai` to automate interactions and generate responses.

## Table of Contents

1.  [Project Description](#project-description)
2.  [Features](#features)
3.  [Dependencies](#dependencies)
4.  [Setup](#setup)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Configuration](#configuration)
5.  [Usage](#usage)
6.  [Code Structure](#code-structure)
7.  [Contributing](#contributing)

## 1.  Project Description

This project creates a Python-based WhatsApp auto-reply bot. The bot automates the process of reading incoming WhatsApp messages and sending AI-generated responses. It uses `pyautogui` to control the mouse and keyboard, `pyperclip` to handle clipboard operations, and `google-genai` to generate the automated replies.

## 2.  Features

* **Automated Message Handling:** Automatically reads incoming WhatsApp messages.
* **AI-Powered Responses:** Generates replies using the Google Gemini AI.
* **Conditional Responding:** Only responds to messages from other users.
* **Continuous Operation:** Runs in a loop to continuously monitor and respond to messages.

## 3.  Dependencies

* `pyautogui`: For controlling mouse and keyboard.
* `pyperclip`: For interacting with the clipboard.
* `time`: For adding delays.
* `google-genai`: For generating AI-powered responses.

## 4.  Setup

### Prerequisites

* Python 3.6 or higher.
* A Google account with access to the Gemini API.
* A desktop computer with WhatsApp Web access.
* Brave Browser

### Installation

1.  **Install Python:** If you don't have Python installed, download it from the official website (python.org) and follow the installation instructions.

2.  **Install the required Python packages:**

    ```
    pip install pyautogui pyperclip google-genai
    ```

### Configuration

1.  **Set up Gemini API:**

    * Create a Google Cloud project.
    * Enable the Gemini API.
    * Obtain an API key.

2.  **Get Browser Coordinates:**

    * Run the `getCoordinates.py` script to get the coordinates of your Brave browser icon on the desktop.

        * Create a file named `getCoordinates.py`

        * Run the script and move your mouse over the Brave browser icon.

        * Press Ctrl+C to stop the script and copy the coordinates.

3.  **Configure `main.py`:**

    * Create a file named `main.py`.
    * Import the required modules
    * Use the coordinates obtained from `getCoordinates.py` with `pyautogui.click()` to open Brave Browser and navigate to web.whatsapp.com.
    * Use `pyautogui` and `pyperclip` to read the text
    * Use `google-genai` to generate a response.
    * Use `pyautogui.write()` and `pyautogui.press('enter')` to send the response.
    * Enclose the functionality in a `while` loop

4.  **Configure `geminiAI.py`:**

    * Create a file named `geminiAI.py`.
    * Add the code to set up and use the Gemini API to generate responses.  This will include your API key.
    * Create a function that takes the incoming message as an argument and returns the AI-generated response.
    * Import this function into `main.py`.

## 5.  Usage

1.  Ensure WhatsApp Web is open in your Brave browser.
2.  Run the `main.py` script.
3.  The bot will start automatically responding to new messages in WhatsApp.

## 6.  Code Structure

* `getCoordinates.py`: A script to get the coordinates of screen elements.
* `main.py`: The main script that controls the bot's logic.
* `geminiAI.py`: A module for interacting with the Gemini AI to generate responses.

## 7.  Contributing

Contributions are welcome!  Feel free to submit pull requests or open issues to suggest improvements or report bugs.

