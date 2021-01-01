from tkinter import *
import tkinter.font as tkFont
import tkinter.font as tkFont
from PIL import ImageTk,Image
import winsound
from playsound import playsound



root = Tk()
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyleSpeed = tkFont.Font(family="Lucida Grande", size=50)

root.configure(background = "#000000")
#root.geometry(0,0)
myTitle= root.title("CAR SEATBELT SIMULATOR")
#myFont = tkFont.Font(family="Lucida Grande", fg="#fff", bg="#000000", font=(24))
FrameTitle = Frame(root, bg="#000000")
FrameTitle.pack(side=TOP)
myTitleLabel = Label(FrameTitle, text="CAR SEATBELT SIMULATOR", fg="#fff", bg="#000000",font=fontStyle)
myTitleLabel.pack()

FrameTop= Frame(root, bg="#000000")
FrameTop.pack(side=TOP)

FrameSpeed= Frame(root, bg="#000000")
FrameSpeed.pack(side=TOP)

FrameBelt= Frame(root, bg="#000000")
FrameBelt.pack(side=TOP)

FramePark= Frame(root, bg="#000000")
FramePark.pack(side=BOTTOM)

acc_img = ImageTk.PhotoImage(Image.open("accelerate.jpg"))
dec_img = ImageTk.PhotoImage(Image.open("decelerate.jpg"))
spd_img = ImageTk.PhotoImage(Image.open("speed.png"))

applyBelt_img  = ImageTk.PhotoImage(Image.open("usedbelt.jpg"))
removeBelt_img = ImageTk.PhotoImage(Image.open("seatunused.jpg"))
park_img  = ImageTk.PhotoImage(Image.open("park.png"))
exit_img  = ImageTk.PhotoImage(Image.open("exit.png"))



count = speed = 0
belt_status = {"apply":False, "remove":False}
def accelerate(belt_stat = 0):
    global spdLabel
    spdLabel.pack_forget()
    global count 
    count = count+1
    spdLabel = Label(FrameSpeed, text=count, fg="#ffffff", bg="#000000", font=fontStyleSpeed)
    spdLabel.pack()

    if belt_stat == 1:
        belt_status.update({"apply":True, "remove":False})
    if belt_stat == 2:
        belt_status.update({"apply":False, "remove":True})

    if count >= 5 and  belt_status['apply'] == False:
        raiseAlarm(True)
    

def decelerate(belt_stat = 0):
    global spdLabel
    spdLabel.pack_forget()
    global count 
    count = count-1
    spdLabel = Label(FrameSpeed, text=count, fg="#ffffff", bg="#000000", font=fontStyleSpeed)
    spdLabel.pack()

    if belt_stat == 2:
        belt_status.update({"remove":True})


    if count > 5 and  belt_status['remove'] == True:
        raiseAlarm(True)
    
    if count > 5 and  belt_status['apply'] == False:
        raiseAlarm(True)

def raiseAlarm(belt):
    if(belt == True):
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    if(belt == False):
        print("Thank you for using safety belt")

def parkCar():
    playsound('car.mp3')
    global spdLabel
    spdLabel.pack_forget()
    global count 
    count =  0
    textShow = "CAR PARKED"
    spdLabel = Label(FrameSpeed, text=textShow, fg="#ffffff", bg="#000000", font=fontStyleSpeed)
    spdLabel.pack()

def exitCar():
    return root.quit()

def apply():
    global seatBelt
    seatBelt = False
    global statusBelt
    global beltRemoveBtn
    statusBelt.pack_forget()
    beltRemoveBtn.pack_forget()
    statusBelt   = Label(FrameBelt,  text="BELT SAFELY USED", padx=20, pady=20, fg="green", bg="black", font=fontStyle)
    statusBelt.pack(side=LEFT)    
    beltRemoveBtn= Button(FrameBelt,  image=removeBelt_img,    bg="#000000", command=remove)
    beltRemoveBtn.pack(side=LEFT)
    accelerate(1)
    raiseAlarm(seatBelt)
    decelerate(1)

def remove():
    global seatBelt
    seatBelt = True
    global statusBelt
    global beltRemoveBtn
    statusBelt.pack_forget()
    beltRemoveBtn.pack_forget()
    statusBelt   = Label(FrameBelt,  text="BELT UNSAFELY REMOVED", padx=20, pady=20, fg="yellow", bg="black", font=fontStyle)
    statusBelt.pack(side=LEFT)
    beltRemoveBtn= Button(FrameBelt,  image=removeBelt_img,    bg="#000000", command=remove)
    beltRemoveBtn.pack(side=LEFT)
    raiseAlarm(seatBelt)
    accelerate(2)

accBtn             =      Button(FrameTop,  image=acc_img,  border=0,  bg="#000000", command=accelerate)
decBtn             =      Button(FrameTop,  image=dec_img, border=0,    bg="#000000", command=decelerate)
spdImg             =      Label(FrameTop,  image=spd_img,    bg="#000000")

beltApplyBtn       =      Button(FrameBelt,  image=applyBelt_img,     bg="#000000", command=apply)
beltRemoveBtn      =      Button(FrameBelt,  image=removeBelt_img,    bg="#000000", command=remove)
statusBelt         =      Label(FrameBelt,  text="BELT NOT USED", padx=20, pady=20, fg="red", bg="black", font=fontStyle)

parkBtn             =      Button(FramePark,  image=park_img,     bg="#000000", command=parkCar)
exitBtn             =      Button(FramePark,  image=exit_img,    bg="#000000", command=exitCar)
middleSpace         =     Label(FramePark,  text="SOMETHING", padx=20, pady=20, fg="black", bg="black", font=fontStyle)

accBtn.pack(side=LEFT)
spdImg.pack(side=LEFT) 
decBtn.pack(side=LEFT)
beltApplyBtn.pack(side=LEFT) 
statusBelt.pack(side=LEFT)
beltRemoveBtn.pack(side=LEFT)

parkBtn.pack(side=LEFT) 
middleSpace.pack(side=LEFT)
exitBtn.pack(side=LEFT)

spdLabel = Label(FrameSpeed, text="0:00", fg="#ffffff", bg="#000000", font=fontStyleSpeed)
spdLabel.pack()

root.mainloop()