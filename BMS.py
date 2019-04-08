#Bicycle Management System by Aiza, Arir, Mavzuna

from tkinter import *
import datetime
import tkinter.messagebox
import locale


       
#Main
window = Tk()

bike_count = open('bikecount.txt', 'r')
bike = int(open('bikecount.txt').read())
bike_count.close()

#Register Function
def register(event):
    '''
        (str,int,str,int)-->(str)
        stores user information (name, ID, password, email and graduation year) in a list
        writes the list into a file as string
        clears all entries 
    '''
    users = []

    

    name = username.get()
    ID = studentid.get()
    passw = password.get()
    mail = email.get()
    year = gyear.get()

    if (name == '') or (ID == 0) or (passw == '') or (mail == '') or (year == 0) :       
        tkinter.messagebox.showinfo('Missing Information', 'Please enter all fields.')
    else:
        posession = str(ID+'False')
        item = [name,ID,passw,mail,year,posession]

        users.extend(item)
        userstring = str(users)

        filename = "users.txt"
        file = open(filename, 'a')
        file.write(userstring+'\n')
        file.close()
        
        tkinter.messagebox.showinfo('Complete', 'Registration was successful. You may now borrow.')
        
    username.delete(0, END)
    studentid.delete(0, END)
    password.delete(0, END)
    email.delete(0, END)
    gyear.delete(0, END)

        
#Borrow Function   
def borrow(event):
    '''
        (str,str)-->(str)
        checks user information file for bike borrowed by user.
        Allows user to borrow if: user does not posess bike, bikes are available
        and user info is registered (in user information file) and correct.
        writes the possesion into user information file as string
        clears all entries 
    '''
    borrowtime = datetime.datetime.now()
          
    ID2 = str(studentid2.get())
    passw2 = str(password2.get())

    time = str(ID2+","+str(borrowtime))

    a = str(ID2+'False')
    b = str(ID2+'True')

    global bike
    print (bike)

   
    mystr = str(open('users.txt').read())
    
    
    if (a in mystr):
        if (bike>0):
            if (ID2 in mystr) and (passw2 in mystr) and (passw2 != '') and (ID2 != ''):
                with open('users.txt', 'r') as file:
                    replacement=file.read().replace(a, b)
                with open('users.txt', 'w') as file:
                    file.write(replacement)
                
                bike = bike-1
                print (bike)

                with open('bikecount.txt', 'w') as file:
                    file.write(str(bike))

                borrowtimestr = borrowtime.strftime("%Y-%m-%d %H:%M")
                returntime = (borrowtime + datetime.timedelta(hours=2)).strftime("%Y-%m-%d %H:%M")

                with open('time.txt', 'a') as file:
                    file.write(time+'\n')             
            
                tkinter.messagebox.showinfo('Complete', 'Borrow was successful. You must return within 2 hours. \nTime of Issue: '+borrowtimestr+
                                            '\nTime of Return: '+returntime)
            else:
                tkinter.messagebox.showinfo('Missing Information', 'Please enter all fields.')
        else:
            tkinter.messagebox.showinfo('No Bikes', 'Sorry, all bikes have been borrowed.')
    elif (b in mystr):
        tkinter.messagebox.showinfo('Posessed', 'You have already borrowed a bike. Please return it to borrow another.')
    else:
        tkinter.messagebox.showinfo('Wrong Info', 'Student ID or password is incorrect.')
        

    studentid2.delete(0, END)
    password2.delete(0, END)

    

