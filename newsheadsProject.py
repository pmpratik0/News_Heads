# importing the module
import json
import requests
import tkinter
from tkinter import *
import tkinter.font as tkFont
from PIL import Image,ImageTk    # pip install pillow
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import webbrowser


# Binding events must be passed event
def show_hand_cursor(event):
    if fl == 2:
        txt2.config(cursor='hand2')
    elif fl == 1:
        txt1.config(cursor='hand2')


def show_xterm_cursor(event):
    if fl == 2:
        txt2.config(cursor='xterm')
    elif fl == 1:
        txt1.config(cursor='xterm')


def click(event):
    webbrowser.open(lin[0])


def click2(event):
    webbrowser.open(lin[1])


def click3(event):
    webbrowser.open(lin[2])

def click4(event):
    webbrowser.open(lin[3])

def click5(event):
    webbrowser.open(lin[4])

def click6(event):
    webbrowser.open(lin[5])

def click7(event):
    webbrowser.open(lin[6])

def click8(event):
    webbrowser.open(lin[7])

def click9(event):
    webbrowser.open(lin[8])

def click10(event):
    webbrowser.open(lin[9])


def fast():
    engine.setProperty('rate', 200)


def medium():
    engine.setProperty('rate', 150)


def slow():
    engine.setProperty('rate', 120)


def voice():
    global v
    if v.get() == "1":
        engine.setProperty('voice', voices[0].id)
        #print(voices[0].id)
    elif v.get() == "2":
        engine.setProperty('voice', voices[1].id)
        #print(voices[1].id)


# This function is used to convert text into speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    audio1 = ""
    return audio1

#   === ------*******------ -------******-------- ------*******---------- ---------******--------- ---------*******----------- --------*******-------

# This function will recognize the audio command
def takeCommand():
    r = sr.Reclinognizer()
    with sr.Microphone() as source:
        txt1.insert(END, "Listening...\n")
        txt1.update_idletasks()
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        txt1.insert(END, "Recognizing...\n")
        txt1.update_idletasks()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        txt1.insert(END, f"User said: {query}\n")
        print(f"User said: {query}")

    except Exception as e:
        txt1.tag_config('start', foreground='red')
        txt1.insert(END, "Voice is not properly recognized...\n", 'start')
        txt1.update_idletasks()
        print("Voice is not properly recognized...")
        speak("Voice is not recognized")
        return "None"
    return query

        # This function is used to get all the covid info from the respective api

