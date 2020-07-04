import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import json
import requests
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voice',voice[1].id)


# Function For speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# Function for taking voice command and converting it in text 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Anshul is Listening Please Speak Your Command")
        speak("Please Speak")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("I am Working On Your Voice. Please Wait Recognizing\n")
            speak("Anshul is Working On Your Voice. Please Wait Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"You Said : {query}\n")

        except Exception as e:
            print("Sorry, Iam Unable to Understand PLease Said that again..")
            speak("Sorry, Iam Unable to Understand PLease Said that again..")
            return "None"
    return query  
# Function for taking voice command for game 
def gamecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Loading your Input")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            speak("Loading your Input")
            query = r.recognize_google(audio, language="en-in")
            print(f"You Said : {query}\n")

        except Exception as e:
            print("Sorry, please enter vaild Option.")
            speak("Sorry, please enter vaild Option.")
            return "None"
    return query  
# Function for sending mail 
def sendmail(mailid, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anshul.aibot@gmail.com','1@Aadarsh')
    server.sendmail('anshul.aibot@gmail.com', emailid, content)
    server.close()
# Function for wish 
def wishme():
    hour = int(datetime.datetime.now().hour)
    # we will get hours in 24 Format
    str = datetime.datetime.now().strftime("%H:%M:%S")
    if hour >=0 and hour<12:
        print("Good Morning")
        print(str)
        speak(f"its {str}")
        speak("Good Morning")
    
    elif hour >= 12 and hour<18:
        print(str)
        speak(f"its {str}")
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print(str)
        speak(f"its {str}")
        speak("Good Evening")
        print("Good Evening")
        
    print("I am Anshul : The AI BOT \n I am in my Learning Phase. \n Lets Get Started the AI Journey.\n @ Anshul:THE.AI.BOT-2020 \n\n")
    speak("I am Anshul: The AI Soft Bot. Hope we will have a Greattime Together. I am in my learning Phase please forgive me if I make any Mistake. lets get Started, the AI journey with me")
# Function for the stone paper scissor game 
def gamesps():
    # import random
    list1 = ["Stone", "Paper", "Scissor"]
    print("Speak Your Name : \n")
    speak("Speak Your Name")
    name = gamecommand()
    print("Wlcome to our Game Stone Paper Scissor\n")
    speak("Wlcome to our Game Stone Paper Scissor")
    print(f"Hey! {name} now its Your turn to give some Mannual Inputs.\n")
    speak(f"Hey! {name} now its Your turn to give some Mannual Inputs.")
    try:
        play = int(input("How Many Times you want to play: "))
    except Exception as e:
        print("I said please Enter Vaild Input, But you Corrupted the Game")
        speak("I said please Enter Vaild Input, But you Corrupted the Game")
        return 3
    count = 1
    userwon = 0
    compwon = 0
    while (play >= count):
        comp = random.choice(list1)
        print("Starting Game", count)
        speak(f"Starting Game {count} \n")
        speak("Enter vaild Input")
        try:
            userin = int(input("Enter 0 For Stone 1 For Paper 2 For Scissor: "))
        except Exception as e:
            print("I said please Enter Vaild Input, But you Corrupted the Game")
            speak("I said please Enter Vaild Input, But you Corrupted the Game")
        print("\n")
        user = list1[userin]
        if comp == "Stone" and user == "Stone":
            print("Match is Drawn")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak("oh Shit! Match is Drawn")
        elif comp == "Paper" and user == "Paper":
            print("Match is Drawn")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak("oh Shit! Match is Drawn")
        elif comp == "Scissor" and user == "Scissor":
            print("Match is Drawn")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak("oh Shit! Match is Drawn")
        elif comp == "Stone" and user == "Paper":
            print("Congo You Won")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak(f"Lucky You! Congratulation! {name} You Won")
            userwon = userwon + 1
        elif comp == "Stone" and user == "Scissor":
            print("Anshul Won")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak("Happy me! I Won, Anshul Bravo")
            compwon = compwon + 1
        elif comp == "Paper" and user == "Stone":
            print("Anshul Won")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak("Happy me! I Won, Anshul Bravo")
            compwon = compwon + 1
        elif comp == "Paper" and user == "Scissor":
            print("Congo You Won")
            print("You Enter", user)
            print("Computer Entered", comp)
            speak(f"Lucky you! Congratulation! {name} You Won")
            userwon = userwon + 1
        elif comp == "Scissor" and user == "Stone":
            print("Congo you Won")
            print("You Enter", user)
            print("Amshul Entered", comp)
            speak(f"Lucky you! Congratulation! {name} You Won")
            userwon = userwon + 1
        elif comp == "Scissor" and user == "Paper":
            print("Anshul Won")
            print("You Enter", user)
            print("Anshul Entered", comp)
            speak("Happy me! I Won, Anshul Bravo")
            compwon = compwon + 1
        else:
            print("Please Enter Valid Terms")

        print(f"---------------Game ={count} is Ended-------------------")
        print("\n")
        count = count + 1

    if compwon > userwon:
        print("Anshul Won the Series by", compwon, "And", userwon, name, "!! Hard luck")
        speak(f"Finally I Won the Series by {compwon} And {userwon} {name} !! Hard luck")
    elif userwon > compwon:
        print(f"Congratulation! {name} You have won the Series by", userwon, "And", compwon)
        speak(f"Bro! Congratulation! {name} You have won the Series by {userwon} And {compwon}")
    else:
        print(f"Play Again Series is Drawn {name}")
        speak(f"Play Again Series is Drawn {name}")


if __name__ == "__main__":
    wishme()
    qc = 0
    while True:
        query = takecommand().lower()

# Logics that Anshul is Going to Perform
        if 'wikipedia' in query:
            print('Anshul is Searching On Wikipedia For You\n')
            speak('Anshul is Searching On Wikipedia For You')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences=2)
            print("According to wikipedia :")
            speak("According to wikipedia :")
            print(results)
            speak(results)

        elif 'start youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'start next level' in query:
            webbrowser.open("thenextlevel.epizy.com")

        elif 'start instagram' in query:
            webbrowser.open("instagram.com")

        elif 'start facebook' in query:
            webbrowser.open("Facebook.com")

        elif 'start google' in query:
            webbrowser.open("Google.com", new=1)

        elif 'medical store' in query:
            webbrowser.open("www.netmeds.com")

        elif 'doctor concern' in query:
            webbrowser.open("www.healthlines.com")

        elif 'indira gandhi engineering college' in query:
            webbrowser.open("www.igecsagar.co.in")

        elif 'start music' in query:
            music_dir =  'F:\\audio'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))

        elif 'the time' in query:
            str = datetime.datetime.now().strftime("%H:%M:%S")
            print(str)
            speak(f"Okay, the time is {str}")

        elif 'start vs code' in query:
            programpath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(programpath)

        elif 'send mail to' in query:
            try:
                # print("Please, Speak Mail Id")
                # speak("Please, Speak Mail Id")
                emailid = 'devanshneekhra2001@gmail.com'
                print("PLease, Speak mail content")
                speak("PLease, Speak mail content")
                content = takecommand()
                sendmail(emailid, content)
                speak("Email has been Send. Thankyou for Using Anshul.")
            except Exception as e:
                print(e)
                print("Sorry, Iam unable to send this email. Please try again")
                speak("Sorry, Iam unable to send this email. Please try again")

        elif 'play stone paper scissor' in query:
            gamesps()
            
            while True:
                speak("Press key 1 to Restart the GAme")
                try:
                    if int(input("Want to play Again Press 1 To Start the Game or Press any number to Exit: ")) == 1:
                        gamesps()
                    else:
                        print("Thankyou For Playing With Anshul. Hope You Enjoyed")
                        speak("Thankyou For Playing With Anshul. Hope You Enjoyed")
                        break
                except Exception as e:
                    print("I said many times please Enter Vaild Input, Now Restart")
                    speak("I said many times please Enter Vaild Input, Now Restart")

        elif 'say thank you' in query:
            speak("Thankyou so much . I am Crying, uumm umm uuuummmm ummm ummm mmmm")

        elif 'please stop' in query:
            print("Thankyou For Using Anshul The AI Bot. Hope You Enjoyed, Follow me through Diffrent Social Platforms")
            speak("Thankyou For Using Anshul The AI Bot. Hope You Enjoyed, Follow me through Diffrent Social Platforms")
            break

        elif 'read news' in query:
            speak("News for today.. Lets begin")
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=9accc5c35b5e4d3b9680ac1c818398cc"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            count = 1
            for article in arts:
                print(f"{count}. {article['title']}\n")
                speak(article['title'])
                speak("Moving on to the next news.")
                count = count+1
                if count == 3:
                    break
            speak("Thanks for listening...")

        elif 'name meaning' in query:
             print("According to Google:")
             speak("According to Google:")
             print("Anshul Meaning: Radiant; Radiant, bright or intelligent, person; Sunbeam\n")
             speak("Anshul Meaning: Radiant; Radiant, bright or intelligent, person; Sunbeam")
             print("According to Urban Dictionary:")
             speak("According to Urban Dictionary:")
             print("It performed in wonders as it was anshuled, just like the flying colours of the rainbow.\n")
             speak("It performed in wonders as it was anshuled, just like the flying colours of the rainbow.")
             print("From Other Interner Source:")
             speak("From Other Interner Source")
             print("Variation in intensity of light, from 0 to max level, like Zig-Zag Pattern\n")
             speak("Variation in intensity of light, from 0 to max level, like Zig-Zag Pattern")

        elif 'open notepad' in query:
            programpath = "%ProgramFiles%\\Windows NT\\Accessories\\wordpad.exe"
            os.startfile(programpath)




        elif 'suffering from stomach pain' in query:
            print(f" Solution: \n1.Soak in a warm Water \n 2. Reduce Intake of Coffee, tea and alcohol.")
            speak(f" Solution: \n1.Soak in a warm Water \n 2. Reduce Intake of Coffee, tea and alcohol.")

        elif 'suffering from malaria' in query:
            print(f"Sir, the Symptoms of marlaria :\n 1. Fever \n 2. Chills \n 3. Headache 4. Sweats  \n Solution : \n 1. Combination of atovaquone and proguanil \n 2. Mefloquine \n 3. Primaquine phosphate. \n Thankyou MediDoc")
            speak(f"Sir, the Symptoms of marlaria :\n 1. Fever \n 2. Chills \n 3. Headache 4. Sweats  \n Solution : \n 1. Combination of atovaquone and proguanil \n 2. Mefloquine \n 3. Primaquine phosphate. \n Thankyou MediDoc")


        qc = qc + 1
        print(f"\n--------Query {qc} is Ended--------\n")