#Return Function   
def bkreturn(event):
    '''
        (str,str)-->(str)
        checks user information file for bike borrowed by user.
        Allows user to return if: user posesses bike, bikes are less than their total number
        and user info is registered (in user information file) and correct.
        writes the return into user information file as string
        clears all entries 
    '''

    returntime = datetime.datetime.now()
    
    ID2 = str(studentid2.get())
    passw2 = str(password2.get())
    

    a = str(ID2+'False')
    b = str(ID2+'True')

    global bike
    print (bike)

   
    mystr = str(open('users.txt').read())
    
    
    if (b in mystr):
        if (bike<5):
            if (ID2 in mystr) and (passw2 in mystr) and (passw2 != '') and (ID2 != ''):
                with open('time.txt', 'r') as file:
                    for line in file:
                        if ID2 in line: 
                            mystr2 = line 
                            x = line.rstrip()
                            y = x.split(",")
                            borrowtime = datetime.datetime.strptime(y[1], "%Y-%m-%d %H:%M:%S.%f")
                            diff = (returntime - borrowtime)

                            seconds = diff.total_seconds()
                            minutes = (seconds % 3600) // 60

                            if (minutes <= 120):
                                with open('time.txt', 'r') as file:
                                    replacement=file.read().replace(mystr2, '')
                                with open('time.txt', 'w') as file:
                                    file.write(replacement)
                                with open('users.txt', 'r') as file:
                                    replacement=file.read().replace(b, a)
                                with open('users.txt', 'w') as file:
                                    file.write(replacement)
                                
                                bike = bike+1
                                print (bike)
                                
                                with open('bikecount.txt', 'w') as file:
                                    file.write(str(bike))
                                tkinter.messagebox.showinfo('Complete', 'Returned successfully in time. Come again.')
                            else:
                                with open('time.txt', 'r') as file:
                                    replacement=file.read().replace(mystr2, '')
                                with open('time.txt', 'w') as file:
                                    file.write(replacement)
                                with open('users.txt', 'r') as file:
                                    replacement=file.read().replace(b, a)
                                with open('users.txt', 'w') as file:
                                    file.write(replacement)
                                  
                                bike = bike+1
                                print (bike)
                                  
                                with open('bikecount.txt', 'w') as file:
                                    file.write(str(bike))
                                tkinter.messagebox.showinfo('Complete', 'Returned late. Be careful next time')
                            
            else:
                tkinter.messagebox.showinfo('Missing Information', 'Please enter all fields.')
                                        
        else:
            tkinter.messagebox.showinfo('All Bikes', 'No bikes have been borrowed.')
    elif (a in mystr):
        tkinter.messagebox.showinfo('None Posessed', 'You have not borrowed a bike. You may borrow one.')
    else:
        tkinter.messagebox.showinfo('Wrong Info', 'Student ID or password is incorrect.')

    studentid2.delete(0, END)
    password2.delete(0, END)


        

#Window Title
window.title("Bicycle Management System by Aiza, Arir, Mavzuna")

#Title
Label(window, text="Bicycle \n Management \n System", font="verdana 30 bold", fg='orange', bg='blue') .grid(row=0, column=0, sticky=N+E+W+S)

#Photo
pic1 = PhotoImage(file="pic1.png")
Label(window, image=pic1) .grid(row=0, column=1,columnspan=2,  sticky=W)

#New User Label
Label(window, text="NEW USER:", font="verdana 18 bold") .grid(row=2, column=0, sticky=W)

#Name Field
Label(window, text="Name:", font="verdana 12 bold") .grid(row=4, column=0, sticky=W)
username = Entry(window, width=35, bg="white", textvariable=StringVar())
username.grid(row=5, column=0, sticky=W)

#Student ID Field
Label(window, text="Student ID:", font="verdana 12 bold") .grid(row=6, column=0, sticky=W)
studentid = Entry(window, width=20, bg="white", textvariable=IntVar())
studentid.grid(row=7, column=0, sticky=W)

#Set Password
Label(window, text="Set Password:", font="verdana 12 bold") .grid(row=8, column=0, sticky=W)
password = Entry(window, width=35, bg="white", textvariable=StringVar(), show="*")
password.grid(row=9, column=0, sticky=W)

#Email Field
Label(window, text="Email:", font="verdana 12 bold") .grid(row=10, column=0, sticky=W)
email = Entry(window, width=35, bg="white", textvariable=StringVar())
email.grid(row=11, column=0, sticky=W)

#Graduation Year Field
Label(window, text="Graduation Year:", font="verdana 12 bold") .grid(row=12, column=0, sticky=W)
gyear = Entry(window, width=20, bg="white", textvariable=IntVar())
gyear.grid(row=13, column=0, sticky=W)

#Register Button
bregister = Button(window, text="REGISTER!", font="verdana 12 bold",  fg="red", width=10, height=2)
bregister.grid(row= 14, column=0, sticky=W)
bregister.bind("<Button-1>", register)

#Existing User Label
Label(window, text="EXISTING USER:", font="verdana 18 bold") .grid(row=2, column=1, sticky=E)

#Student ID Field
Label(window, text="Student ID:", font="verdana 12 bold") .grid(row=4, column=1, sticky=W)
studentid2 = Entry(window, width=20, bg="white", textvariable=IntVar())
studentid2.grid(row=5, column=1, sticky=W)

#Password
Label(window, text="Password:", font="verdana 12 bold") .grid(row=6, column=1, sticky=W)
password2 = Entry(window, width=35, bg="white", textvariable=StringVar(), show="*")
password2.grid(row=7, column=1, sticky=W)

#Borrow Button
bborrow = Button(window, text="BORROW", font="verdana 12 bold",  fg="red", width=10, height=2) 
bborrow.grid(row= 8, column=1, sticky=N+E+W+S)
bborrow.bind("<Button-1>", borrow)

#Return Button
breturn = Button(window, text="RETURN", font="verdana 12 bold",  fg="red", width=10, height=2)
breturn.grid(row= 9, column=1, sticky=N+E+W+S)
breturn.bind("<Button-1>", bkreturn)

#Exit Button
Button(window, text="EXIT", font="verdana 12 bold",  fg="red", width=10, height=2, command=quit) .grid(row= 14, column=1, sticky=W)


window. mainloop()