# This function is used to get all the covid info from the respective api
def covid(choice):
    global txt
    while True:
        if fl == 0:
            txt.delete(1.0, END)
            # txt.update_idletasks()
        # elif fl == 1:
        #     txt1.delete(1.0, END)
        #     txt1.update_idletasks()
        # This block is for state
        if "state" in choice or choice == "State":
            url2 = "https://api.covid19india.org/data.json"
            covid = requests.get(url2).text
            covid_dict = json.loads(covid)
            state_dict = covid_dict["statewise"]
            l = len(state_dict)
            flag = 0
            if choice == "State":
                state = covalue.get().title()
                if "And" in state:
                    donotCap = ["and", "AND", "And"]
                    parts = state.split()
                    state = ' '.join(v.lower() if v in donotCap else v.title() for v in parts)
            donotCap = ["and"]
            parts = choice.split()
            choice = " ".join(v if v in donotCap else v.title() for v in parts)
            for i in range(1, l):
                Maha_dict = state_dict[i]
                if Maha_dict["state"] in choice and choice != "State":
                    state = Maha_dict["state"]
                elif i == l - 1 and Maha_dict["state"] not in choice and choice != "State":
                    txt1.tag_config('start', foreground='red')
                    txt1.insert(END, "\nState not recognized", 'start')
                    txt1.update_idletasks()
                    print("State not recognized")
                    speak("State not recognized")
                    break
                elif choice != "State":
                    continue
                if Maha_dict["state"] == state:
                    flag = 1
                    if fl == 0:
                        txt.insert(END, f"\nIn {state}"
                                        f"\nActive Cases : {Maha_dict['active']}"
                                        f"\nRecovered Cases : {Maha_dict['recovered']}"
                                        f"\nDeaths : {Maha_dict['deaths']}\n")
                        txt.update_idletasks()
                    if fl == 1:
                        txt1.insert(END, f"\nIn {state}"
                                         f"\nActive Cases : {Maha_dict['active']}"
                                         f"\nRecovered Cases : {Maha_dict['recovered']}"
                                         f"\nDeaths : {Maha_dict['deaths']}\n")
                        txt1.update_idletasks()
                    # print(f"In {state}")
                    # print(f"Active Cases : {Maha_dict['active']}")
                    # print(f"Recovered Cases : {Maha_dict['recovered']}")
                    # print(f"Deaths : {Maha_dict['deaths']}")
                    speak(f"In {Maha_dict['state']} - Active Cases : {Maha_dict['active']} "
                        f"- Recovered Cases : {Maha_dict['recovered']}"
                        f" - Deaths : {Maha_dict['deaths']}")
                    break
            if flag == 0 and choice == "State":
                txt.tag_config('start', foreground='red')
                txt.insert(END, "Please check State properly", 'start')
                print("PLease check State properly")
                break
            else:
                break
        # This block is for district
        elif "city" in choice or choice == "City":
            url1 = "https://api.covid19india.org/state_district_wise.json"
            covid = requests.get(url1).text
            covid_dict = json.loads(covid)
            # Maha_dict = covid_dict["Maharashtra"]
            # Dist_dict = Maha_dict["districtData"]
            if choice == "City":
                state1 = covalue.get().title()
                if "And" in state1:
                    donotCap = ["And"]
                    parts = state1.split()
                    state1 = ' '.join(v.lower() if v in donotCap else v.title() for v in parts)
                if state1 in covid_dict.keys():
                    Maha_dict = covid_dict[state1]
                else:
                    txt.tag_config('start', foreground='red')
                    txt.insert(END, "\nEnter a valid State", 'start')
                    print("Enter a valid State")
                    break
                Dist_dict = Maha_dict["districtData"]
                dist = covalue2.get().title()
                flag = 1
            elif choice != "2":
                states = covid_dict.keys()
                donotCap = ["and"]
                parts = choice.split()
                choice = " ".join(v if v in donotCap else v.title() for v in parts)
                for state in states:
                    if state in choice:
                        Maha_dict = covid_dict[state]
                        Dist_dict = Maha_dict["districtData"]
                        flag = 1
                        break
                        # search from first to last but not getting any city so it takes the last city in the form of list
                    elif state == list(covid_dict.keys())[-1] and state not in choice:
                        txt1.tag_config('start', foreground='red')
                        txt1.insert(END, "\nSpecify state properly", 'start')
                        print("Specify state properly")
                        flag = 0
                        break
                if flag == 1:
                    cities = Dist_dict.keys()
                    for city in cities:
                        if city in choice:
                            dist = city
                            break
                        elif city == list(Dist_dict.keys())[-1] and city not in choice:
                            txt1.tag_config('start', foreground='red')
                            txt1.insert(END, "\nCity not recognized", 'start')
                            #print("City not recognized")
                            speak("City not recognized")
                            dist = ""
                            break
            if flag == 1 and dist in Dist_dict:
                city = Dist_dict[dist]
                if fl == 0:
                    txt.insert(END, f"\nIn {dist}\n"
                                    f"Active Cases : {city['active']}\n"
                                    f"Recovered Cases : {city['recovered']}\n"
                                    f"Deaths : {city['deceased']}\n")
                    txt.update_idletasks()
                elif fl == 1:
                    txt1.insert(END, f"\nIn {dist}\n"
                                     f"Active Cases : {city['active']}\n"
                                     f"Recovered Cases : {city['recovered']}\n"
                                     f"Deaths : {city['deceased']}\n")
                    txt1.update_idletasks()
                # print(f"In {dist}")
                # print(f'Active Cases : {city["active"]}')
                # print(f"Recovered Cases : {city['recovered']}")
                # print(f"Deaths : {city['deceased']}")
                speak(f"In {dist} - Active Cases : {city['active']} - "
                      f"Recovered Cases : {city['recovered']}"
                      f" - Deaths : {city['deceased']}")
                break
            elif choice == "City":
                txt.insert(END, f"{list(Dist_dict.keys())}\n")
                txt.tag_config('start', foreground='red')
                txt.insert(END, "\nCheck Spelling of City or Give a valid City name from above", 'start')
                print(list(Dist_dict.keys()))
                print("Check Spelling or Give a valid City name from above")
                break
            else:
                break
        elif choice == "3":
            break
        else:
            txt1.tag_config('start', foreground='red')
            txt1.insert(END, "\nTry saying State or City at the end", 'start')
            print("Try saying State or City at the end")
            break


