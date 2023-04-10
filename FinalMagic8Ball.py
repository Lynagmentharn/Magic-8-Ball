from gpiozero import Button, PWMLED, RGBLED
import random
from pygame import mixer
from time import sleep
QuestionReady=True
v=0
ledR1= PWMLED(17)
ledB2= PWMLED(5)
ledG2= PWMLED(6)
led=RGBLED(red=12, green=16, blue=20)
button=Button(4)
print("This project was done by Group 10: Ryan Durham, Justina Edwards, and Josiah Gomez.")
sleep(1)
while QuestionReady==True:
    print("Push the button to ask the magic 8 ball a question.")
    button.wait_for_press()
    d = 0
    while d < 3:
        ledG2.value = 1
        sleep(0.5)
        ledG2.value = 0
        sleep(0.5)
        d+=1
    mixer.init()
    mixer.music.load("Intro.mp3")
    mixer.music.set_volume(0.5)
    mixer.music.play()
    input("Ask the Magic 8 Ball a yes or no question: ")
    e = 0
    while e < 2:
        ledB2.value = 1
        sleep(0.5)
        ledB2.value = 0
        sleep(0.5)
        e+=1
    print("Push the button again to recieve your answer.")
    button.wait_for_press()
    f = 0
    while f <2:
        ledR1.value = 1
        sleep(0.5)
        ledR1.value = 0
        sleep(0.5)
        f+=1 
    QuestionReady=False
    AnswerReady=True
    while AnswerReady==True:
        eightball= random.randint(1,8)
        if eightball==1:
            print("No.")
            mixer.init()
            mixer.music.load("No.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            Going=True
            while Going is True:
                ledR1.value = 1
                sleep(1)
                ledR1.value=0
                ledB2.value = 1
                sleep(1)
                ledB2.value=0
                ledG2.value = 1
                led.color=(0,1,0)
                sleep(.2)
                led.color=(1,1,0)
                sleep(.2)
                ledR1.value = 1
                ledB2.value = 1
                ledG2.value = 1
                led.color=(0,0,1)
                sleep(1)
                ledR1.value = 0
                ledB2.value = 0
                ledG2.value = 0
                led.color=(0,0,0)
                sleep(1)
                ledR1.value = 1
                ledB2.value = 1
                ledG2.value = 1
                led.color=(0,0,1)
                if v>=0.96:
                    v=0
                if v==0:
                    ledR1.value = v
                    ledB2.value = v
                    ledG2.value = v
                    led.color=(0,0,0)
                    Going=False
            sleep(1)
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
        if eightball==2:
            sleep(0.02)
            f2 = 0.25
            v+=f2
            if v>=0.96: f2*= -1
            elif v<= 0.04: f2*= -1
            print("The future is hazy.")
            mixer.init()
            mixer.music.load("Thefutureishazy.mp3")
            mixer.music.set_volume(0.8)
            mixer.music.play()
            Going=True
            ledR1.value=1
            led.color=(1,0,0)
            sleep(1)
            ledB2.value=1
            ledR1.value=0
            led.color=(0,0,1)
            sleep(1)
            led.color=(0,0,0)
            ledG2.value=1
            ledB2.value=0
            led.color=(0,1,0)
            sleep(1)
            led.color=(0.8,0.2,0.6)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            while Going is True:
                ledR1.value = v
                ledB2.value = v
                ledG2.value = v
                v+=0.08
                sleep(0.15)
                if v>=0.96:
                    v=0
                if v==0:
                    ledR1.value = v
                    ledB2.value = v
                    ledG2.value = v
                    led.color=(0,0,0)
                    Going=False
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
            AnswerReady=False
            button.wait_for_press(5)
        if eightball==3:
            print("Definitely not.")
            mixer.init()
            mixer.music.load("Definitelynot.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            Going=True
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(1)
            ledR1.value=0
            led.color=(0,0,0)
            ledB2.value=0
            ledG2.value=0
            sleep(1)
            ledR1.value=1
            led.color=(1,0.5,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.3)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            sleep(0.2)
            ledR1.value=1
            led.color=(1,0.5,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.3)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            sleep(0.2)
            ledR1.value=1
            led.color=(1,0.5,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.3)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            sleep(0.2)
            ledR1.value=1
            led.color=(1,0.5,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.3)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            sleep(0.2)
            ledR1.value=1
            led.color=(1,0.5,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.3)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
            button.wait_for_press(5)
        if eightball==4:
            print("Maybe.")
            mixer.init()
            mixer.music.load("Maybe.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            ledR1.value=1
            led.color=(1,0,1)
            ledB2.value=0
            ledG2.value=0
            sleep(0.75)
            led.color=(0,0,0)
            ledR1.value = 0
            ledB2.value = 0
            ledG2.value = 0
            sleep(0.2)
            ledB2.value=1
            ledG2.value=1
            sleep(0.75)
            ledB2.value=0
            ledG2.value=0
            sleep(0.5)
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
            button.wait_for_press(5)
        if eightball==5:
            print("Ask again later.")
            mixer.init()
            mixer.music.load("AskAgainLater.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()
            Going=True
            while Going is True:
                ledR1.value = v
                ledB2.value = v
                ledG2.value = v
                v+=0.19
                led.color=(0,1,0)
                sleep(.2)
                led.color=(0.58,0.29,0)
                sleep(.2)
                if v>=0.96:
                    v=0
                if v==0:
                    ledR1.value = v
                    ledB2.value = v
                    ledG2.value = v
                    led.color=(0,0,0)
                    Going=False
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
        if eightball==6:
            print("Doubtful.")
            mixer.init()
            mixer.music.load("Doubtful.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()
            Going=True
            v=.5
            c=.1
            while Going is True:
                led.color=(.9,0,0)
                ledR1.value = c
                ledB2.value = v
                ledG2.value = v
                v-=0.05
                c+=.09
                sleep(.5)
                if v<=0.01 or c>=.98:
                    v=0
                    c=0
                    ledR1.value = 0
                    ledB2.value = v
                    ledG2.value = v
                    led.color=(0,0,0)
                    Going=False
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
        if eightball==7:
            print("It is certain.")
            mixer.init()
            mixer.music.load("Itiscertain.mp3")
            mixer.music.set_volume(1)
            mixer.music.play()
            Going=True
            v=0.98
            while Going is True:
                ledR1.value = v
                ledB2.value = v
                ledG2.value = v
                v-=0.09
                led.color=(1,0,0)
                sleep(.2)
                led.color=(0,0,1)
                sleep(.2)
                if v<=0.05:
                    v=0
                if v==0:
                    ledR1.value = v
                    ledB2.value = v
                    ledG2.value = v
                    led.color=(0,0,0)
                    Going=False
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
        if eightball==8:
            print("Yes.")
            mixer.init()
            mixer.music.load("YES.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            sleep(0.2)
            ledR1.value=0.4
            ledB2.value=0.4
            ledG2.value=0.4
            sleep(1)
            ledR1.value=0
            ledB2.value=0
            ledG2.value=0
            sleep(.3)
            ledR1.value=0.6
            ledB2.value=0.6
            ledG2.value=0.6
            sleep(1)
            ledR1.value=0
            ledB2.value=0
            ledG2.value=0
            sleep(0.4)
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=1
            led.color=(0,0,0)
            ledB2.value=1
            ledG2.value=1
            sleep(0.2)
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=1
            led.color=(0,0,0)
            ledB2.value=1
            ledG2.value=1
            sleep(0.2)
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=1
            led.color=(0,0,0)
            ledB2.value=1
            ledG2.value=1
            sleep(0.2)
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=1
            led.color=(0,0,0)
            ledB2.value=1
            ledG2.value=1
            sleep(0.2)
            ledR1.value=1
            led.color=(1,1,1)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=1
            led.color=(0,0,0)
            ledB2.value=1
            ledG2.value=1
            sleep(0.02)
            ledR1.value=0
            led.color=(0,0,0)
            ledB2.value=0
            ledG2.value=0
            sleep(0.2)
            print("Push the button again if you would like to ask another question. If you dont have another question the program will time out in 10 seconds.")
            AnswerReady=False
            if button.wait_for_press(10)==True:
                QuestionReady=True
            else:
                mixer.init()
                mixer.music.load("Goodbye.mp3")
                mixer.music.set_volume(0.5)
                mixer.music.play()
                print("Goodbye, thanks for using the magic 8 ball!")
                break
