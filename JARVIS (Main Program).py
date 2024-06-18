#Jarvis Program

#Import libraries
import pyttsx3                   
import speech_recognition as sr  
import datetime 
import wikipedia 
import webbrowser 
import os
import random as r
import pyautogui as py
import time
import playsound
import turtle
import urllib.request as urlreq


#..........................................................................voice engine part
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)


#...........................................................................speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#...........................................................................wish me function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Jarvis: Good morning sir")
        speak("Good morning sir")
    elif hour >= 12 and hour <= 18:
        print("Jarvis: Good After noon sir")
        speak("Good After noon sir")
    else:
        print("Jarvis: Good evening sir")
        speak("Good evening sir")
    print("Jarvis: I am Jarvis tell me how may i help you")
    speak("I am Jarvis tell me how may i help you")


#...............................................................................password part
#name=py.password("Enter your name","NAME")
#age=py.password("Enter your age","AGE")

#...............................................................................welcoming the user
print("\t\tWelcome  sir")
speak("Welcome  sir")
print("\nJarvis is activating in")
speak("Jarvis is activating")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)



#..........................................................................take command function
def takecommand():
    #it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        print("Jarvis: Say that again please...")
        return "None"
    return query

#.............................................................................Main important jarvis program
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # logic for executing tasks based on query
        
        #.....................................................................wikipedia part
        if "wikipedia" in query:   
            print("Jarvis: Searching wikipedia...")
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print("Jarvis: According to wikipedia")
            speak("According to wikipedia")
            print("Jarvis:", results)
            speak(results)
        
        #.......................................................................opening python website
        elif "open python website" in query:
            print("Ok sir,opening PYTHON WEBSITE in Default Browser")
            speak("ok sir opening python website in Default Browser")
            weburl=urlreq.urlopen("https://www.python.org/")
            url= weburl.geturl() 
            webbrowser.open_new(url)
        
        #........................................................................opening google website
        elif "open google" in query:
            print("\t\t      888888888       88888888    88888888     888888888      88           88888888  ")
            time.sleep(0.5)
            print("\t\t     88              88      88  88      88   88              88           88        ")
            time.sleep(0.5)
            print("\t\t    88               88      88  88      88  88               88           88        ")
            time.sleep(0.5)
            print("\t\t    88               88      88  88      88  88               88           88888888  ")
            time.sleep(0.5)
            print("\t\t    88     88888888  88      88  88      88  88     88888888  88           88        ")
            time.sleep(0.5)
            print("\t\t     88          88  88      88  88      88   88          88  88           88        ")
            time.sleep(0.5)
            print("\t\t      888888888  88   88888888    88888888     888888888  88  88888888888  88888888  ")
            time.sleep(0.5)
            print("\t\t                 88                                       88                         ")
            print("Ok sir,opening GOOGLE in Default Browser")
            speak("ok sir opening google in Default Brower")
            weburl=urlreq.urlopen("https://www.google.com/")
            url= weburl.geturl() 
            webbrowser.open_new(url)
            
        
        #........................................................................opening youtube website
        elif "open youtube" in query:
            print("Ok sir,opening YOUTUBE in Default Browser")
            speak("ok sir opening youtube in Default Browser")
            weburl=urlreq.urlopen("https://www.youtube.com/")
            url= weburl.geturl() 
            webbrowser.open_new(url)
            
        
        #.......................................................................playing musics
        elif "play music" in query:
            music_dir = "G:\\NETHRANAND EDUCATION\\12TH CLASS 2020-21\\PERSONAL PROGRAMS\\PERSONAL ASSI. (JARVIS)\\MUSIC"          #....directory path
            res = "yes"
            while res == "yes":
                print("Jarvis: LIST OF SONGS TO PLAY")
                print()
                songs = os.listdir(music_dir)
                length = len(songs)
                for i in range(0, length-1):
                    f = songs[i]
                    print(i, ":", f)
                print("\nJarvis: Enter the serial number of the music that u want to listen")
                speak("Enter the serial number of the music that u want to listen")
                song_no = int(input("\nJarvis: Enter song number to play: "))
                os.startfile(os.path.join(music_dir, songs[song_no]))
                print()
                res = input("Jarvis: Do u want to listen another music(yes/no): ")
                if res == "yes":
                    continue
                else:
                    pass
            print("Jarvis: Thanks for listening the songs")
            speak("Thanks for listing the songs")
        
        #.......................................................................shows analog clock and tells time
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"Jarvis: Sir,the time is {strTime}")
            speak(f"Sir the time is {strTime}")

            wndw = turtle.Screen()
            wndw.bgcolor("black")
            wndw.setup(width=600, height=600)
            wndw.title("Analogue Clock")
            wndw.tracer(0)
            # Create the drawing pen
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.speed(0)
            pen.pensize(3)
            def draw_clock(hr, mn, sec, pen):
                # Draw clock face
                pen.up()
                pen.goto(0, 210)
                pen.setheading(180)
                pen.color("green")
                pen.pendown()
                pen.circle(210)
                # Draw hour hashes
                pen.up()
                pen.goto(0, 0)
                pen.setheading(90)
                for _ in range(12):
                    pen.fd(190)
                    pen.pendown()
                    pen.fd(20)
                    pen.penup()
                    pen.goto(0, 0)
                    pen.rt(30)
                # Draw the hands
                # Each tuple in list hands describes the color, the length
                # and the divisor for the angle
                hands = [("white", 80, 12), ("blue", 150, 60), ("red", 110, 60)]
                time_set = (hr, mn, sec)
                for hand in hands:
                    time_part = time_set[hands.index(hand)]
                    angle = (time_part/hand[2])*360
                    pen.penup()
                    pen.goto(0, 0)
                    pen.color(hand[0])
                    pen.setheading(90)
                    pen.rt(angle)
                    pen.pendown()
                    pen.fd(hand[1])
            while True:
                hr = int(time.strftime("%I"))
                mn = int(time.strftime("%M"))
                sec = int(time.strftime("%S"))
                draw_clock(hr, mn, sec, pen)
                wndw.update()
                time.sleep(1)
                pen.clear()
            wndw.mainloop()
            
            
        #........................................................................open visual studio code
        elif "open code" in query:
            print("Ok sir,opening VISUAL STUDIO CODE")
            speak("ok sir opening visual studio code")
            codepath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   #....directory path
            os.startfile(codepath)
        
        #.........................................................................opening python program list
        elif "program" in query:
            program_dir = "E:\\Geddada_Nethranand\\12TH_CLASS\\COMPUTER SCIENCE\\Jarvis folder\\Jarvis Data\\programs"       #....directory path
            res = "yes"
            while res == "yes":
                print("Jarvis: LIST OF PROGRAMS TO RUN")
                print()
                programs = os.listdir(program_dir)
                length = len(programs)
                for i in range(0, length-1):
                    f = programs[i]
                    print(i, ":", f)
                print("\nJarvis: Enter the serial number of the program that u want to run")
                speak("Enter the serial number of the program that u want to run")
                program_no = int(input("\nJarvis: Enter program number to run: "))
                os.startfile(os.path.join(program_dir, programs[program_no]))
                print()
                res = input("\tJarvis: Do u want to run another program(yes/no): ")
                if res == "yes":
                    continue
                else:
                    pass
            print("Jarvis: Thanks for running the programs")
            speak("Thanks for running the programs")
        
        #.......................................................................playing the video
        elif "play video" in query:
            video_dir = "E:\\NETHRANAND EDUCATION\\12TH CLASS 2020-21\\COMPUTER SCIENCE\\programs\\PERSONAL PROGRAMS\\PERSONAL ASSI. (JARVIS)\\VIDEO"    #...directory path
            res = "yes"
            while res == "yes":
                print("Jarvis: LIST OF VIDEOS TO PLAY")
                print()
                videos = os.listdir(video_dir)
                length = len(videos)
                for i in range(0, length-1):
                    f = videos[i]
                    print(i, ":", f)
                print("\nJarvis: Enter the serial number of the video that u want to play")
                speak("Enter the serial number of the video that u want to play")
                video_no = int(input("\nJarvis: Enter video number to play: "))
                os.startfile(os.path.join(video_dir, videos[video_no]))
                print()
                res = input("Jarvis: Do u want to play another video(yes/no): ")
                if res == "yes":
                    continue
                else:
                    pass
            print("Jarvis: Thanks for watching the videos")
            speak("Thanks for watching the videos")
        
        #........................................................................asking who made you
        elif "who made you" in query:
            print("\t\t8888      88  8888888888  8888888888  88      88  8888888888        8888       ")
            time.sleep(0.5)
            print("\t\t88 88     88  88              88      88      88  88      88       88  88      ")
            time.sleep(0.5)
            print("\t\t88  88    88  88              88      88      88  88      88      88    88     ")
            time.sleep(0.5)
            print("\t\t88   88   88  8888888888      88      8888888888  8888888888     8888888888    ")
            time.sleep(0.5)
            print("\t\t88    88  88  88              88      88      88  888888        88        88   ")
            time.sleep(0.5)
            print("\t\t88     88 88  88              88      88      88  88   88      88          88  ")
            time.sleep(0.5)
            print("\t\t88      8888  8888888888      88      88      88  88    888   88            88 ")
            time.sleep(0.5)
            print('''\nI was made by NETHRANAND
DATE : SUNDAY MAY 24 2020
TIME : 05:44:55 PM''')
            speak("i was made by natahranand ")
            speak("on Sunday May 24 2020")
            speak("time 5:44:55 PM")
            speak("I am under development")
        
        elif "how are you" in query:
            print("I am fine sir")
            speak("I am fine sir")
        
        elif "hello" in query:
            print("Hi ,nice to meet you")
            speak("hi nice to meet you")
        
        elif "tell me your name" in query:
            print("My name is J.A.R.V.I.S")  
            speak("my name is J A R V I S jarvis")
            print("Full form : Just A Rather Very Intelligent System")
            speak("full form just a rather very intelligent system")
            print("And I am your personal assistant")
            speak("and i am your personal assistant")
        
        elif "system info" in query:

            print("88                 88  88  88      88  8888       88   88                 88  8888888888 ")
            time.sleep(0.5)
            print(" 88               88   88  8888    88  88  88   88  88  88               88   88 ")
            time.sleep(0.5)
            print("  88             88    88  88 88   88  88   88  88  88   88             88    88 ")
            time.sleep(0.5)
            print("   88           88     88  88  88  88  88    88 88  88    88           88     8888888888 ")
            time.sleep(0.5)
            print("    88   888   88      88  88   88 88  88   88  88  88     88   888   88              88 ")
            time.sleep(0.5)
            print("     88 88 88 88       88  88    8888  88  88   88  88      88 88 88 88               88 ")
            time.sleep(0.5)
            print("      888   888        88  88      88  8888       88         888   888        8888888888 ")
            time.sleep(0.5)
            print()
            print("                          8888       8888    ") 
            time.sleep(0.5) 
            print("                         88 88      88 88    ")   
            time.sleep(0.5)
            print("                        88  88     88  88    ")    
            time.sleep(0.5)
            print("                            88         88    ")    
            time.sleep(0.5)
            print("                            88         88    ")    
            time.sleep(0.5)
            print("                            88         88    ")  
            print("                        888888888  888888888 ") 
            time.sleep(0.5)

            print('''\nWindow 11                    ............................................need to update???

Processor: Pentium(R) Core(TM) i3-10100 CPU @3.60GHz
Installed memory (RAM): 8.00GB (7.86 GB usable)
System Type: 64-bit Operating System,x64-based processor
Graphic card: Integrated (Intel 630) ''')
            print()
            print()
            speak("This is the system information of this pc")

        elif "open quiz" in query:
            #Quiz program made by geddada nethranand
            #started on 15 sep 2020
            #playsound.playsound('C:\\Users\\Micro\\Music\\DOWNLOAD MUSIC\\Warriyo - Mortals.mp3', False)
            print("\t\tGENRAL KNOWLEDGE QUIZ")
            print()
            print()
            print("\t\t       8888888888   88    88  88  8888888888  ")
            time.sleep(0.5)
            print("\t\t      88        88  88    88  88          88  ")
            time.sleep(0.5)
            print("\t\t      88        88  88    88  88        88    ")
            time.sleep(0.5)
            print("\t\t      88        88  88    88  88      88      ")
            time.sleep(0.5)
            print("\t\t      88   8888 88  88    88  88    88        ")
            time.sleep(0.5)
            print("\t\t       8888888888    888888   88  8888888888  ")
            time.sleep(0.5)
            print("\t\t              88                              ")
            time.sleep(0.5)
            print("\t\t               888                            ")

            speak("welcome to the genral knowledge quiz by nethranand")
            print("\nQUIZ RULE")
            speak("quiz rule")
            print("1.First you have to enter how many question quiz do you want to write.")
            print("2.Read the questions carefully the write your answer.")
            print("3.The system will check the answer thn it tells whether it is correct or wrong.")
            print("4.All answers should start using capital letter and then followed by small letters.")
            print("5.At last it will tell the correct answer after each question.")

            question = {1: "How many days do we have in a week?", 2: "How many days are there in a year?", 3: "How many colors are there in a rainbow?", 4: "Which animal is known as the ‘Ship of the Desert?’", 5: "How many letters are there in the English alphabet?", 6: "How many consonants are there in the English alphabet?", 7: "How many sides are there in a triangle?", 8: "In which direction does the sun rise?", 9: "What do you call a type of shape that has five sides?", 10: "Which month of the year has the least number of days?",
            11: "What is a baby frog called?", 12: "Where does a pig live?", 13: "We smell with our?", 14: "Which is the largest mammal?", 15: "What do you call the person who brings a letter to your home from post office?", 16: "What type of gas do plants absorb?", 17: "Which place is known as the roof of the world?",18: "Who was the first prime minister of India?", 19: "How many years are there in one Millenium?", 20: "Who was the first man to walk on the moon?",
            21:"How many primary colors are there?",22:"Which way is anti-clockwise, left or right?",23:"How many equal sides does an isosceles triangle have?",24:"How many days are there in the month of February in a leap year?",25:"What do you call a house made of ice?",26:" Which is the longest river on the earth?",27:"Which is the principal source of energy for earth?",28:"Which is the smallest continent?",29:"Which is the densest jungle in the world?",30:"Which is the coldest location in the earth?",
            31:"What is the standard taste of the water?",32:"Which is the tallest mountain in the world?",33:"Which country is called the land of rising sun?",34:"Which is the fastest animal on the land?",35:"Who is the inventor of electricity?",36:"Which continent is known as ‘Dark’ continent?",37:"Which planet is known as the Red Planet?",38:"Which is the tallest animal on the earth?",39:"Which is the most sensitive organ in our body?",40:"Which two parts of the body continue to grow for your entire life?",
            41:"The largest ‘Democracy’ in the world?",42:"Which is the largest ocean in the world?",43:"Which is the instrument used to measure Blood pressure?",44:"How many years are there in a century?",45:"Which is the largest country in the world?",46:"Caterpillars turn into butterflies.[T/F]",47:"Adults have a total of 34 teeth.[T/F]",48:"There are 30 days in May.[T/F]",49:"New York is the capital of America.[T/F]",50:"Cinderella’s carriage turns into a potato.[T/F]",
            51:"Half of 250 is 125.[T/F]",52:"An ostrich’s eye is bigger than its brain.[T/F]",53:"A jellyfish is 95% water.[T/F]",54:"Plants give us oxygen.[T/F]",55:"Bubble gum contains rubber.[T/F]",56:"8 o’clock in the evening is written as 8 am.[T/F]",57:"Bacon was part of the first meal eaten on the Moon.[T/F]",58:"Spinach originally comes from Iran.[T/F]",59:"Watermelons are originally from Australia.[T/F]",60:"Black Forest cake has the same colors as the traditional dress of the inhabitants of the Black Forest in Germany.[T/F]",}

            answer = {1: "7", 2: "365", 3: "7", 4: "Camel", 5: "26",6: "21", 7: "3", 8: "East", 9: "Pentagon", 10: "February",
            11: "Tadpole", 12: "Sty", 13: "Nose", 14: "Blue Whale", 15: "Postman", 16: "Carbon dioxide", 17: "Tibet", 18: "Pandit Jawaharlal Nehru", 19: "1000", 20: "Neil Armstrong",
            21:"3",22:"Left",23:"2",24:"29",25:"Igloo",26:"Nile",27:"Sun",28:"Australia",29:"Amazon rainforest",30:"Antarctica",
            31:"Tasteless",32:"Mount Everest",33:"Japan",34:"Cheetah",35:"Benjamin Franklin",36:"Africa",37:"Mars",38:"Giraffe",39:"Skin",40:"Nose and Ears",
            41:"India",42:"Pacific Ocean",43:"Sphygmomanometer",44:"100",45:"Russia",46:"T",47:"F",48:"F",49:"F",50:"F",
            51:"T",52:"T",53:"T",54:"T",55:"T",56:"F",57:"T",58:"T",59:"F",60:"T",}

            #number of question
            qno=int(input("\nEnter the number of questions that you want to play: "))

            print("\n\tLETS BEGIN")
            speak("lets begin")
            c=0
            for i in range(1,qno+1):
                rno=r.randint(1,60)
                print("\nQ", i,":", question[rno])
                userans=input("Your Answer: ")
                if userans==answer[rno]:
                    playsound.playsound('C:\\Users\\Micro\\Downloads\\sounds\\applause.mp3', False)
                    print("Congratulation your answer is CORRECT")
                    c=c+1
                else:
                    playsound.playsound('C:\\Users\\Micro\\Downloads\\sounds\\gameover2.mp3', False)
                    print("Oops!!,Your answer is incorrect")
                    print("The answer to this problem is: ",answer[rno])
            time.sleep(4)
            print("\nQuiz over")
            speak("quiz over")
            print("Thank you for playing this quiz")
            speak("thank you for playing this quiz")
            print("\nYOUR SCORE")
            speak("your score")
            print(c,"/",qno)
            playsound.playsound('C:\\Users\\Micro\\Downloads\\sounds\\gameover.mp3', False)
            time.sleep(5)
 
            
        #elif "tell me my name" in query:
            #print("Your name is", name)
            #speak("Your name is")
            #speak(name)

        #elif "tell me my age" in query:
            #print("You are", age, "years old")
            #speak("You are")
            #speak(age)
            #speak("years old")
            

        #........................................................................program for exiting
        elif "exit" in query:
            print('''Thank you sir
        Exiting...''')
            speak("Thank you sir")
            speak("program is terminating ...")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            print(".")
            time.sleep(0.5)
            exit()