def category(no_of_headline, head, cat, verb):
    if fl == 2:
        txt2.insert(END, f"Today's top {no_of_headline} {head} related to {cat} {verb}...\n")
        txt2.update_idletasks()
    elif fl == 1:
        txt1.insert(END, f"Today's top {no_of_headline} {head} related to {cat} {verb}...\n")
        txt1.update_idletasks()

    print(f"Today's top {no_of_headline} {head} related to {cat} {verb}...")
    speak(f"Today's top {no_of_headline} {head} related to {cat} {verb}...")

    # This is the main function

def main2():
    # com = int(input("Press 1 for text command\nPress 2 for Audio command"))
    global warlabel,arts, no_of_headline, p, lin,fl
    while True:
        if fl == 2:
            txt2.delete(1.0, END)
        elif fl == 1:
            txt1.delete(1.0, END)
        if flags == 0:
            cat = uservalue.get().title()
        elif flags == 1:
            cat = selectvalue.get().title()
        else:
            # TakeCommand() function is used recognize the voice command
            cat = takeCommand().lower()
            # t is a dictionary which helps to convert number in word to actual number
            t = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
                 "nine": "9", "ten": "10"}
            # This for loop is used to convert number word to actual word
            l = len(t)
            i = 0

            # This for loop is used to convert number word to actual word
            for key, item in t.items():
                i += 1
                if str(key) not in cat and str(item) not in cat and i == l:
                    no_of_headline = -1
                    break
                elif str(key) in cat:
                    no_of_headline = int(item)
                    break
                elif str(item) in cat:
                    no_of_headline = int(item)
                    break
        # From below this, all the code ran by user's respective input
        if "covid" in cat or "corona" in cat or cat == "State" or cat == "City":
            choice = cat
            covid(choice)
            break
        elif "general" in cat or cat == "General":
            cat = "general"
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=cbf962b15f0342db8dc1f296d53c6c5d"
        elif "business" in cat or cat == "Business":
            cat = "business"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        elif "entertainment" in cat or cat == "Entertainment":
            cat = "entertainment"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        elif "health" in cat or cat == "Health":
            cat = "health"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        elif "sports" in cat or cat == "Sports":
            cat = "sports"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        elif "technology" in cat or cat == "Technology":
            cat = "technology"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        elif "science" in cat or cat == "Science":
            cat = "science"
            url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey" \
                  "=cbf962b15f0342db8dc1f296d53c6c5d "
        else:
            txt1.tag_config('start', foreground='red')
            txt1.insert(END, "\nTry saying again", 'start')
            print("Try again")
            break
        # This block will get the url from site in jason format
        news = requests.get(url).text
        # This line will convert or parse jason script to python understandable code
        news_dict = json.loads(news)
        # This line is used to retrive only the headlines
        arts = news_dict['articles']
        last = len(arts)
        if flags == 0:
            no_of_headline = headvalue.get()
        if no_of_headline == 1:
            verb = 'is'
            head = 'headline'
        elif no_of_headline == 0:
            txt2.tag_config('start', foreground='red')
            txt2.insert(END, "\nNumber of headlines should be more than zero", 'start')
            # print("Number of headlines should be more than zero")
            speak("Number of headlines should be more than zero")
            break
        elif no_of_headline > 20:
            txt2.tag_config('start', foreground='red')
            txt2.insert(END, "\nNumber of headlines should be less than 20", 'start')
            speak("Number of headlines should be less than 20")

            # print("Number of headlines should be more than zero")
            break
        elif no_of_headline == -1:
            txt1.tag_config('start', foreground='red')
            txt1.insert(END, "\nNumber of headline is not recognized", 'start')
            speak("Number of headline is not recognized")
            break
        else:
            verb = 'are'
            head = 'headlines'
        if "general" in cat or cat == "General":
            if fl == 2:
                txt2.insert(END, f"Today's top {no_of_headline} {head} {verb}...\n")
                txt2.update_idletasks()
            elif fl == 1:
                txt1.insert(END, f"Today's top {no_of_headline} {head} {verb}...\n")
                txt1.update_idletasks()
            # print(f"Today's top {no_of_headline} {head} {verb}...")
            speak(f"Today's top {no_of_headline} {head} {verb}...")
        elif "business" in cat or cat == "Business":
            category(no_of_headline, head, cat, verb)
        elif "entertainment" in cat or cat == "Entertainment":
            category(no_of_headline, head, cat, verb)
        elif "health" in cat or cat == "Health":
            category(no_of_headline, head, cat, verb)
        elif "sports" in cat or cat == "Sports":
            category(no_of_headline, head, cat, verb)
        elif "technology" in cat or cat == "Technology":
            category(no_of_headline, head, cat, verb)
        elif "science" in cat or cat == "Science":
            category(no_of_headline, head, cat, verb)
        s = 0
        # This for loop will display and read out to headlines
        lin = []
        for index, article in enumerate(arts):
            if index <= int(no_of_headline) - 1:
                s += 1
                if fl == 2:
                    txt2.insert(END, f"\n{s} {article['title']}\n")
                    txt2.tag_config(f"link{s}", foreground='blue', underline=True)
                    txt2.insert(END, article['url'] + "\n", f"link{s}")
                    p = article['url']
                    lin.append(p)
                    # Mouse pointer
                    txt2.tag_bind(f"link{s}", '<Enter>', show_hand_cursor)
                    # Mouse leaves
                    txt2.tag_bind(f"link{s}", '<Leave>', show_xterm_cursor)
                    # Left click
                    txt2.tag_bind(f"link1", '<Button-1>', click)
                    txt2.tag_bind(f"link2", '<Button-1>', click2)
                    txt2.tag_bind(f"link3", '<Button-1>', click3)
                    txt2.tag_bind(f"link4", '<Button-1>', click4)
                    txt2.tag_bind(f"link5", '<Button-1>', click5)
                    txt2.tag_bind(f"link6", '<Button-1>', click6)
                    txt2.tag_bind(f"link7", '<Button-1>', click7)
                    txt2.tag_bind(f"link8", '<Button-1>', click8)
                    txt2.tag_bind(f"link9", '<Button-1>', click9)
                    txt2.tag_bind(f"link10", '<Button-1>', click10)
                    txt2.update_idletasks()
                elif fl == 1:
                    txt1.insert(END, f"\n{s} {article['title']}\n")
                    txt1.tag_config(f"link{s}", foreground='blue', underline=True)
                    txt1.insert(END, article['url'] + "\n", f"link{s}")
                    p = article['url']
                    lin.append(p)
                    # Mouse pointer
                    txt1.tag_bind(f"link{s}", '<Enter>', show_hand_cursor)
                    # Mouse leaves
                    txt1.tag_bind(f"link{s}", '<Leave>', show_xterm_cursor)
                    # Left click
                    txt1.tag_bind(f"link1", '<Button-1>', click)
                    txt1.tag_bind(f"link2", '<Button-1>', click2)
                    txt1.tag_bind(f"link3", '<Button-1>', click3)
                    txt1.tag_bind(f"link4", '<Button-1>', click4)
                    txt1.tag_bind(f"link5", '<Button-1>', click5)
                    txt1.tag_bind(f"link6", '<Button-1>', click6)
                    txt1.tag_bind(f"link7", '<Button-1>', click7)
                    txt1.tag_bind(f"link8", '<Button-1>', click8)
                    txt1.tag_bind(f"link9", '<Button-1>', click9)
                    txt1.tag_bind(f"link10",'<Button-1>', click10)
                    txt1.update_idletasks()
                print(s, article['title'])
                print(article['url'])
                # link = article['url']
                # print("Click this link for more info:", pyshorteners.Shortener().clckru.short(link))
                speak(article['title'])
            if index <= int(no_of_headline) - 2:
                speak("Next headline is...")
        # speak("Thanks for listening...")
        break


