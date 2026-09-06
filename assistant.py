import datetime
import os
import shutil
import subprocess
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()
engine.setProperty("rate", 170)

recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("\nListening...")

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=7
            )

            command = recognizer.recognize_google(audio).lower().strip()
            print("You:", command)
            return command

        except sr.WaitTimeoutError:
            speak("I did not hear anything.")

        except sr.UnknownValueError:
            speak("Sorry, I could not understand that.")

        except sr.RequestError:
            speak("Speech recognition needs an internet connection.")

    return ""


def open_program(program):
    try:
        programs = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "wordpad": "write.exe",
            "task manager": "taskmgr.exe",
            "control panel": "control.exe",
            "command prompt": "cmd.exe",
            "powershell": "powershell.exe",
            "file explorer": "explorer.exe"
        }

        if program in programs:
            subprocess.Popen(programs[program])
            speak("Opening " + program)
            return

        if program == "word":
            paths = [
                "WINWORD.EXE",
                r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
                r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
            ]

            for path in paths:
                if shutil.which(path):
                    subprocess.Popen(path)
                    speak("Opening Microsoft Word.")
                    return

            speak("Microsoft Word was not found.")
            return

        if program == "excel":
            paths = [
                "EXCEL.EXE",
                r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
                r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
            ]

            for path in paths:
                if shutil.which(path):
                    subprocess.Popen(path)
                    speak("Opening Microsoft Excel.")
                    return

            speak("Microsoft Excel was not found.")
            return

        if program == "powerpoint":
            paths = [
                "POWERPNT.EXE",
                r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
                r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
            ]

            for path in paths:
                if shutil.which(path):
                    subprocess.Popen(path)
                    speak("Opening Microsoft PowerPoint.")
                    return

            speak("Microsoft PowerPoint was not found.")
            return

        if program == "vscode":
            code = shutil.which("code")

            if code:
                subprocess.Popen([code])
                speak("Opening Visual Studio Code.")
            else:
                speak("Visual Studio Code was not found.")

    except Exception as error:
        print(error)
        speak("I could not open that application.")


def open_website(url, name):
    webbrowser.open(url)
    speak("Opening " + name)


def search_google(query):
    url = "https://www.google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    speak("Searching for " + query)


def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
    speak("Searching YouTube for " + query)


def create_folder():
    folder = os.path.join(os.getcwd(), "MyFolder")
    os.makedirs(folder, exist_ok=True)
    speak("MyFolder has been created.")


def take_screenshot():
    filename = (
        "screenshot_"
        + datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".png"
    )

    pyautogui.screenshot(filename)
    speak("Screenshot saved as " + filename)


