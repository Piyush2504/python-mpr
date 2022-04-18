# import pyttsx3 #pip install pyttsx3
# import speech_recognition as sr #pip install speechRecognition
# import datetime
# import wikipedia #pip install wikipedia
# import webbrowser
# import os
# import smtplib

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Good Morning!")

#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")   

#     else:
#         speak("Good Evening!")  

#     speak("I am Jarvis Sir. Please tell me how may I help you")       

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         r.energy_threshold=1043
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

# if __name__ == "__main__":
#     wishMe()
#     while True:
#     # if 1:
#         query = takeCommand().lower()

#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             print(results)
#             speak(results)

#         elif 'open youtube' in query:
#             webbrowser.open("youtube.com")

#         elif 'open google' in query:
#             webbrowser.open("google.com")

#         elif 'open stackoverflow' in query:
#             webbrowser.open("stackoverflow.com")   
#         # elif 'play music' in query:
#         #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
#         #     songs = os.listdir(music_dir)
#         #     print(songs)    
#         #     os.startfile(os.path.join(music_dir, songs[0]))

#         elif 'the time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")    
#             speak(f"Sir, the time is {strTime}")

#         # elif 'open code' in query:
#         #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#         #     os.startfile(codePath)

#         elif 'email to harry' in query:
#             try:
#                 speak("What should I say?")
#                 content = takeCommand()
#                 to = "harryyourEmail@gmail.com"    
#                 sendEmail(to, content)
#                 speak("Email has been sent!")
#             except Exception as e:
#                 print(e)
#                 speak("Sorry my friend harry bhai. I am not able to send this email")    
# from tkinter import *
# import wikipedia
# import wolframalpha

# import speech_recognition
# import pyttsx3

# root = Tk()
# root.title("Python Virtual Assistant")

# def retrive_input(event =None):
#     inputx = textBox.get("1.0" , "end-1c")
#     tex = Text()
#     try:
#         app_id='R57UY3-QHE4A3G4WK'
#         client = wolframalpha.Client(app_id)
#         res = client.query(inputx)
#         answer = next(res.results).text
#         tex.insert(END, answer)
#         tex.see(END)
#         tex.pack()
        
#     except:
#         inputx = list(inputx.strip().split(" "))
#         inputx = inputx[2:]
#         result = wikipedia.summary(''.join(inputx) , sentences = 4)
#         tex.insert(END, answer)
#         tex.see(END)
#         tex.pack()
    
# textBox =Text(root , height=2 , width=40)
# textBox.bind('<Return>' , retrive_input)
# textBox.pack()

# buttonCommit = Button(root , height = 2 , width =10 , text = "Commit",  command = lambda : retrive_input())
# buttonCommit.pack()

# mainloop()

import speech_recognition as sr    #To convert speech into text
import pyttsx3                     #To convert text into speech
import datetime                    #To get the date and time
import wikipedia                   #To get information from wikipedia
import webbrowser                  #To open websites
import os                          #To open files
import time                        #To calculate time
import subprocess                  #To open files
from tkinter import *              #For the graphics
import pyjokes                     #For some really bad jokes
from playsound import playsound    #To playsound
import keyboard                    #To get keyboard
  
# name_file = open("Cortana")
name_assistant = "Cortana"

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
    
def speak(text):
    engine.say(text)
    print(name_assistant + " : "  +  text)
    engine.runAndWait() 


def wishMe():


  hour=datetime.datetime.now().hour

  if hour >= 0 and hour < 12:

      speak("Hello,Good Morning")
 
  elif hour >= 12 and hour < 18:

      speak("Hello,Good Afternoon")

  else:

      speak("Hello,Good Evening")


def get_audio(): 

    r = sr.Recognizer() 
    audio = '' 

    with sr.Microphone() as source: 

        print("Listening") 
        # playsound("assistant_on.wav")
        audio = r.listen(source, phrase_time_limit = 3) 
        # playsound("assistant_off.wav")
        print("Stop.") 
        
    try: 
        text = r.recognize_google(audio, language ='en-US') 
        print('You: ' + ': ' + text)
        return text


    except:

        return "None"


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def date():
    now = datetime.datetime.now()
    month_name = now.month
    day_name = now.day
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st'] 

    speak("Today is "+ month_names[month_name-1] +" " + ordinalnames[day_name-1] + '.')

wishMe()


