import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    print(f"[Jarvis says] {text}")   
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:   
            print("[System] Adjusting for background noise...")
            listener.adjust_for_ambient_noise(origin)   
            print("[System] Listening...")
            speech = listener.listen(origin)

            print("[System] Processing speech...")

            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print(f"[User said] {instruction}")   

            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', " ")
                print(f"[Command extracted] {instruction}")
    except Exception as e:
        print(f"[Error] {e}")   
        instruction = ""
    return instruction

def play_Jarvis():
    instruction = input_instruction()
    if not instruction:
        talk("I didn't catch that, please say again.")
        return play_Jarvis()

    if "play" in instruction:
        song = instruction.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time ' + time)

    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date " + date)

    elif 'how are you' in instruction:
        talk('I am fine, how about you')

    elif 'what is your name' in instruction:
        talk('I am Jarvis, What can I do for you?')

    elif 'who is' in instruction:
        human = instruction.replace('who is', " ")
        info = wikipedia.summary(human, 1)
        print(f"[Wikipedia] {info}")   
        talk(info)

    else:
        talk('Please repeat')
        play_Jarvis()

play_Jarvis()
