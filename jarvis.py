import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
import sys
import random
import calendar

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def screenshot():
    imp = pyautogui.screenshot()
    img.save('give path')


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(calendar.month_name[month])
    speak(year)


def wishme():
    speak("Welcome Back Achyuth")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning Achyuth")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Achyuth")
    elif hour >= 18 and hour < 24:
        speak("Good evening Achyuth")
    else:
        speak("Good Night Achyuth")
    speak('Jarvis at your service. please tell me how can i help you')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak('Say that again please')
        return 'None'
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak('Cpu is at ' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gmail id','password' )
    server.sendmail('gmail id', to, content)
    server.close()


def jokes():
    speak(pyjokes.get_joke())


def TicTacTOe():
    def place(num, x):
        # Returns the value in x at position num
        for i, v in enumerate(x):
            if v == num:
                return x[(i + 1)]
        return str(num)

    def print_grid(move, player, x):

        pos_list.extend([move, player])

        # Grid on which the player and computer play on
        template = """
    -------------
    | {} | {} | {} |
    |-----------|
    | {} | {} | {} |
    |-----------|
    | {} | {} | {} |
    --------------"""
        if x == 2:
            # Only prints if the player has made a move
            print(template.format(*(place(num + 1, pos_list) for num in range(9))))

    def winner(x, player, xx):
        wins = ((1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
                (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
                (1, 5, 9), (3, 5, 7))  # Diagonal

        if any(all(pos in x for pos in win) for win in wins):
            if xx != 1:
                if player in 'Jarvis':
                    speak('I won')
                else:
                    speak('You won')
                print('\n' * 5, "'{}'".format(player), "HAS WON!")
            return True
        return False

    def computer_AI_part(listx):
        global computer_move
        for x in range(1, 10):
            if x not in pos_list:
                listx.append(x)
                if (winner(listx, 'Jarvis', 1)):
                    del listx[-1]
                    computer_move = x
                    return 1
                del listx[-1]

    def computer_and_player():
        global computer_move, pos_list, player_list, computer_list
        replay, draw = 0, 0

        while True:

            # Replay's the game
            if replay:
                speak('Would you like to replay?')
                restart = input("Would you like to replay?: ").lower()
                if restart in ("y", "yes"):
                    pass
                elif restart in ("n", "no"):
                    return
                else:
                    print("Say 'yes' or 'no'")
                    continue
            else:
                print("\nTic Tac Toe - Jarvis vs You", '\n' * 2, "Jarvis goes first\n")
                speak('I go first')

            replay, computer_move, players_move, loop_count, pos_list, player_list, computer_list = 0, 0, 0, 0, [], [], []

            for each in "XXXXX":
                loop_count += 1

                # Computer's Move
                if computer_AI_part(computer_list) or computer_AI_part(player_list) == 1:
                    pass
                else:
                    while True:
                        computer_move = random.randint(1, 9)
                        if computer_move not in pos_list:
                            break
                computer_list.append(computer_move)
                # Prints Grid
                print_grid(computer_move, 'O', 2)

                if loop_count == 5:
                    if winner(player_list, 'player', 2) == True or winner(computer_list, 'Jarvis', 2) == True:
                        pass
                    else:
                        print("Match Was a draw!")
                        speak("It's Draw")
                    replay = 1
                    break

                # Checks winner
                if winner(computer_list, 'Jarvis', 2) == True:
                    replay = 1
                    break

                # Player's Move
                while True:
                    try:
                        speak("Your Turn")
                        players_move = int(input("\n\'%s\' Enter a value from the grid to plot your move: " % each))
                        if players_move in pos_list or players_move < 1 or players_move > 9:
                            speak("Your Turn")
                            print("Enter an available number that's between 1-9")

                            continue
                        break
                    except:
                        speak("Your Turn")
                        print("Enter a number")

                player_list.append(players_move)
                # Sets player's move for printing
                print_grid(players_move, each, 1)

                # Checks winner again
                if winner(player_list, 'player', 1) == True:
                    print_grid(players_move, each, 2)
                    winner(player_list, 'player', 2)
                    replay = 1
                    break

    computer_and_player()


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'offline' in query:
            speak('Good Bye Achyuth')
            break
        elif 'wikipedia' in query:
            speak('Searching')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'email' in query:
            speak('Who is the sender? ')
            sender = myCommand()

            if 'I am' in sender:
                try:
                    speak("Please Enter Email address of Recipient.")
                    Recipient_user = input("User: ")
                    speak('What should I say? ')
                    content = myCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("achyuth@gmail.com", '@passwordhere')
                    server.sendmail('achyuth@gmail.com', Recipient_user, content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry harsh! I am unable to send your message at this moment!')
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye harsh, have a good day.')
            sys.exit()
        elif 'search in chrome' in query:
            speak('what should i search?')
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        elif 'logout' in query:
            speak('Logging out')
            os.System('shutdown -l')
        elif 'shutdown' in query:
            speak('Shutting down')
            os.System('shutdown /s /t 1')
        elif 'restart' in query:
            speak('Restarting p c')
            os.System('shutdown /r /t 1')
        elif 'play song' in query:
            song_dr = 'B:\\Songs'
            speak('Shall i play Lost in Japan')
            t = takecommand()
            songs = os.listdir(song_dr)
            if 'yes' in t:
                os.startfile(os.path.join(song_dr, songs[0]))
            else:
                os.startfile(os.path.join(song_dr, random.choice(songs)))
            speak('Okay, here is your music! Enjoy!')
            from time import sleep
            sleep(60)
        elif 'send mail' in query:
            sendmail()
        elif 'remember that' in query:
            speak('what should i remember')
            data = takecommand()
            speak('You told me to remember' + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak('you told me to remember' + remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak('Done')
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'hello' in query:
            speak('Hello Achyuth')
        elif 'bye' in query:
            speak('Bye harsh, have a good day.')
            sys.exit()
        elif 'open youtube' in query:
            speak('okay')
            wb.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            wb.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay')
            wb.open('www.gmail.com')
        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'game' in query:
            speak("Let's play TicTacToe")
            TicTacTOe()
            speak('You are bad at this game')
        elif 'quote' in query:
            speak('Give yourself more time rather than thinking about others')