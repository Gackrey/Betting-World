from tkinter import *
import random
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
    li=[1,2,3,4,5,6]
    Label(ad,text="Enter Name:").grid(row=0)
    name=Entry(ad)
    name.grid(row=0,column=1)
    Label(ad,text="Enter Amount:").grid(row=1)
    amount=Entry(ad)
    amount.grid(row=1,column=1)
    Label(ad,text="Place Bet on:").grid(row=2)
    st=StringVar(ad)
    st.set("Choose->")
    OptionMenu(ad,st,*li).grid(row=2,column=1)
    Button(ad,text="Submit",command=lambda:click(ad,name,amount,st)).grid(row=3)

def end():
    div=0
    total=0
    check=random.randint(1,6)
    res.set(str(check))
    
    for i in range(len(mainlist)):
        total=total+int(mainlist[i][1])
        if check==int(mainlist[i][2]):
          div=div+1
    if div>0:
        ag=Tk()
        ag.title("Result")
        for i in range(len(mainlist)):
            if check==int(mainlist[i][2]):
               Label(ag,text=mainlist[i][0]+" has won Rs:"+str(total/div),font=("Arial",18,("bold","italic"))).pack()
    
        
def delete():
    dell=corrlist.index(box.get(ANCHOR))
    corrlist.remove(corrlist[dell])
    mainlist.remove(mainlist[dell])
    box.delete(ANCHOR)
#Declarations
mainlist=[]
corrlist=[]                                  
rand=0
root=Tk()
frame1=Frame(root)
frame1.pack()
root.title("Number Betting")
#Frame 1
#Result Line
Label(frame1,text="Result:",font=("Arial",18,("bold","italic"))).grid(row=0,column=1)
res=StringVar(frame1)
res.set(str(rand))
#Number line
respanel=Label(frame1,textvariable=res,bg='white',font=("Tahoma",30,"bold"))
respanel.grid(row=1,column=1)
#Buttons
add=Button(frame1,text="  Add  ",font=("Calibri",14),command=addfun)
add.grid(row=2,column=0)
add=Button(frame1,text="Remove",font=("Calibri",14),command=delete)
add.grid(row=2,column=1)
add=Button(frame1,text="Submit",font=("Calibri",14),command=end)
add.grid(row=2,column=2)
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
