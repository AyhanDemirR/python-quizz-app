from tkinter import END, messagebox
import MySQLdb
import tkinter as tk

#Sql
conn = MySQLdb.connect(host='localhost', database='quizdb', user='root', password='root')
cursor = conn.cursor()

def countdb():
    count = "select count(QID) from questions"
    cursor.execute(count)
    cNumber=cursor.fetchone()
    cNumber=cNumber[0]
    return cNumber

strQ = ""
questions = []
index = ''

#Menü
root=tk.Tk()
root.title('Soru Düzenleme-Ekleme')
root.geometry('1300x700+0+0')
root.config(background="Azure")

def soruyugetir():
    global index
    index=Q_list.curselection()
    if index:
        question=Q_list.get(index)
        soruEntry.delete(1.0,tk.END)
        soruEntry.insert(1.0,question[1])
        
        opAEntry.delete(0,tk.END)
        opAEntry.insert(0,question[2])
        
        opBEntry.delete(0,tk.END)
        opBEntry.insert(0,question[3])
        
        opCEntry.delete(0,tk.END)
        opCEntry.insert(0,question[4])

        opDEntry.delete(0,tk.END)
        opDEntry.insert(0,question[5])

        cevapEntry.delete(0,tk.END)
        if question[6]==1:
            cevapEntry.insert(0,'A')
        elif question[6]==2:
            cevapEntry.insert(0,'B')
        elif question[6]==3:
            cevapEntry.insert(0,'C')
        elif question[6]==4:
            cevapEntry.insert(0,'D')

    else:
        messagebox.showerror(title='Hata',message='Lütfen Getirmek İçin Bir Soru Seçiniz!')

def soruekle():
    global cursor
    global conn
    cNumber=countdb()

    if cevapEntry.get()=='A':
        ans=1
    elif cevapEntry.get()=='B':
        ans=2
    elif cevapEntry.get()=='C':
        ans=3
    elif cevapEntry.get()=='D':
        ans=4
    else:
        messagebox.showerror(title='Hata',message='Cevabı Kontrol Ediniz!')
        return
    
    cNumber+=1

    query = "insert into questions(QID, qstn, opA, opB, opC, opD, ans) values('{}','{}','{}','{}','{}','{}','{}')".format(
        cNumber,
        soruEntry.get(1.0,END),
        opAEntry.get(),
        opBEntry.get(),
        opCEntry.get(),
        opDEntry.get(),
        ans
    )
    
    cursor.execute(query)
    conn.commit()
    addedQ=(cNumber,soruEntry.get(1.0,END),opAEntry.get(),opBEntry.get(),opCEntry.get(),opDEntry.get(),ans)
    Q_list.insert(END,addedQ)

def soruguncelle():
    global cursor
    global conn
    selectedid=Q_list.curselection()
    
    if cevapEntry.get()=='A':
        ans=1
    elif cevapEntry.get()=='B':
        ans=2
    elif cevapEntry.get()=='C':
        ans=3
    elif cevapEntry.get()=='D':
        ans=4
    else:
        messagebox.showerror(title='Hata',message='Cevabı Kontrol Ediniz!')
        return

    selectedid=selectedid[0]
    query = "UPDATE questions SET qstn='{}', opA='{}', opB='{}', opC='{}', opD='{}', ans='{}' WHERE QID='{}'".format(
        soruEntry.get(1.0,END),
        opAEntry.get(),
        opBEntry.get(),
        opCEntry.get(),
        opDEntry.get(),
        ans,
        selectedid+1
    )
    cursor.execute(query)
    conn.commit()

    soruyugetirsDB()

def sorusil():
    global conn
    global cursor
    cNumber=countdb()
    selectedid=Q_list.curselection()
    
    if selectedid:
        selectedid=selectedid[0]
        query="DELETE FROM questions WHERE QID={}".format(selectedid+1)
        cursor.execute(query)
        conn.commit()

        for id in range(selectedid+2,cNumber+1):
            query="UPDATE questions SET QID={} WHERE QID={}".format(id-1,id)
            cursor.execute(query)
            conn.commit()

        soruyugetirsDB()
    else:
        messagebox.showerror(title="Hata",message="Lütfen Bir Soru Seçiniz!")
    

