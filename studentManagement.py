from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import datetime
import backend

class Student:

    def __init__(self,root):
        self.root = root
        self.root.title('student record database systems')
        self.root.geometry('1350x750')
        self.root.config(bg='cadet blue')

        Stdid = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Coursecode = StringVar()
        Examno = StringVar()
        Maths = StringVar()
        English = StringVar()
        Biology = StringVar()
        Computing = StringVar()
        Chemistry = StringVar()
        Physics = StringVar()
        Addmaths = StringVar()
        Business = StringVar()
        Totalscore = StringVar()
        Average = StringVar()
        Ranking = StringVar()
        Dateissued = StringVar()   
        #============================== Functions ==================================
        
        def Exit():
            qExit = tkinter.messagebox.askyesno('QUIT SYSTEM ',' DO YOU WANT TO QUIT ?')
            if qExit > 0:
                root.destroy()
                return
            
        def Clear():
            Stdid.set('')
            Firstname.set('')
            Surname.set('')
            Coursecode.set('')
            Examno.set('')
            Maths.set('')
            English.set('')
            Biology.set('')
            Computing.set('')
            Chemistry.set('')
            Physics.set('')
            Addmaths.set('')
            Business.set('')
            Totalscore.set('')
            Average.set('')
            Ranking.set('')
            self.txtUnitgrades.delete('1.0',END)

        def AddUnitScore():
             
           Unit1 = float(Maths.get())
           Unit2 = float(English.get())        
           Unit3 = float(Biology.get())
           Unit4 = float(Computing.get())
           Unit5 = float(Chemistry.get())
           Unit6 = float(Physics.get())
           Unit7 = float(Addmaths.get())
           Unit8 = float(Business.get())

           Unitaverage = (Unit1 + Unit2 + Unit3 +Unit4 +Unit5+Unit6+Unit7+Unit8) /8
           Unittotal = (Unit1+Unit2+Unit3+Unit4+Unit5+Unit6+Unit7+Unit8)
           Totalscore.set(str('%.2f'%(Unittotal)))
           Average.set(str('%.2f'%(Unitaverage)))

           if Unittotal >= 700:
               Ranking.set('1st Class')
           elif Unittotal > 600:
               Ranking.set('2nd Upper')
           elif Unittotal >500:
               Ranking.set('2nd Lower')
           elif Unittotal >400:
               Ranking.set('3rd Class')
           elif Unittotal >200 and Unittotal <= 399:
               Ranking.set('certification of higher education (coHE)')
           else:
               Ranking.set('FAIL')
           time1 = datetime.datetime.now()
           Dateissued.set(time1.strftime('%d/%m/%Y'))
           self.txtUnitgrades.insert(END,'============= TRANSCRIPT =============')
           self.txtUnitgrades.insert(END,'student ID :\t\t' + Stdid.get() + '\t\t' + Dateissued.get() + '\n')
           self.txtUnitgrades.insert(END,'====================================='+ '\n')
           self.txtUnitgrades.insert(END,'FIRST NAME : \t\t\t'+Firstname.get() +'\n')
           self.txtUnitgrades.insert(END,'SURNAME : \t\t\t'+Surname.get() + '\n')
           self.txtUnitgrades.insert(END,'COURSE CODE :\t\t\t '+Coursecode.get() +'\n')
           self.txtUnitgrades.insert(END,'MATHS : \t\t\t'+Maths.get() +'\n')
           self.txtUnitgrades.insert(END,'ENGLISH : \t\t\t'+English.get()+'\n')
           self.txtUnitgrades.insert(END,'BIOLOGY :\t\t\t'+Biology.get()+'\n')
           self.txtUnitgrades.insert(END,'COMPUTING :\t\t\t'+Computing.get()+'\n')
           self.txtUnitgrades.insert(END,'CHEMISTRY :\t\t\t' +Chemistry.get() +'\n')
           self.txtUnitgrades.insert(END,'PHYSICS : \t\t\t'+Physics.get()+'\n')
           self.txtUnitgrades.insert(END,'ADDMATHS : \t\t\t'+Addmaths.get()+'\n')
           self.txtUnitgrades.insert(END,'BUSINESS :\t\t\t'+Business.get()+'\n')
           self.txtUnitgrades.insert(END,'======================================'+'\n')
           self.txtUnitgrades.insert(END,'TOTAL SCORE :\t\t\t'+Totalscore.get()+'\n')
           self.txtUnitgrades.insert(END,'AVERAGE :\t\t\t'+Average.get()+'\n')
           self.txtUnitgrades.insert(END,'RANKING :\t\t\t'+Ranking.get()+'\n')
           self.txtUnitgrades.insert(END,'====================================='+'\n')

        #========================= database function ================================

        def adddata():
            AddUnitScore()
            if (len(Stdid.get())!=0):
                backend.addstdrec(Stdid.get(),Firstname.get(),Surname.get(),Coursecode.get(),\
                                  Maths.get(),English.get(),Biology.get(),Computing.get(),\
                                  Chemistry.get(),Physics.get(),Addmaths.get(),Business.get(),\
                                  Totalscore.get(),Average.get(),Ranking.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(Stdid.get(),Firstname.get(),Surname.get(),Coursecode.get(),\
                                  Maths.get(),English.get(),Biology.get(),Computing.get(),\
                                  Chemistry.get(),Physics.get(),Addmaths.get(),Business.get(),\
                                  Totalscore.get(),Average.get(),Ranking.get()))
        
        def displaydata():
            for row in backend.viewdata():
                studentlist.insert(END,row,str(''))

        def deletedata():
            if (len(Stdid.get()) != 0):
                backend.deleterec(sd[0])
                clear()
                displaydata()

        def searchdatabase():
            studentlist.delete(0,END)
            for row in backend.searchdata(Stdid.get(),Firstname.get(),Surname.get(),Coursecode.get(),\
                                  Maths.get(),English.get(),Biology.get(),Computing.get(),\
                                  Chemistry.get(),Physics.get(),Addmaths.get(),Business.get(),\
                                  Totalscore.get(),Average.get(),Ranking.get()):
                studentlist.insert(END,row,str(''))

        def update():
            if (len(stddid.get())!=0):
                backend.deleterec(sd[0])
            if (len(stdid.get())!=0):
                backend.addstdrec(Stdid.get(),Firstname.get(),Surname.get(),Coursecode.get(),\
                                  Maths.get(),English.get(),Biology.get(),Computing.get(),\
                                  Chemistry.get(),Physics.get(),Addmaths.get(),Business.get(),\
                                  Totalscore.get(),Average.get(),Ranking.get())
            studentlist.delete(0,END)
            studentlist.insert(END,(Stdid.get(),Firstname.get(),Surname.get(),Coursecode.get(),\
                                  Maths.get(),English.get(),Biology.get(),Computing.get(),\
                                  Chemistry.get(),Physics.get(),Addmaths.get(),Business.get(),\
                                  Totalscore.get(),Average.get(),Ranking.get()))

        def studentrec(event):
             global sd
             searchstd = studentlist.curselection()[0]
             sd = studentlist.get(searchstd)

             self.txtStdid.delete(0,END)
             self.txtStdid.insert(END,sd[1])
             self.txtFirstname.delete(0,END)
             self.txtFirstname.insert(END,sd[2])
             self.txtSurname.delete(0,END)
             self.txtSurname.insert(END,sd[3])
             self.txtCoursecode.delete(0,END)
             self.txtCoursecode.insert(END,sd[4])
             self.txtMaths.delete(0,END)
             self.txtMaths.insert(END,sd[5])
             self.txtEnglish.delete(0,END)
             self.txtEnglish.insert(END,sd[6])
             self.txtBiology.delete(0,END)
             self.txtBiology.insert(END,sd[7])
             self.txtComputing.delete(0,END)
             self.txtComputing.insert(END,sd[8])
             self.txtChemistry.delete(0,END)
             self.txtChemistry.insert(END,sd[9])
             self.txtPhysics.delete(0,END)
             self.txtPhysics.insert(END,sd[10])
             self.txtAddmaths.delete(0,END)
             self.txtAddmaths.insert(END,sd[11])
             self.txtBusiness.delete(0,END)
             self.txtBusiness.insert(END,sd[12])
             self.txtTotalscore.delete(0,END)
             self.txtTotalscore.insert(END,sd[13])
             self.txtAverage.delete(0,END)
             self.txtAverage.insert(END,sd[14])
             self.txtRanking.delete(0,END)
             self.txtRanking.insert(END,sd[15])
             
        #======================== FRAME =============================================     
        MainFrame = Frame(self.root , bg= 'firebrick')
        MainFrame.grid()
        
        DataFrameBottom = Frame(MainFrame,bd=1,width=1300,height=400,relief=RIDGE,pady=20,padx=20,bg='firebrick')
        DataFrameBottom.pack(side = BOTTOM)

        ListFrameTop = Frame(DataFrameBottom,bd=1,width=1350,height=200,relief=RIDGE,pady=10,padx=18,bg='lightcoral')
        ListFrameTop.pack(side = TOP)
        ListFrameBottom = Frame(DataFrameBottom,bd=1,width=1350,height=40,relief=RIDGE,pady=10,padx=18,bg='lightcoral')
        ListFrameBottom.pack(side = BOTTOM)
        
        DataFrameTop = Frame(MainFrame,bd=1,width=1300,height=70,relief=RIDGE,pady=20,padx=20,bg='indianred')
        DataFrameTop.pack(side = TOP)

        DataFrameLeft = LabelFrame(DataFrameTop,bd=1,width=900,height=400,relief=RIDGE,bg='Ghost White',font=('arial',18,'bold'),text= 'STUDENT DETAILS\n')
        DataFrameLeft.pack(side = LEFT)

        DataFrameRight = LabelFrame(DataFrameTop,bd=1,width=450,height=400,relief=RIDGE,bg='lightcoral',font=('arial',18,'bold'),text = 'UNIT GRADES\n')
        DataFrameRight.pack(side = RIGHT)
        #============================== Widget =================================

        self.lblstdid = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='STUDENT ID : ',padx =2, pady=2,bg='ghost White')
        self.lblstdid.grid(row=0,column=0,sticky = W) # sticky in capital letters
        self.textstdid = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Stdid,bg = 'ghost white') # we cannot use padding here
        self.textstdid.grid(row=0,column=1)

        
        self.lblCoursecode = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='COURSE ID : ',padx =2, pady=2,bg='ghost White')
        self.lblCoursecode.grid(row=1,column=0,sticky = W) # sticky in capital letters
        self.cboCoursecode = ttk.Combobox(DataFrameLeft,textvariable=Coursecode,font = ('Arial',14,'bold'),state = 'readonly',width=17)
        self.cboCoursecode['values']=('','7712','7713','7714','7715','7716','7717')
        self.cboCoursecode.current(2)
        self.cboCoursecode.grid(row=1,column=1,pady=3,padx=20)
    
        
        self.lblFirstname = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='FIRST NAME : ',padx =2, pady=2,bg='ghost White')
        self.lblFirstname.grid(row=2,column=0,sticky = W) # sticky in capital letters
        self.textFirstname = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Firstname ,bg = 'ghost white') # we cannot use padding here
        self.textFirstname.grid(row=2,column=1)

        
        self.lblSurname = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='SURNAME : ',padx =2, pady=2,bg='ghost White')
        self.lblSurname.grid(row=3,column=0,sticky = W) # sticky in capital letters
        self.textSurname = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Surname ,bg = 'ghost white') # we cannot use padding here
        self.textSurname.grid(row=3,column=1)
        
        self.lblExamno = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='EXAM NO : ',padx =2, pady=2,bg='ghost White')
        self.lblExamno.grid(row=4,column=0,sticky = W) # sticky in capital letters
        self.textExamno = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Examno,bg = 'ghost white') # we cannot use padding here
        self.textExamno.grid(row=4,column=1)

        
        self.lblTotalscore = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='TOTAL SCORE : ',padx =2, pady=2,bg='ghost White')
        self.lblTotalscore.grid(row=5,column=0,sticky = W) # sticky in capital letters
        self.textTotalscore = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Totalscore ,bg = 'ghost white') # we cannot use padding here
        self.textTotalscore.grid(row=5,column=1)
        
        
        self.lblAverage = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='AVERAGE : ',padx =2, pady=2,bg='ghost White')
        self.lblAverage.grid(row=6,column=0,sticky = W) # sticky in capital letters
        self.textAverage = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Average ,bg = 'ghost white') # we cannot use padding here
        self.textAverage.grid(row=6,column=1)
    
        
        self.lblRanking = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='RANKING : \n',padx =2, pady=2,bg='ghost White')
        self.lblRanking.grid(row=7,column=0,sticky = W) # sticky in capital letters
        self.textRanking = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Ranking ,bg = 'ghost white') # we cannot use padding here
        self.textRanking.grid(row=7,column=1)

        self.lblMaths = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='MATHS : ',padx =2, pady=2,bg='ghost White')
        self.lblMaths.grid(row=0,column=2,sticky = W) # sticky in capital letters
        self.textMaths = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable =Maths ,bg = 'ghost white') # we cannot use padding here
        self.textMaths.grid(row=0,column=3)

        
        self.lblComputing = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='COMPUTING : ',padx =2, pady=2,bg='ghost White')
        self.lblComputing.grid(row=1,column=2,sticky = W) # sticky in capital letters
        self.textComputing = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Computing ,bg = 'ghost white') # we cannot use padding here
        self.textComputing.grid(row=1,column=3)
        
        
        self.lblEnglish = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='ENGLISH : ',padx =2, pady=2,bg='ghost White')
        self.lblEnglish.grid(row=2,column=2,sticky = W) # sticky in capital letters
        self.textEnglish = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = English ,bg = 'ghost white') # we cannot use padding here
        self.textEnglish.grid(row=2,column=3)
    
        
        self.lblBiology = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='BIOLOGY : ',padx =2, pady=2,bg='ghost White')
        self.lblBiology.grid(row=3,column=2,sticky = W) # sticky in capital letters
        self.textBiology = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Biology ,bg = 'ghost white') # we cannot use padding here
        self.textBiology.grid(row=3,column=3)
        
        self.lblChemistry = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='CHEMISTRY : ',padx =2, pady=2,bg='ghost White')
        self.lblChemistry.grid(row=4,column=2,sticky = W) # sticky in capital letters
        self.textChemistry = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable =Chemistry ,bg = 'ghost white') # we cannot use padding here
        self.textChemistry.grid(row=4,column=3)

        
        self.lblPhysics = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='PHYSICS : ',padx =2, pady=2,bg='ghost White')
        self.lblPhysics.grid(row=5,column=2,sticky = W) # sticky in capital letters
        self.textPhysics = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Physics ,bg = 'ghost white') # we cannot use padding here
        self.textPhysics.grid(row=5,column=3)

        
        self.lblAddmaths = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='ADD MATHS : ',padx =2, pady=2,bg='ghost White')
        self.lblAddmaths.grid(row=6,column=2,sticky = W) # sticky in capital letters
        self.textAddmaths = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable = Addmaths ,bg = 'ghost white') # we cannot use padding here
        self.textAddmaths.grid(row=6,column=3)
    
        
        self.lblBusiness = Label(DataFrameLeft, font = ('Arial',14,'bold'),text='BUSINESS : \n',padx =2, pady=2,bg='ghost White')
        self.lblBusiness.grid(row=7,column=2,sticky = W) # sticky in capital letters
        self.textBusiness = Entry(DataFrameLeft,width=19,font = ('Arial',14,'bold'),textvariable =Business ,bg = 'ghost white') # we cannot use padding here
        self.textBusiness.grid(row=7,column=3)

        
        #========================== UNIT GRADES =================================

        self.txtUnitgrades = Text(DataFrameRight,height =15, width = 43, bd =1, font =('arial',11,'bold'))
        self.txtUnitgrades.grid(row = 0, column = 0)
        #========================== ListFrame =====================================
        
        scrollbar = Scrollbar  (ListFrameTop)
        scrollbar.grid(row =0 , column = 1,sticky = 'ns')
        
        studentlist = Listbox (ListFrameTop,width = 141 , height = 7 , font = ('arial',12,'bold'),yscrollcommand = scrollbar.set)
        studentlist.grid(row =0 ,column=0, padx=8)
        scrollbar.config(command = studentlist.yview)
        #============================ ButtonFrame =====================================
        
        self.btnAddData = Button(ListFrameBottom , text = 'ADD NEW' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=13, command =adddata)
        self.btnAddData.grid(row=0,column =0)

        self.btnDisplayData = Button(ListFrameBottom , text = 'DISPLAY' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=9,command=displaydata)
        self.btnDisplayData.grid(row=0,column =1)
    
        self.btnClearData = Button(ListFrameBottom , text = 'CLEAR' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=9,command= Clear)
        self.btnClearData.grid(row=0,column =2)

        self.btnDeleteData = Button(ListFrameBottom , text = 'DELETE' , font=('arial',12,'bold'),height = 1,width=16 ,bd =2,padx=9,command=deletedata)
        self.btnDeleteData.grid(row=0,column =3)

        self.btnSearchData = Button(ListFrameBottom , text = 'SEARCH' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=9,command=searchdatabase)
        self.btnSearchData.grid(row=0,column =4)

        self.btnUpdateData = Button(ListFrameBottom , text = 'UPDATE' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=9)
        self.btnUpdateData.grid(row=0,column =5)

        self.btnExit = Button(ListFrameBottom , text = 'EXIT' , font=('arial',12,'bold'),height = 1,width =16 ,bd =2,padx=9,command = Exit)
        self.btnExit.grid(row=0,column =6)

        
if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
        