def audWin():
    global flags, fla ,fl ,txt1
    #  -------  this f3 in other code  ------

    hide_all_frame()
    menubar()
    frame5.place(x=450, y=150, width=800, height=600)
    flags = 2
    fla = 1
    fl = 1
    splabel = Label(frame5,text="Press \"Speak\" button and give a voice command",font=("times new roman",15,"bold"),bg="gray").place(x=100,y=50)
    b6 = Button(frame5, text="Speak",font=("times new roman",10,"bold"), command=main2,bg="#A8A8A8").place(x=200,y=100)

    txt1 = Text(frame5)
    txt1.place(x=30,y=150,width=890,height=380)

    backbtn = Button(frame5,text=" Back ",fg="black",command=main).place(x=5,y=5)

def coWin():
    global select, selectentry, selectvalue, user, covalue, userentry, flags, user2, covalue2, userentry2, fla, txt, fl
    hide_all_frame()
    menubar()
    fl = 0
    # this is f2 frame in other code
    frame4.place(x=450, y=150, width=800, height=600)
    flags = 1
    fla = 2
    select = Label(frame4, text="Select State or City",font=("times new roman", 12, "bold"), bg="gray").place(x=100, y=50)
    selectvalue = StringVar()
    selectvalue.set("State")
    selectentry = OptionMenu(frame4, selectvalue, "State", "City")
    selectentry.config(bg="#A8A8A8", fg="black", border="0")
    selectentry.place(x=400, y=50)


    user = Label(frame4, text="Enter name of the State",font=("times new roman", 12, "bold"),bg="gray").place(x=100,y=100)
    covalue = StringVar()
    userentry = Entry(frame4, textvariable=covalue,bg="#A8A8A8")
    userentry.place(x=350,y=100)
    userentry.focus_force()


    user2 = Label(frame4, text="Enter name of the City",font=("times new roman", 12, "bold"),bg="gray").place(x=100,y=150)
    covalue2 = StringVar()
    userentry2 = Entry(frame4, textvariable=covalue2,bg="#A8A8A8")
    userentry2.place(x=350,y=150)
    userentry2.focus_force()

    b5 = Button(frame4, text="Submit",font=("times new roman",10,"bold"), command=main2,bg="#A8A8A8").place(x=250,y=200)

    txt = Text(frame4)
    txt.place(x=50,y=250,width=750,height=330)

    backb = Button(frame4,text=" Back ",command=main).place(x=5,y=5)

