#graphical user interface(GUI)

from tkinter import*
root=Tk()
root.title('myfirstapp')
root.geometry('400x700')
ID=IntVar()
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
Label(root, text="ID").grid(row=0,column=0)
Entry(root,textvariable=ID).grid(row=0,column=1)
ID.set('')

NAME=StringVar()
Label(root, text="NAME").grid(row=1,column=0)
Entry(root,textvariable=NAME).grid(row=1,column=1)


MARK1=IntVar()
Label(root, text="MARK1").grid(row=2,column=0)
Entry(root,textvariable=MARK1).grid(row=2,column=1)
MARK1.set('')

MARK2=IntVar()
Label(root, text="MARK2").grid(row=3,column=0)
Entry(root,textvariable=MARK2).grid(row=3,column=1)
MARK2.set('')

MARK3=IntVar()
Label(root, text="MARK3").grid(row=4,column=0)
Entry(root,textvariable=MARK3).grid(row=4,column=1)
MARK3.set('')

def gendersel():
    gen = ID5.get()
    if gen == 14:
        return 'Male'
    else:
        return 'Female'


def savetofile():
    import csv
    import os.path
    a=ID.get()
    b=NAME.get()
    c=MARK1.get()
    d=MARK2.get()
    e=MARK3.get()
    total=c+d+e
    avg=total/3
    g=gendersel()
    print(a, b, c, d, e,total,avg,g)
    country=[]
    I=check1.get()
    U=check2.get()
    US=check3.get()
    if I == 1:
        country.append('India')
    elif U == 1:
        country.append('UK')
    elif US == 1:
        country.append('USA')

    x= ",".join(country)
    state=value_inside.get()
    Rank=value_inside.get()

    fileexist=os.path.isfile('mycsv.csv')
    if fileexist:
      with open('mycsv.csv', 'a', newline="") as f:
        w = csv.writer(f)
        w.writerow([a,b,c,d,e, total, avg,g,I,U,US,x,state,Rank])
    else:
      with open('mycsv.csv', 'a', newline="") as f:
        w = csv.writer(f)
        w.writerow(['ID', 'NAME', 'MARK1', 'MARK2', 'MARK3', 'total', 'avg','Gender','country','state','Rank'])
        w.writerow([a,b,c,d,e, total, avg,g,I,U,US,x,state,Rank])

    root.destroy()
ID5=IntVar()
Label(root, text="Gender").grid(row=5,column=0)
Radiobutton(root, variable=ID5, text='Male', value=14, command=gendersel).grid(row=5, column=1)
Radiobutton(root, variable=ID5, text='Female', value=2, command=gendersel).grid(row=5, column=2)

Label(root,text="country").grid(row=6,column=0)
Checkbutton(root, variable=check1, text='India', onvalue=1, offvalue=0).grid(row=6, column=1)
Checkbutton(root, variable=check2, text='UK', onvalue=1, offvalue=0).grid(row=6, column=2)
Checkbutton(root, variable=check3, text='USA', onvalue=1, offvalue=0).grid(row=6, column=3)
options_list = ["Tamil Nadu", "Kerala", "Mumbai", "Delhi"]
value_inside = StringVar(root)
value_inside.set("Select an Option")
Label(root,text="State").grid(row=7,column=0)
OptionMenu(root, value_inside, *options_list).grid(row=7,column=1)

options_list = ["first class", "second class", "third class"]
value_inside = StringVar(root)
value_inside.set("Select an Option")
Label(root,text="Rank").grid(row=8,column=0)
OptionMenu(root, value_inside, *options_list).grid(row=8,column=1)

Button(root,text="Submit",command=savetofile).grid(row=9,column=1)

root.mainloop()