soruEntry=tk.Text(root)
soruEntry.place(relx=0.05,rely=0.1,relwidth=0.3,relheight=0.1)
soruLabel=tk.Label(root,text="Soru: ",font=('Times New Roman',12),bg='azure')
soruLabel.place(relx=0.015,rely=0.13)

opAEntry=tk.Entry(root)
opAEntry.place(relx=0.05,rely=0.220,relwidth=0.3,relheight=0.03)
opALabel=tk.Label(root,text="A: ",font=('Times New Roman',12),bg='azure')
opALabel.place(relx=0.03,rely=0.215)

opBEntry=tk.Entry(root)
opBEntry.place(relx=0.05,rely=0.263,relwidth=0.3,relheight=0.03)
opBLabel=tk.Label(root,text="B: ",font=('Times New Roman',12),bg='azure')
opBLabel.place(relx=0.03,rely=0.258)

opCEntry=tk.Entry(root)
opCEntry.place(relx=0.05,rely=0.306,relwidth=0.3,relheight=0.03)
opCLabel=tk.Label(root,text="C: ",font=('Times New Roman',12),bg='azure')
opCLabel.place(relx=0.03,rely=0.301)

opDEntry=tk.Entry(root)
opDEntry.place(relx=0.05,rely=0.349,relwidth=0.3,relheight=0.03)
opDLabel=tk.Label(root,text="D: ",font=('Times New Roman',12),bg='azure')
opDLabel.place(relx=0.03,rely=0.344)

cevapEntry=tk.Entry(root)
cevapEntry.place(relx=0.05,rely=0.392,relwidth=0.3,relheight=0.03)
cevapLabel=tk.Label(root,text="Cevap: ",font=('Times New Roman',12),bg='azure')
cevapLabel.place(relx=0.006,rely=0.387)

sorusecButton=tk.Button(root,text='Soruyu Getir',font=('Times New Roman',10),command=soruyugetir)
sorusecButton.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.03)

soruekleButton=tk.Button(root,text='Soruyu Ekle',font=('Times New Roman',10),command=soruekle)
soruekleButton.place(relx=0.8,rely=0.143,relwidth=0.1,relheight=0.03)

soruguncelleButton=tk.Button(root,text='Soruyu Güncelle',font=('Times New Roman',10),command=soruguncelle)
soruguncelleButton.place(relx=0.8,rely=0.186,relwidth=0.1,relheight=0.03)

sorusilButton=tk.Button(root,text='Soruyu Sil',font=('Times New Roman',10),command=sorusil)
sorusilButton.place(relx=0.8,rely=0.229,relwidth=0.1,relheight=0.03)

Q_Frame = tk.Frame(root,width=1300,height=350)
Q_Frame.place(x=0,y=350)
Q_Scroll=tk.Scrollbar(Q_Frame)
Q_Scroll.place(x=1287,relwidth=0.01,relheight=1)
Q_list=tk.Listbox(Q_Frame,relief='sunken',borderwidth=3)
Q_list.place(x=0,y=0,relwidth=0.99,relheight=1)
Q_list.configure(yscrollcommand = Q_Scroll.set)
Q_Scroll.configure(command= Q_list.yview)

def soruyugetirsDB():
    global cursor
    global questions
    cNumber=countdb()
    questions = []
    for id in range(cNumber):    
        s = "select QID,qstn,opA,opB,opC,opD,ans from questions where QID={}".format(id+1)
        cursor.execute(s)
        strQ = cursor.fetchone()
        questions.append(strQ)
    Q_list.delete(0,END)
    for question in questions:
        Q_list.insert(tk.END,question)
    
soruyugetirsDB()

root.mainloop()