def remove():
    lanframe.destroy()
    print("inside remove 1")
    helpframe1.destroy()
    print("inside remove 2")
    main()


# def langframe():  # ------- lanframe --------
#     # frame1.withdraw()
#     lanframe = Frame(root, bg="gray")
#     lanframe.place(x=450, y=150, width=800, height=600)
#     checkbox1 = IntVar()
#
#     langlabel = Label(lanframe, text="~~~~ Select language you want to listen ~~~~\n",
#                       font=("times new roman", 15), fg="red", bg="gray").place(x=100, y=50)
#     ckbtn = Checkbutton(lanframe, text="en", variable=checkbox1, onvalue=2, offvalue=1).place(x=200, y=80)
#     ckbtn = Checkbutton(lanframe, text="hi", variable=checkbox1, onvalue=1, offvalue=2).place(x=300, y=80)
#
#     backbtn = Button(lanframe, text=" Back ", command=lanframe.destroy).place(x=10, y=10)

def helpframe():  # --------  help frame -------
    helpframe1 = Frame(root, bg="gray")
    helpframe1.place(x=450, y=150, width=800, height=600)
    HelpLabel = Label(helpframe1, text="Here just you have to give command..",
                      font=("times new roman", 15, "bold"), bg="gray").place(x=180, y=50)
    helpLabel2 = Label(helpframe1, text=" \" Covid 19 news \" ", font=("times new roman", 15, "bold"),
                       bg="gray").place(x=250, y=90)

    backbtn = Button(helpframe1, text=" Back ", command=helpframe1.destroy).place(x=10, y=10)