def handle_command(command):

    if not command:
        return True

    if command in ["hello", "hi", "hey"]:
        speak("Hello! How can I help you?")

    elif "good morning" in command:
        speak("Good morning! Have a great day.")

    elif "good afternoon" in command:
        speak("Good afternoon! How can I help you?")

    elif "good evening" in command:
        speak("Good evening! How can I help you?")

    elif "how are you" in command:
        speak("I am doing great. Thank you for asking.")

    elif "your name" in command:
        speak("I am your Python Voice Control Assistant.")

    elif "time" in command:
        speak(
            "The time is "
            + datetime.datetime.now().strftime("%I:%M %p")
        )

    elif "date" in command or "today" in command:
        speak(
            "Today is "
            + datetime.datetime.now().strftime("%d %B %Y")
        )

    elif "day" in command:
        speak(
            "Today is "
            + datetime.datetime.now().strftime("%A")
        )

    elif "youtube" in command and "search" not in command:
        open_website("https://www.youtube.com", "YouTube")

    elif "google" in command and "search" not in command:
        open_website("https://www.google.com", "Google")

    elif "gmail" in command:
        open_website("https://mail.google.com", "Gmail")

    elif "google drive" in command:
        open_website("https://drive.google.com", "Google Drive")

    elif "google maps" in command:
        open_website("https://maps.google.com", "Google Maps")

    elif "google docs" in command:
        open_website("https://docs.google.com", "Google Docs")

    elif "google sheets" in command:
        open_website("https://sheets.google.com", "Google Sheets")

    elif "google slides" in command:
        open_website("https://slides.google.com", "Google Slides")

    elif "github" in command:
        open_website("https://github.com", "GitHub")

    elif "linkedin" in command:
        open_website("https://www.linkedin.com", "LinkedIn")

    elif "instagram" in command:
        open_website("https://www.instagram.com", "Instagram")

    elif "facebook" in command:
        open_website("https://www.facebook.com", "Facebook")

    elif "whatsapp" in command:
        open_website("https://web.whatsapp.com", "WhatsApp")

    elif "netflix" in command:
        open_website("https://www.netflix.com", "Netflix")

    elif "amazon" in command:
        open_website("https://www.amazon.in", "Amazon")

    elif "flipkart" in command:
        open_website("https://www.flipkart.com", "Flipkart")

    elif "chatgpt" in command:
        open_website("https://chatgpt.com", "ChatGPT")

    elif "code with harry" in command:
        search_youtube("Code With Harry")

    elif command.startswith("search youtube for "):
        query = command.replace("search youtube for ", "", 1).strip()

        if query:
            search_youtube(query)

    elif command.startswith("youtube search "):
        query = command.replace("youtube search ", "", 1).strip()

        if query:
            search_youtube(query)

    elif command.startswith("search google for "):
        query = command.replace("search google for ", "", 1).strip()

        if query:
            search_google(query)

    elif command.startswith("search for "):
        query = command.replace("search for ", "", 1).strip()

        if query:
            search_google(query)

    elif command.startswith("search "):
        query = command.replace("search ", "", 1).strip()

        if query:
            search_google(query)

    elif "microsoft word" in command or command == "word" or "open word" in command:
        open_program("word")

    elif "microsoft excel" in command or command == "excel" or "open excel" in command:
        open_program("excel")

    elif "microsoft powerpoint" in command or command == "powerpoint" or "open powerpoint" in command:
        open_program("powerpoint")

    elif "notepad" in command:
        open_program("notepad")

    elif "calculator" in command or command == "calc":
        open_program("calculator")

    elif "paint" in command:
        open_program("paint")

    elif "wordpad" in command:
        open_program("wordpad")

    elif "file explorer" in command or command == "files" or "open files" in command or "explorer" in command:
        open_program("file explorer")

    elif "vs code" in command or "visual studio code" in command or command == "code":
        open_program("vscode")

    elif "task manager" in command:
        open_program("task manager")

    elif "control panel" in command:
        open_program("control panel")

    elif "command prompt" in command or command == "cmd":
        open_program("command prompt")

    elif "powershell" in command:
        open_program("powershell")

    elif "open project folder" in command or "open project" in command:
        os.startfile(os.getcwd())
        speak("Opening the project folder.")

    elif "create folder" in command or command == "folder" or "make folder" in command:
        create_folder()

    elif "open desktop" in command:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        os.startfile(desktop)
        speak("Opening Desktop.")

    elif "open downloads" in command:
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        os.startfile(downloads)
        speak("Opening Downloads.")

    elif "open documents" in command:
        documents = os.path.join(os.path.expanduser("~"), "Documents")
        os.startfile(documents)
        speak("Opening Documents.")

    elif "open pictures" in command:
        pictures = os.path.join(os.path.expanduser("~"), "Pictures")
        os.startfile(pictures)
        speak("Opening Pictures.")

    elif "open music" in command:
        music = os.path.join(os.path.expanduser("~"), "Music")
        os.startfile(music)
        speak("Opening Music.")

    elif "open videos" in command:
        videos = os.path.join(os.path.expanduser("~"), "Videos")
        os.startfile(videos)
        speak("Opening Videos.")

    elif "open recycle bin" in command:
        subprocess.Popen(
            'explorer.exe shell:RecycleBinFolder',
            shell=True
        )
        speak("Opening Recycle Bin.")

    elif "take screenshot" in command or "screenshot" in command:
        take_screenshot()

    elif "open calculator" in command:
        open_program("calculator")

    elif "open paint" in command:
        open_program("paint")

    elif "open notepad" in command:
        open_program("notepad")

    elif "open browser" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening the browser.")

    elif "open chrome" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Chrome.")

    elif "open edge" in command:
        subprocess.Popen("msedge.exe")
        speak("Opening Microsoft Edge.")

    elif "open python" in command:
        search_google("Python programming")

    elif "open stack overflow" in command:
        open_website(
            "https://stackoverflow.com",
            "Stack Overflow"
        )

    elif "open w3schools" in command:
        open_website(
            "https://www.w3schools.com",
            "W3Schools"
        )

    elif "open geeksforgeeks" in command:
        open_website(
            "https://www.geeksforgeeks.org",
            "GeeksforGeeks"
        )

    elif "open kaggle" in command:
        open_website(
            "https://www.kaggle.com",
            "Kaggle"
        )

    elif "open coursera" in command:
        open_website(
            "https://www.coursera.org",
            "Coursera"
        )

    elif "open udemy" in command:
        open_website(
            "https://www.udemy.com",
            "Udemy"
        )

    elif "open spotify" in command:
        open_website(
            "https://open.spotify.com",
            "Spotify"
        )

    elif "play music" in command:
        open_website(
            "https://open.spotify.com",
            "Spotify"
        )

    elif "play youtube" in command:
        open_website(
            "https://www.youtube.com",
            "YouTube"
        )

    elif "open calendar" in command:
        open_website(
            "https://calendar.google.com",
            "Google Calendar"
        )

    elif "open classroom" in command:
        open_website(
            "https://classroom.google.com",
            "Google Classroom"
        )

    elif "open canva" in command:
        open_website(
            "https://www.canva.com",
            "Canva"
        )

    elif "open reddit" in command:
        open_website(
            "https://www.reddit.com",
            "Reddit"
        )

    elif "open x" in command or "open twitter" in command:
        open_website(
            "https://x.com",
            "X"
        )

    elif "open telegram" in command:
        open_website(
            "https://web.telegram.org",
            "Telegram"
        )

    elif "open wikipedia" in command:
        open_website(
            "https://www.wikipedia.org",
            "Wikipedia"
        )

    elif "open news" in command:
        open_website(
            "https://news.google.com",
            "Google News"
        )

    elif "open weather" in command:
        open_website(
            "https://www.google.com/search?q=weather",
            "Weather"
        )

    elif "open maps" in command:
        open_website(
            "https://maps.google.com",
            "Google Maps"
        )

    elif "open translate" in command:
        open_website(
            "https://translate.google.com",
            "Google Translate"
        )

    elif "open calculator online" in command:
        open_website(
            "https://www.google.com/search?q=calculator",
            "online calculator"
        )

    elif "open qr generator" in command:
        open_website(
            "https://www.qr-code-generator.com",
            "QR Code Generator"
        )

    elif "open remove background" in command:
        open_website(
            "https://www.remove.bg",
            "Remove Background"
        )

    elif "open pdf" in command:
        open_website(
            "https://www.adobe.com/acrobat/online.html",
            "Adobe PDF tools"
        )

    elif "open drive" in command:
        open_website(
            "https://drive.google.com",
            "Google Drive"
        )

    elif "open gmail" in command:
        open_website(
            "https://mail.google.com",
            "Gmail"
        )

    elif "minimize window" in command:
        pyautogui.hotkey("alt", "space")
        pyautogui.press("n")
        speak("Window minimized.")

    elif "close window" in command:
        pyautogui.hotkey("alt", "f4")
        speak("Window closed.")

    elif "switch window" in command:
        pyautogui.hotkey("alt", "tab")
        speak("Switching window.")

    elif "show desktop" in command:
        pyautogui.hotkey("win", "d")
        speak("Showing desktop.")

    elif "lock computer" in command:
        pyautogui.hotkey("win", "l")
        speak("Locking the computer.")

    elif "open start menu" in command:
        pyautogui.press("win")
        speak("Opening Start menu.")

    elif "copy" in command:
        pyautogui.hotkey("ctrl", "c")
        speak("Copied.")

    elif "paste" in command:
        pyautogui.hotkey("ctrl", "v")
        speak("Pasted.")

    elif "select all" in command:
        pyautogui.hotkey("ctrl", "a")
        speak("Selected all.")

    elif "undo" in command:
        pyautogui.hotkey("ctrl", "z")
        speak("Undo.")

    elif "redo" in command:
        pyautogui.hotkey("ctrl", "y")
        speak("Redo.")

    elif "save" in command:
        pyautogui.hotkey("ctrl", "s")
        speak("Saved.")

    elif "print" in command:
        pyautogui.hotkey("ctrl", "p")
        speak("Opening print.")

    elif "refresh" in command:
        pyautogui.press("f5")
        speak("Refreshing.")

    elif "go back" in command:
        pyautogui.hotkey("alt", "left")
        speak("Going back.")

    elif "go forward" in command:
        pyautogui.hotkey("alt", "right")
        speak("Going forward.")

    elif "new tab" in command:
        pyautogui.hotkey("ctrl", "t")
        speak("New tab opened.")

    elif "close tab" in command:
        pyautogui.hotkey("ctrl", "w")
        speak("Tab closed.")

    elif "next tab" in command:
        pyautogui.hotkey("ctrl", "tab")
        speak("Next tab.")

    elif "previous tab" in command:
        pyautogui.hotkey("ctrl", "shift", "tab")
        speak("Previous tab.")

    elif "zoom in" in command:
        pyautogui.hotkey("ctrl", "+")
        speak("Zooming in.")

    elif "zoom out" in command:
        pyautogui.hotkey("ctrl", "-")
        speak("Zooming out.")

    elif "reset zoom" in command:
        pyautogui.hotkey("ctrl", "0")
        speak("Zoom reset.")

    elif "shutdown" in command:
        speak("Shutdown is disabled for safety.")

    elif "restart" in command:
        speak("Restart is disabled for safety.")

    elif (
        command == "exit"
        or command == "quit"
        or command == "stop"
        or "exit assistant" in command
        or "close assistant" in command
    ):
        speak("Goodbye!")
        return False

    else:
        speak("I do not know that command yet.")

    return True


def main():
    speak("Voice Control Assistant started.")
    speak("Say a command, or say exit to close.")

    running = True

    while running:
        command = listen()
        running = handle_command(command)


if __name__ == "__main__":
    main()