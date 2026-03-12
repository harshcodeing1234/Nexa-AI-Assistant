# Import Packages........
import speech_recognition as sr
import os
import webbrowser
from pyttsx import speak
from config import api_key,news_api_key
import random
import datetime
import pywhatkit
import wikipedia
import pyautogui
import psutil
import time 
import requests
import threading
from openai import OpenAI 

tasks = []

### 
client = OpenAI(
    api_key=api_key,
    base_url="https://api.sambanova.ai/v1"
)

chat_history = [
    {
        "role": "system",
        "content": "You are Nexa, a professional AI assistant. Always reply in plain text. Do NOT use emojis. Do NOT use symbols. Keep responses clean, short and formal.always response in english"
    }
]

def chat(query):
    global chat_history
    try:
        time.sleep(2)
        chat_history.append({"role": "user", "content": query})

        response = client.chat.completions.create(
            model="DeepSeek-V3.1",
            messages=chat_history,
            max_tokens=100,
            temperature=0.7
        )

        reply = response.choices[0].message.content

        chat_history.append({"role": "assistant", "content": reply})

        print(f"Nexa Say : {reply}")
        say(reply)
        return reply 

    except Exception as e:
        say("Some error occured. sorry from nexa")
        print(e)
        return "AI connection error."

def ai(prompt):
    try:
        response = client.chat.completions.create(
            model="DeepSeek-V3.1",
            messages=[
                {"role": "system", "content": "You are Nexa AI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        text = response.choices[0].message.content

    except Exception as e:
        print("Error:", e)
        return

    if not os.path.exists("SambaNova"):
        os.mkdir("SambaNova")

    filename = f"SambaNova/{prompt[:20]}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    say("Response saved successfully.")

### 
def say(text):
    speak(f'{text}')   

###
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"{query}")
            return query
        except:
            return "Some error occured. sorry from nexa."
        
###
def play_on_youtube(song_name):
    say(f"Playing {song_name}")
    pywhatkit.playonyt(song_name)
###
apps = {
    "notepad": "notepad",
    "calculator": "calc",
    "chrome": "chrome",
    "vs code": "code",
    "cmd": "cmd",
    "powershell": "powershell",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
    "outlook": "outlook",
    "camera": "camera"

}

def open_app(app_name):
    if app_name in apps:
        os.system(f'start "" "{apps[app_name]}"')
        say(f"Opening {app_name}")
        return True
    return False

###
def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
        response = requests.get(url, timeout=5)
        articles = response.json()['articles'][:5]
        say("Here are top news headlines")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            say(article['title'])
    except:
        say("Unable to fetch news")
###
def set_timer(seconds):
    say(f"Timer set for {seconds} seconds")
    def timer():
        time.sleep(seconds)
        say("Timer finished")
    threading.Thread(target=timer, daemon=True).start()
###
def clean_system():
    try:
        temp_folder = os.environ.get('TEMP')
        files_removed = 0
        for file in os.listdir(temp_folder):
            try:
                file_path = os.path.join(temp_folder, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    files_removed += 1
            except:
                pass
        say(f"Cleaned {files_removed} temporary files")
    except:
        say("Cleanup failed")
###
def manage_tasks(action, task=""):
    global tasks
    if "add" in action:
        tasks.append(task)
        say(f"Task added: {task}")
    elif "remove" in action:
        if task in tasks:
            tasks.remove(task)
            say(f"Task removed: {task}")
    elif "list" in action or "show" in action:
        if tasks:
            say(f"You have {len(tasks)} tasks")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
                say(t)
        else:
            say("No tasks")
###
def tell_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        joke_data = response.json()
        setup = joke_data['setup']
        punchline = joke_data['punchline']
        say(setup)
        time.sleep(2)
        say(punchline)
    except:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache!",
            "What do you call a programmer from Finland? Nerdic!"
        ]
        say(random.choice(jokes))
#######
def system_control(query):
        if "timer" in query.lower():
            say("How many seconds?")
            secs = takeCommand()
            try:
                set_timer(int(secs))
            except:
                say("Invalid timer")
        elif "Time".lower() in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f'Time is {hour}:{minute}')
        
        elif "battery" in query.lower():
            battery = psutil.sensors_battery()
            say(f"Battery is {battery.percent} percent")

        elif "cpu" in query.lower():
            say(f"CPU usage is {psutil.cpu_percent()} percent")

        elif "ram" in query.lower():
            say(f"RAM usage is {psutil.virtual_memory().percent} percent")

        elif "screenshot" in query.lower():
            img = pyautogui.screenshot()
            img.save("screenshot.png")
            say("Screenshot saved")

        elif "shutdown" in query.lower():
                os.system("shutdown /s /t 5")
                say('System shutdown')

        elif "restart" in query.lower():
                os.system("shutdown /r /t 5")
                say('system restared')

        ### Search app and website...
        elif "open" in query.lower():
            item = query.lower().replace("open", "").strip()

            # Try app
            if open_app(item):
                pass

            else:
                try:
                    # Try direct website
                    webbrowser.open(f"https://www.{item}.com")
                    say(f"Opening {item}")
                except:
                    # Final fallback Google search
                    pywhatkit.search(item)
                    say(f"Searching {item} on Google")

        elif "using ai".lower() in query.lower():
            ai(prompt=query)
            
        elif "reset chat".lower() in query.lower():
            global chat_history
            chat_history = [{"role": "system", "content": "You are Nexa, a helpful AI assistant."}]
            say("Chat reset successfully")

        elif "play" in query.lower():
            song = query.lower().replace("play", "").strip()
            play_on_youtube(song)

        
        elif "chat history" in query.lower():
            say("Showing chat history")

            for message in chat_history:
                role = message["role"]
                content = message["content"]

                print(f"{role.upper()} : {content}")   
        
        elif "wikipedia" in query.lower():
            person = query.lower().replace("wikipedia", "")
            result = wikipedia.summary(person, sentences=2)
            print(result)
            say(result)
        
        elif "news" in query.lower():
            get_news()
        
        elif "clean system" in query.lower():
            clean_system()
        
        elif "add task" in query.lower():
            task = query.lower().replace("add task", "").strip()
            manage_tasks("add", task)
        
        elif "remove task" in query.lower():
            task = query.lower().replace("remove task", "").strip()
            manage_tasks("remove", task)
        
        elif "show task" in query.lower() or "list tasks" in query.lower():
            manage_tasks("list")
        
        elif "joke" in query.lower():
            tell_joke()

        else:
            print("Chatting...")
            chat(query)


# Call function...
if __name__ == '__main__':
    print('-----------------------------------------------------------------------------------')
    print('Welcome to Nexa')
    say("Nexa Activated")

    while True:

        print("Listening...")
        query = takeCommand()

        if query == "Some error occured. sorry from nexa.":
            continue

        if query:
            system_control(query)

        time.sleep(1)

        