def newsWin():
    global user, userentry, uservalue, head, headvalue, headentry, flags, fla, txt2, fl
    #----- this is f1 frame in other code ----
    hide_all_frame()
    menubar()
    frame3.place(x=450, y=150, width=800, height=600)
    flags = 0
    fla = 3
    fl = 2
    user = Label(frame3, text="Select category of news", font=("times new roman", 12, "bold"), bg="gray").place(x=100, y=50)
    uservalue = StringVar()
    uservalue.set("General")
    userentry = OptionMenu(frame3,uservalue, "General", "Business", "Entertainment", "Health","Sports", "Technology", "Science")
    userentry.config(bg="#A8A8A8", fg="black",border="0")
    userentry.place(x=400, y=50)

    head = Label(frame3, text="No of headlines", font=("times new roman", 12, "bold"), bg="gray").place(x=100,y=100)
    headvalue = IntVar()
    headentry = Entry(frame3, textvariable=headvalue,bg="#A8A8A8")
    headentry.place(x=400, y=100)
    # headentry.focus_force()

    b4 = Button(frame3, text="Submit",font=("times new roman",10,"bold"), command=main2,bg="#A8A8A8").place(x=250, y=150)
    backb = Button(frame3,text=" Back ",fg="black",command=main).place(x=5,y=5)

    txt2 = Text(frame3)
    txt2.place(x=30,y=200,width=890,height=380)

def voisel():
    global v, values, c1 ,i
    hide_all_frame()
    menubar()
    f4.place(x=450, y=150, width=800, height=600)
    l = Label(f4, text="Select a voice:",font=("times new roman",15,"bold"),bg="gray").place(x=100,y=50)
    # b8 = Button(f4, text="Male", command=voice1).pack(pady=10)
    # b9 = Button(f4, text="Female", command=voice2).pack(pady=10)
    values = {"Male": "1", "Female": "2"}
    i=0
    for text, value in values.items():
        c1 = Radiobutton(f4, text=text, variable=v, value=value, command=voice,bg="#A8A8A8").place(x=150+i,y=100)
        i=100
        print(v.get())
    #bclose = Button(f4, text="Home", command=main).place(x=780, y=2)
    if fla == 1:
        bback = Button(f4, text="Back", command=audWin).place(x=10, y=10)
    elif fla == 2:
        bback = Button(f4, text="Back", command=coWin).place(x=10, y=10)
    elif fla == 3:
        bback = Button(f4, text="Back", command=newsWin).place(x=10, y=10)
    else:
        bback = Button(f4, text="Back", command=main).place(x=10, y=10)


