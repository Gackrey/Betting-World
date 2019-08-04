from tkinter import *
import random
def confteam(root,en1,en2):
    teamvar.append(en1.get())
    teamvar.append(en2.get())
    tab_name=" VS ".join(teamvar)
    root.destroy()
    add0.destroy()
    add1.config(state=ACTIVE)
    add2.config(state=ACTIVE)
    add3.config(state=ACTIVE)
    respanel.config(text=tab_name)
    
def addteam():
    team=Tk()
    Label(team,text="Team 1:",font=("Arial",14)).grid(row=0,column=0)
    Label(team,text="Team 2:",font=("Arial",14)).grid(row=2,column=0)
    team1=Entry(team)
    team1.grid(row=0,column=1)
    Label(team,text="VS",font=("Arial",16,"bold")).grid(row=1)
    team2=Entry(team)
    team2.grid(row=2,column=1)
    Button(team,text="Submit",font=("Arial",14),command=lambda:confteam(team,team1,team2)).grid(row=3,column=1)
    
def click(add,nam,amm,st1):
    detail=[]
    detail.append(nam.get())
    detail.append(amm.get())
    detail.append(st1.get())
    temp=" ".join(detail)
    box.insert(END,temp)
    add.destroy()
    corrlist.append(temp)
    mainlist.append(detail)    
    
def addfun():
    ad=Tk()
    ad.title("Add Bet")
    Label(ad,text="Enter Name:").grid(row=0)
    name=Entry(ad)
    name.grid(row=0,column=1)
    Label(ad,text="Enter Amount:").grid(row=1)
    amount=Entry(ad)
    amount.grid(row=1,column=1)
    Label(ad,text="Place Bet on:").grid(row=2)
    st=StringVar(ad)
    st.set("Choose->")
    OptionMenu(ad,st,*teamvar).grid(row=2,column=1)
    Button(ad,text="Submit",command=lambda:click(ad,name,amount,st)).grid(row=3)
    
def end():
    ag=Tk()
    ag.title("Result")
    lb=Label(ag,text="Who won:->")
    lb.grid(row=0)
    ent=StringVar(ag)
    ent.set("Choose->")
    menu=OptionMenu(ag,ent,*teamvar)
    menu.grid(row=0,column=1)
    but=Button(ag,text="Submit",command=lambda:check(ag,lb,menu,but,ent))
    but.grid(row=0,column=2)
    
def check(rt,lb,line,but,en):
    div=0
    total=0
    lb.destroy()
    line.destroy()
    but.destroy()    
    for i in range(len(mainlist)):
        total=total+int(mainlist[i][1])
        if en.get()==mainlist[i][2]:
          div=div+1
          
    if div>0:
        for i in range(len(mainlist)):
            if en.get()==mainlist[i][2]:
               Label(rt,text=mainlist[i][0]+" has won Rs:"+str(total/div),font=("Arial",18,("bold","italic"))).pack()
    
def delete():
    dell=corrlist.index(box.get(ANCHOR))
    corrlist.remove(corrlist[dell])
    mainlist.remove(mainlist[dell])
    box.delete(ANCHOR)
    
#Declarations
mainlist=[]
corrlist=[]
teamvar=[]
tab_name=" "
root=Tk()
st=0
add0=Button(root,text="Add Teams",command=addteam)
add0.pack()
frame1=Frame(root)
frame1.pack()
root.title("Betting")    
#Frame 1
#Number line
respanel=Label(frame1,text=tab_name,bg='white',font=("Tahoma",16,"bold"))
respanel.grid(row=0,column=1)
#Buttons
add1=Button(frame1,text="  Add  ",font=("Calibri",14),state=DISABLED,command=addfun)
add1.grid(row=1,column=0)
add2=Button(frame1,text="Remove",font=("Calibri",14),state=DISABLED,command=delete)
add2.grid(row=1,column=1)
add3=Button(frame1,text="Submit",font=("Calibri",14),state=DISABLED,command=end)
add3.grid(row=1,column=2)
frame2=Frame(root)
frame2.pack(fill=BOTH)
#Frame 2
Label(frame2,text="List of Betters:",font=("Arial",12)).pack()
scr=Scrollbar(frame2)
scr.pack(side=RIGHT,fill=Y)
#Listbox
box=Listbox(frame2,yscrollcommand=(scr, 'set'))
box.pack(side=LEFT,fill=BOTH,expand=1)
scr.config(command=(box,'yview'))
mainloop()