def Process_audio():

    run = 1
    if __name__=='__main__':
        while run==1:

            app_string = ["open word", "open powerpoint", "open excel" ,"open code",  "open chrome"]
            app_link = [r'\Word.lnk',r'\PowerPoint.lnk', r'\Excel.lnk', r'\Sublime Text 3.lnk',r'\Google Chrome.lnk' ]
            app_dest = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

            statement = get_audio().lower()
            results = ''
            run +=1

            if "hello" in statement or "hi" in statement:

              wishMe()               


            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('Your personal assistant ' + name_assistant +' is shutting down, Good bye')
                screen.destroy()
                break

            if 'wikipedia' in statement:
              try:


                speak('Searching Wikipedia...')
                statement = statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences = 3)
                speak("According to Wikipedia")
                wikipedia_screen(results)
              except:
                speak("Error")


            if 'joke' in statement:
              speak(pyjokes.get_joke())    
     
            if 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)


            if 'open google' in statement:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google chrome is open now")
                    time.sleep(5)


            if 'open gmail' in statement:
                    webbrowser.open_new_tab("mail.google.com")
                    speak("Google Mail open now")
                    time.sleep(5)

            if 'open netflix' in statement:
                    webbrowser.open_new_tab("netflix.com/browse") 
                    speak("Netflix open now")


            if 'open prime video' in statement:
                    webbrowser.open_new_tab("primevideo.com") 
                    speak("Amazon Prime Video open now")
                    time.sleep(5)

            if app_string[0] in statement:
                os.startfile(app_dest + app_link[0])

                speak("Microsoft office Word is opening now")

            if app_string[1] in statement:
                os.startfile(app_dest + app_link[1])
                speak("Microsoft office PowerPoint is opening now")

            if app_string[2] in statement:
                os.startfile(app_dest + app_link[2])
                speak("Microsoft office Excel is opening now")
        
            if app_string[3] in statement:

                os.startfile(app_dest + app_link[3])
                speak("Zoom is opening now")


            if app_string[4] in statement:
                os.startfile(app_dest + app_link[4])
                speak("Notepad is opening now")
        
            if app_string[5] in statement:
                os.startfile(app_dest + app_link[5])
                speak("Google chrome is opening now")
                       

            if 'news' in statement:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/mangalore")
                speak('Here are some headlines from the Times of India, Happy reading')
                time.sleep(6)

            if 'cricket' in statement:
                news = webbrowser.open_new_tab("cricbuzz.com")
                speak('This is live news from cricbuzz')
                time.sleep(6)

            if 'corona' in statement:
                news = webbrowser.open_new_tab("https://www.worldometers.info/coronavirus/")
                speak('Here are the latest covid-19 numbers')
                time.sleep(6)

            if 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            if 'date' in statement:
                date()

            if 'who are you' in statement or 'what can you do' in statement:
                    speak('I am '+name_assistant+' your personal assistant. I am programmed to minor tasks like opening youtube, google chrome, gmail and search wikipedia etcetra') 


            if "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Abhhi  Sannayya")

            
            if 'make a note' in statement:
                statement = statement.replace("make a note", "")
                note(statement)


            if 'note this' in statement:    
                statement = statement.replace("note this", "")
                note(statement)         

            speak(results)


def change_name():

  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()


def change_name_window():
    
      global settings_screen
      global name


      settings_screen = Toplevel(screen)
      settings_screen.title("Settings")
      settings_screen.geometry("300x300")
      settings_screen.iconbitmap('app_icon.ico')

      
      name = StringVar()

      current_label = Label(settings_screen, text = "Current name: "+ name_assistant)
      current_label.pack()

      enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below") 
      enter_label.pack(pady=10)   
      

      Name_label = Label(settings_screen, text = "Name")
      Name_label.pack(pady=10)
     
      name_entry = Entry(settings_screen, textvariable = name)
      name_entry.pack()


      change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
      change_name_button.pack(pady=10)


def info():

  info_screen = Toplevel(screen)
  info_screen.title("Info")
  info_screen.iconbitmap('app_icon.ico')

  creator_label = Label(info_screen,text = "Created by Abhhi Sannayya")
  creator_label.pack()

  Age_label = Label(info_screen, text= " at the age of 12")
  Age_label.pack()

  for_label = Label(info_screen, text = "For Makerspace")
  for_label.pack()

keyboard.add_hotkey("F4", Process_audio)


def wikipedia_screen(text):


  wikipedia_screen = Toplevel(screen)
  wikipedia_screen.title(text)
  wikipedia_screen.iconbitmap('app_icon.ico')

  message = Message(wikipedia_screen, text= text)
  message.pack()



def main_screen():

      global screen
      screen = Tk()
      screen.title(name_assistant)
      screen.geometry("100x250")
      screen.iconbitmap('app_icon.ico')


      name_label = Label(text = name_assistant,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
      name_label.pack()


      microphone_photo = PhotoImage(file = "assistant_logo.png")
      microphone_button = Button(image=microphone_photo, command = Process_audio)
      microphone_button.pack(pady=10)

      settings_photo = PhotoImage(file = "settings.png")
      settings_button = Button(image=settings_photo, command = change_name_window)
      settings_button.pack(pady=10)
       
      info_button = Button(text ="Info", command = info)
      info_button.pack(pady=10)

      screen.mainloop()


main_screen()