def speed():
    hide_all_frame()
    menubar()
    global f5 ,s,speeds ,sp
    f5.place(x=450, y=150, width=800, height=600)
    l = Label(f5, text="Select Speed from the below",font=("times new roman",15,"bold"),bg="gray").place(x=100,y=50)

    speeds = {"Fast": "1", "Medium": "2", "Slow": "3"}
    speedbtn1 = Radiobutton(f5,text="Fast",font=("tims new roman",10,"bold"),bg="gray",value=0,command=fast).place(x=200,y=100)
    speedbtn2 = Radiobutton(f5,text="Slow",font=("tims new roman",10,"bold"),bg="gray",value=1,command=slow).place(x=200,y=200)
    speedbtn3 = Radiobutton(f5,text="Medium",font=("tims new roman",10,"bold"),bg="gray",value=2,command=medium)
    speedbtn3.place(x=200,y=150)
    if sp == 0:
        speedbtn3.select()
        print("  sp ")
        sp = 1


    #b11 = Button(f5, text="Fast",font=("times new roman",12,"bold"), command=fast,bg="#A8A8A8").place(x=150,y=100)
    #b12 = Button(f5, text="Medium",font=("times new roman",12,"bold"), command=medium,bg="#A8A8A8").place(x=150,y=150)
    #b13 = Button(f5, text="Slow",font=("times new roman",12,"bold"), command=slow,bg="#A8A8A8").place(x=150,y=200)
    if fla == 1:
        bback = Button(f5, text="Back", command=audWin).place(x=10, y=10)
    elif fla == 2:
        bback = Button(f5, text="Back", command=coWin).place(x=10, y=10)
    elif fla == 3:
        bback = Button(f5, text="Back", command=newsWin).place(x=10, y=10)
    else:
        bback = Button(f5, text="Back", command=main).place(x=10, y=10)

    # ----------   ************  for hinding all frame and switch to home page  ******** ------------

def hide_all_frame():
    # pass
    for w in f4.winfo_children():
        w.destroy()
    for w in f5.winfo_children():
        w.destroy()
    for w in frame3.winfo_children():
        w.destroy()
    for w in frame4.winfo_children():
        w.destroy()
    for w in frame5.winfo_children():           #fabout
        w.destroy()
    for w in fabout.winfo_children():
        w.destroy()
    for w in fhow.winfo_children():
        w.destroy()
    frame3.place_forget()
    fhow.place_forget()
    fabout.place_forget()
    frame4.place_forget()
    frame5.place_forget()
    f4.place_forget()
    f5.place_forget()

# ------ - --- ****   About Frame  ****** ---- ----- ---------
def how_to_use():
    global fhow
    hide_all_frame()
    fhow.place(x=450, y=150, width=800, height=600)
    txt3 = Text(fhow,font=("",12),bg="gray",fg="white",bd=0,width=250,height=200)     #A8A8A8
    with open('HowToUse.txt') as f:
        contents = f.read()
        txt3.insert(INSERT,f'{contents}')
        txt3.configure(state='disable')
    txt3.place(x=50, y=50)
    bkbtn = Button(fhow, text=" Back ", command=main).place(x=10, y=10)

# ------ - --- ****   About Frame  ****** --- - --- ---------
def about():
    global fabout
    hide_all_frame()
    fabout.place(x=450, y=150, width=800, height=600)
    txt4 = Text(fabout,bg="gray",font=("",12),fg="white",bd=0,width=200,height=200)
    with open('About.txt') as f:
        contents = f.read()
        txt4.insert(INSERT,f'{contents}')
        txt4.configure(state='disable')
    txt4.place(x=50, y=50)
    backbtn = Button(fabout, text=" Back ", command=main).place(x=10, y=10)

    #  --------  *************  Function for Menubar in Home Page  *************  ---------
def menubar():
    menufm = Frame(frame1,bg="gray")
    menufm.place(x=450, y=150, width=800, height=600)

    my_menu = Menu(menufm,font=("times new roman",35,"bold"))
    root.config(menu=my_menu)
    file_menu = Menu(my_menu, tearoff=False,font=("times new roman",13))
    my_menu.add_cascade(label="Settings",menu=file_menu,font=("times new roman",13))
    file_menu.add_command(label="Select Voice", command=voisel)
    file_menu.add_command(label="Set Speed", command=speed)
    file_menu.add_command(label="Exit", command=menufm.quit)
    help_menu = Menu(my_menu, tearoff=False,font=("times new roman",13))
    my_menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="How to use",command=how_to_use)
    help_menu.add_command(label="About",command=about)

def msg():
    exit = messagebox.askquestion("Confirm", "Are you sure?")
    if(exit == 'yes'):
        print("destroy")
        root.destroy()


def main():
    global fla,ms
    fla = 0

    hide_all_frame()
    frame1.place(x=450, y=150, width=900, height=600)


    title = Label(frame1, text="Choose option from here", font=("times new roman", 20, "bold"), bg="gray").place(x=50, y=30)

    btn1 = Button(frame1, text=" News ", font=("times new roman", 12, "bold"), bg="white", fg="black",
                  command=newsWin).place(x=50, y=100, width=150, height=30)
    btn1 = Button(frame1, text="Covid 19 tracker", font=("times new roman", 12, "bold"), bg="white", fg="black",
                  command=coWin).place(x=250, y=100, width=150, height=30)
    btn1 = Button(frame1, text=" Voice Search ", font=("times new roman", 12, "bold"), bg="white", fg="black",
                  command=audWin).place(x=50, y=150, width=150, height=30)
    btn1 = Button(frame1, text=" Close ", font=("times new roman", 12, "bold"), bg="white", fg="black",
                  command=msg).place(x=250, y=150, width=150,height=30)

    # menubtn = Menubutton(frame1, text=" = ", font=("times new roman", 15, "bold"), relief=RAISED)
    #
    #
    # menubtn.menu = Menu(menubtn, tearoff=0)
    # menubtn["menu"] = menubtn.menu
    # #text = Text(frame4, relwidth=1, relheight=1)
    #
    # language = IntVar()
    # help = IntVar()
    # settings = IntVar()
    #
    sidelabel = Label(frame1,image=sideicon).place(x=810, y=10,width=80, height=80)
    # # -----  menubutton for language selection and help ------
    #
    # menubtn.menu.add_checkbutton(label="Language", variable=language, command=langframe)
    # menubtn.menu.add_checkbutton(label="Help", variable=help, command=helpframe)
    # menubtn.place(x=800, y=10)

    menubar()

if __name__ == '__main__':
    global fla ,ms ,text
    ms=0
    fla =0
    sp =0
    root = Tk()
    root.title("  NEWS HEADS  ")
    root.geometry("1450x800+0+0")
    root.maxsize(width=1450, height=800)
    root.minsize(width=1450, height=800)
    flags = 2

    bg = ImageTk.PhotoImage(file="square.jpg")
    bglabel = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

    icon = PhotoImage(file="icon1.png")
    root.iconphoto(False, icon)

    fm = Frame(root,bg="white")
    fm.place(x=50,y=0,width=1300,height=150)
    head = Label(fm, text="NEWS HEADS", font=("times new roman", 40, "bold"), bg="#482756", fg="white").place(x=5,y=5,width=1290,height=140)

    # ---------- frame 2 for iamage -----------
    frame2 = Frame(root, bg="#520e5c")
    frame2.place(x=50, y=150, width=400, height=600)

    bg1 = ImageTk.PhotoImage(file="News.JPG")
    bg1label = Label(frame2, image=bg1).place(x=0, y=0, width=400, height=600)

    # --------- frame 1 for main frame --------
    frame1 = Frame(root, bg="gray")

    f5 = Frame(root,bg="gray")
    frame3 = Frame(root, bg="gray")
    frame4 = Frame(root, bg="gray")
    frame5 = Frame(root, bg="gray")
    f4 = Frame(root,bg="gray")
    v = StringVar(f4, "1")
    s = StringVar(f5, "2")
    fabout = Frame(root,bg="gray")
    fhow = Frame(root,bg="gray")
    sideicon = ImageTk.PhotoImage(file='newsicon2.png')


    global lanframe ,helpframe1

    menubar()
    main()
    # ------- -------- ----------  here all functional behaviour methods   -------- --------- -----------

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)

    root.update_idletasks()
    speak("Welcome to news heads")

    root.mainloop()

