from tkinter import *
import sqlite3
import tkinter.messagebox
import time
from datetime import *
from tkinter.ttk import Combobox
from PIL import Image
from tkinter import filedialog
from prettytable import PrettyTable
import os
import sys


# localtime = time.asctime(time.localtime(time.time()))
class Main_window(object):
    def hide(self):
        self.mainwindow.withdraw()

    def __init__(self, parent):

        def open_main_screen():
            database = sqlite3.connect("LMS.sqlite")
            name = username_Input.get()
            passwordin = password_Input.get()
            for username, password in database.execute("SELECT * FROM login WHERE username Like ? AND password Like ?", (name, passwordin)):
                if password == passwordin and username == name:
                    login_screen()       
                else:
                    tkinter.messagebox.showinfo('Login Information', 'Username and Password dose not mach!!')

            database.close()

            # ======================================= Other Toplavel Window =============================
        def login_screen():
            def exitmain():
                answer = tkinter.messagebox.askquestion('Exit confirmation', 'Do you want to close?')
                if answer == 'yes':
                    sys.exit()

            def student_report():
                from prettytable import PrettyTable
                import os

                conn = sqlite3.connect('LMS.sqlite')
                curs = conn.cursor()
                #curs.execute('SELECT State, Name, ESTIMATESBASE2010 AS Est2010 FROM pop_est WHERE region="1" ORDER BY Name')
                curs.execute('SELECT * FROM student_add ORDER BY studentname')

                col_names = [cn[0] for cn in curs.description]
                rows = curs.fetchall()

                x = PrettyTable(col_names)
                x.align[col_names[0]] = "l"
                x.align[col_names[1]] = "l"
                x.align[col_names[2]] = "l"
                x.align[col_names[3]] = "l"
                x.align[col_names[4]] = "l"
                x.align[col_names[5]] = "l"
                x.align[col_names[7]] = "l"
                x.align[col_names[8]] = "l"

                x.padding_width = 1
                for row in rows:
                    x.add_row(row)

                tabstring = x.get_string()

                output = open("export.txt", "w")
                output.write("Book Report"+"\n")
                output.write(tabstring)
                output.close()
                os.system('export.txt')

            def book_report():
                from prettytable import PrettyTable
                import os

                conn = sqlite3.connect('LMS.sqlite')
                curs = conn.cursor()
                curs.execute('SELECT * FROM book_entry ORDER BY bookuid')

                col_names = [cn[0] for cn in curs.description]
                rows = curs.fetchall()

                x = PrettyTable(col_names)
                x.align[col_names[0]] = "l"
                x.align[col_names[1]] = "l"
                x.align[col_names[2]] = "l"
                x.align[col_names[3]] = "l"
                x.align[col_names[4]] = "l"
                x.align[col_names[5]] = "l"
                x.align[col_names[6]] = "l"

                x.padding_width = 1
                for row in rows:
                    x.add_row(row)

                tabstring = x.get_string()

                output = open("export.txt", "w")
                output.write("Student Report"+"\n")
                output.write(tabstring)
                output.close()
                os.system('export.txt')

            def issue_report():
                from prettytable import PrettyTable
                import os

                conn = sqlite3.connect('LMS.sqlite')
                curs = conn.cursor()
                curs.execute('SELECT * FROM issuebook ORDER BY bookuid')

                col_names = [cn[0] for cn in curs.description]
                rows = curs.fetchall()

                x = PrettyTable(col_names)
                x.align[col_names[0]] = "l"
                x.align[col_names[1]] = "l"
                x.align[col_names[2]] = "l"
                x.align[col_names[3]] = "l"
                x.align[col_names[4]] = "l"
                x.align[col_names[5]] = "l"
                x.align[col_names[6]] = "l"
                x.align[col_names[7]] = "l"
                x.align[col_names[8]] = "l"

                x.padding_width = 1
                for row in rows:
                    x.add_row(row)

                tabstring = x.get_string()

                output = open("export.txt", "w")
                output.write("Book Issue Report"+"\n")
                output.write(tabstring)
                output.close()
                os.system('export.txt')

            self.mainwindow.withdraw()
            main_screen = Toplevel()
            main_screen.title("Library Management System")
            main_screen.state('zoomed')
            # =====================Frame===========================
            menu_frame = Frame(main_screen, width=1024, height=50, bg='pink', relief='sunken')
            menu_frame.pack(side='top')
            text_LMS = Label(menu_frame, font=('arial', 20, 'bold'), text="Library Management System").pack()

            frame1 = Frame(main_screen, width=512, height=700, relief='sunken')
            frame2 = Frame(main_screen, width=512, height=700, bg='alice blue', relief='sunken')
            frame3 = Frame(main_screen, width=200, height=700, relief='sunken')
            frame3.pack(side='left')
            frame1.pack(side='left')
            frame2.pack(side='right')

            # ===============================Menu===========================================
            menu = Menu(main_screen)
            main_screen.config(menu=menu)

            subMenu = Menu(menu)
            menu.add_cascade(label="File", menu=subMenu)
            subMenu.add_separator()
            subMenu.add_command(label="Exit", command=exitmain)

            reportMenu = Menu(menu)
            menu.add_cascade(label="Report", menu=reportMenu)
            reportMenu.add_command(label="Student Report", command=student_report)
            reportMenu.add_command(label="Book Report", command=book_report)
            reportMenu.add_command(label="Book Issue Report", command=issue_report)

            toolsMenu = Menu(menu)
            menu.add_cascade(label="Tools")

            AboutMenu = Menu(menu)
            menu.add_cascade(label="About", menu=AboutMenu)
            AboutMenu.add_command(label="About us", command=self.about_from)

            # ==============================Button==============================
            book_add_button = Button(frame1, width=20, text="Entry A Book", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.book_entry)
            book_management_button = Button(frame1, width=20, text="Book Management", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.book_management)
            student_add_button = Button(frame1, width=20, text="Add A Student", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.student_add)
            student_management_button = Button(frame1, width=20, text="Student Management", fg='#fff', bg='#A38C20', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.student_management)
            issue_button = Button(frame1, width=20, text="Issue A Book", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.issue_book)
            return_button = Button(frame1, width=20, text="Return A Book", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=self.return_from)
            exit_button = Button(frame1, width=20, text="Exit", bg='#A38C20', fg='#fff', font=('times new roman', 23, 'bold italic'), bd=2, padx=2, pady=2, command=exitmain)

            book_add_button.grid(row=0, column=0)
            book_management_button.grid(row=1, column=0)
            student_add_button.grid(row=2, column=0)
            student_management_button.grid(row=3, column=0)
            issue_button.grid(row=4, column=0)
            return_button.grid(row=5, column=0)
            exit_button.grid(row=6, column=0)

            #localtime = time.asctime(time.localtime(time.time()))

            clock_label = Label(frame2, text="DIGITAL CLOCK", font=('arial', 30, 'bold'), justify=CENTER)
            clock_label.grid(row=0, column=0)





        self.mainwindow = parent
        self.mainwindow.title("Welcome To RPI Library")
        self.mainwindow.geometry('300x150+500+400')

        username_label = Label(self.mainwindow, font=('times new roman', 20, 'bold'), text="Username:")
        password_label = Label(self.mainwindow, font=('times new roman', 20, 'bold'), text="Password:")
        username_label.grid(row=0, column=0, sticky=E)
        password_label.grid(row=1, column=0, sticky=E)
        # =======================Input==============================
        username_Input = StringVar()
        password_Input = StringVar()
        username_entry = Entry(self.mainwindow, textvariable=username_Input, bd=5, bg='powder blue')
        password_entry = Entry(self.mainwindow, textvariable=password_Input, bd=5, show='*', bg='powder blue')
        username_entry.grid(row=0, column=1, pady=5, padx=10)
        password_entry.grid(row=1, column=1, pady=5, padx=10)

        # =======================Button===============================
        login_button = Button(self.mainwindow, font=('arial', 12, 'bold'), bd=1, text="Login", width=13, command=open_main_screen, activeforeground='red')
        exit_button = Button(self.mainwindow, font=('arial', 12, 'bold'), bd=1, text="Exit", width=13, activeforeground='green', command=sys.exit)
        login_button.grid(row=2, column=0, pady=10)
        exit_button.grid(row=2, column=1, pady=10)

    def onCloseOtherWindow(self, otherWindow):
        otherWindow.destroy()
        self.show()

    def show(self):
        self.mainwindow.update()
        self.mainwindow.deiconify()

    # =======================================================================================
    def book_entry(self):
        def exitbutt():
            bookentry.destroy()

        def clearfield():
            bookName_Input.set("")
            WriterNme_Input.set("")
            bookUid_Input.set("")
            NumberOfCopies_Input.set("")
            prize_Input.set("")
            publisher_Input.set("")
            bookCategory_Input.set("")

        def savedata():
            database = sqlite3.connect("LMS.sqlite")
            data = bookUid_Input.get()
            for bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory in database.execute("SELECT * FROM book_entry WHERE bookuid Like ?", (data,)):
                if bookuid == data:
                    msg = tkinter.messagebox._show('Information', 'Book already exist')
                    clearfield()
                    break
            cursor = database.execute("SELECT * FROM book_entry")
            bookname = bookName_Input.get()
            writername = WriterNme_Input.get()
            bookuid = bookUid_Input.get()
            numberofcopies = NumberOfCopies_Input.get()
            prize = prize_Input.get()
            publisher = publisher_Input.get()
            bookcategory = bookCategory_Input.get()

            cursor.execute("INSERT INTO book_entry VALUES(?, ?, ?, ?, ?, ?, ?)",
                           (bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory))
            cursor.connection.commit()
            cursor.close()
            msg = tkinter.messagebox._show('Information', 'Book saved')
        def go_to_bookmanagement():
            bookentry.destroy()
            self.book_management()

        bookentry = Toplevel()
        bookentry.title("Book Entry Form")
        #bookentry.geometry('1024x768+500+100')
        bookentry.maxsize()
        # ===================== Frame ===========================
        menu_frame = Frame(bookentry, width=1024, height=18, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Book Entry Form", font=('arial', 20, 'bold')).pack()

        frame1 = Frame(bookentry, width=100, height=750, relief='sunken')
        frame2 = Frame(bookentry, width=462, height=700, relief='sunken')
        frame3 = Frame(bookentry, width=462, height=700, relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='left')
        frame3.pack(side='right')
        # ============================== Lable and Entry =============================
        bookName = Label(frame2, width=20, text="Book Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        WriterNme = Label(frame2, width=20, text="Writer Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookUid = Label(frame2, width=20, text="Book UID", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        NumberOfCopies = Label(frame2, width=20, text="Number Of Copies", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        prize = Label(frame2, width=20, text="Price", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        publisher = Label(frame2, width=20, text="Publisher", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookCategory = Label(frame2, width=20, text="Book Category", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)

        bookName_Input = StringVar()
        WriterNme_Input = StringVar()
        bookUid_Input = IntVar()
        NumberOfCopies_Input = IntVar()
        prize_Input = IntVar()
        publisher_Input = StringVar()
        bookCategory_Input = StringVar()

        BookName_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookName_Input, bd=10)
        WriterNme_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=WriterNme_Input, bd=10)
        bookUid_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookUid_Input, bd=10)
        NumberOfCopies_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=NumberOfCopies_Input, bd=10)
        prize_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=prize_Input, bd=10)
        publisher_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=publisher_Input, bd=10)
        bookCategory_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookCategory_Input, bd=10)

        bookUid_Input.set("")
        NumberOfCopies_Input.set("")
        prize_Input.set("")

        bookName.grid(row=0, column=0, pady=2, padx=2)
        WriterNme.grid(row=1, column=0, pady=2, padx=2)
        bookUid.grid(row=2, column=0, pady=2, padx=2)
        NumberOfCopies.grid(row=3, column=0, pady=2, padx=2)
        prize.grid(row=4, column=0, pady=2, padx=2)
        publisher.grid(row=5, column=0, pady=2, padx=2)
        bookCategory.grid(row=6, column=0, pady=2, padx=2)

        BookName_entry.grid(row=0, column=1)
        WriterNme_entry.grid(row=1, column=1)
        bookUid_entry.grid(row=2, column=1)
        NumberOfCopies_entry.grid(row=3, column=1)
        prize_entry.grid(row=4, column=1)
        publisher_entry.grid(row=5, column=1)
        bookCategory_entry.grid(row=6, column=1)
        # ================================== Button =====================================
        clear_button = Button(frame3, width=10, text="Clear", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=clearfield)
        save_button = Button(frame3, width=10, text="Save", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=savedata)
        go_to_bookmanagement_button = Button(frame3, width=10, text="B M", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=go_to_bookmanagement)
        exit_button = Button(frame3, width=10, text="Exit", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=exitbutt)


        clear_button.grid(row=0, column=2, pady=12)
        save_button.grid(row=1, column=2, pady=13)
        go_to_bookmanagement_button.grid(row=2, column=2, pady=13)
        exit_button.grid(row=3, column=2, pady=10)

    def book_management(self):
        def exitbutt():
            book_management.destroy()

        def clearfield():
            bookName_Input.set("")
            WriterNme_Input.set("")
            bookUid_Input.set("")
            NumberOfCopies_Input.set("")
            prize_Input.set("")
            publisher_Input.set("")
            bookCategory_Input.set("")

        def searchdata():
            database = sqlite3.connect("LMS.sqlite")
            data = bookUid_Input.get()
            for bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory in database.execute("SELECT * FROM book_entry WHERE bookuid Like ?", (data,)):
                if bookuid == data:
                    bookName_Input.set(bookname)
                    WriterNme_Input.set(writername)
                    bookUid_Input.set(bookuid)
                    NumberOfCopies_Input.set(numberofcopies)
                    prize_Input.set(prize)
                    publisher_Input.set(publisher)
                    bookCategory_Input.set(bookcategory)
                    msg = tkinter.messagebox.showinfo('Book Information', 'Book Found')
            database.close()
        def go_to_bookentry():
            book_management.destroy()
            self.book_entry()

        def deletedata():
            answer = tkinter.messagebox.askquestion('Delete confirmation', 'Do you want to delete?')
            if answer == 'yes':
                database = sqlite3.connect("LMS.sqlite")
                data = bookUid_Input.get()
                database.execute("DELETE FROM book_entry WHERE bookuid Like ?", (data,))
                database.commit()
                msg = tkinter.messagebox.showinfo('Book Information', 'Successfully Deleted')
                database.close()
                clearfield()

        book_management = Toplevel()
        book_management.title("Book Entry From")
        #book_management.geometry('1024x768+500+100')
        book_management.maxsize()
        # ===================== Frame ===========================
        menu_frame = Frame(book_management, width=1024, height=18, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Book Management From", font=('arial', 20, 'bold')).pack()

        frame1 = Frame(book_management, width=100, height=750, relief='sunken')
        frame2 = Frame(book_management, width=462, height=700, relief='sunken')
        frame3 = Frame(book_management, width=462, height=700, relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='left')
        frame3.pack(side='right')
        # ============================== Lable and Entry =============================
        bookName = Label(frame2, width=20, text="Book Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        WriterNme = Label(frame2, width=20, text="Writer Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookUid = Label(frame2, width=20, text="Book UID", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        NumberOfCopies = Label(frame2, width=20, text="Number Of Copies", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        prize = Label(frame2, width=20, text="Prize", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        publisher = Label(frame2, width=20, text="Publisher", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookCategory = Label(frame2, width=20, text="Book Category", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        control = Label(frame3, width=10, text="Controls", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2)

        bookName_Input = StringVar()
        WriterNme_Input = StringVar()
        bookUid_Input = IntVar()
        NumberOfCopies_Input = IntVar()
        prize_Input = IntVar()
        publisher_Input = StringVar()
        bookCategory_Input = StringVar()

        BookName_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookName_Input, bd=10)
        WriterNme_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=WriterNme_Input, bd=10)
        bookUid_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookUid_Input, bd=10)
        NumberOfCopies_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=NumberOfCopies_Input, bd=10)
        prize_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=prize_Input, bd=10)
        publisher_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=publisher_Input, bd=10)
        bookCategory_entry = Entry(frame2, font=('arial', 12, 'bold'), bg='#CCCCCC', fg='#000000', textvariable=bookCategory_Input, bd=10)

        bookUid_Input.set("")
        NumberOfCopies_Input.set("")
        prize_Input.set("")

        bookName.grid(row=0, column=0, padx=2, pady=2)
        WriterNme.grid(row=1, column=0, padx=2, pady=2)
        bookUid.grid(row=2, column=0, padx=2, pady=2)
        NumberOfCopies.grid(row=3, column=0, padx=2, pady=2)
        prize.grid(row=4, column=0, padx=2, pady=2)
        publisher.grid(row=5, column=0, padx=2, pady=2)
        bookCategory.grid(row=6, column=0, padx=2, pady=2)
        control.grid(row=0, column=0, padx=2, pady=2)

        BookName_entry.grid(row=0, column=1)
        WriterNme_entry.grid(row=1, column=1)
        bookUid_entry.grid(row=2, column=1)
        NumberOfCopies_entry.grid(row=3, column=1)
        prize_entry.grid(row=4, column=1)
        publisher_entry.grid(row=5, column=1)
        bookCategory_entry.grid(row=6, column=1)
        # ================================== Button =====================================
        search_button = Button(frame3, width=11, text="Search",bg='#BDCCD4',  font=('times new roman', 23, 'bold'), bd=2, command=searchdata)
        clear_button = Button(frame3, width=11, text="Clear",bg='#BDCCD4',  font=('times new roman', 23, 'bold'), bd=2, command=clearfield)
        delete_button = Button(frame3, width=11, text="Delete",bg='#BDCCD4',  font=('times new roman', 23, 'bold'), bd=2, command=deletedata)
        go_to_bookentry_button = Button(frame3, width=11, text="Book Entry",bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=go_to_bookentry)
        exit_button = Button(frame3, width=11, text="Exit",bg='#BDCCD4',  font=('times new roman', 23, 'bold'), bd=2, command=exitbutt)

        search_button.grid(row=1, column=0)
        clear_button.grid(row=2, column=0)
        delete_button.grid(row=4, column=0)
        go_to_bookentry_button.grid(row=5, column=0)
        exit_button.grid(row=6, column=0)

    def student_add(self):
        def exitbutt():
            studentadd.destroy()

        def savedata():
            database = sqlite3.connect("LMS.sqlite")
            cursor = database.execute("SELECT * FROM student_add")
            data = roll_Input.get()
            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (data,)):
                if roll == data:
                    msg = tkinter.messagebox.showinfo('Student Information', 'Student already exist')
                    cleardata()
                    break
            studentname = studentName_Input.get()
            address = address_Input.get()
            phoneno = phone_no_Input.get()
            roll = roll_Input.get()
            department = department_Input.get()
            semester = semester_Input.get()
            shift = shift_Input.get()
            date = dateformat()

            d = day_Input.get()
            m = month_Input.get()
            if int(d) >31:
                tkinter.messagebox.showinfo('Student Information', 'Date is not correct')
            elif int(m) >12:
                tkinter.messagebox.showinfo('Student Information', 'Month is not correct')
            else:
                bookonhand = 0
                cursor.execute("INSERT INTO student_add VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (studentname, address, phoneno, roll, department, semester, shift, date, bookonhand))
                cursor.connection.commit()
                cursor.close()
                tkinter.messagebox.showinfo('Student Information', 'Save Successfully')

        def cleardata():
            studentName_Input.set("")
            address_Input.set("")
            phone_no_Input.set("")
            roll_Input.set("")
            department_Input.set("")
            semester_Input.set("")
            shift_Input.set("")
            day_Input.set(0)
            month_Input.set(0)
            year_Input.set(2000)
            photo = PhotoImage(file='student_image.png')
            lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)


        def dateformat():
            d = day_Input.get()
            m = month_Input.get()
            y = year_Input.get()
            date_Input = d + '/' + m + '/' + y
            return date_Input

        def searchdata():
            database = sqlite3.connect("LMS.sqlite")
            data = roll_Input.get()
            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (data,)):
                if roll == data:
                    studentName_Input.set(studentname)
                    address_Input.set(address)
                    phone_no_Input.set(phoneno)
                    roll_Input.set(roll)
                    department_Input.set(department)
                    semester_Input.set(semester)
                    shift_Input.set(shift)
                    dateformat().set(date)
            database.close()

        def student_image():
            con = sqlite3.connect('imagedb.sqlite')
            cur = con.cursor()

            image_id = roll_Input.get()
            image_location = filedialog.askopenfilename()
            cur.execute("INSERT INTO image (id, name) VALUES(?, ?)", (image_id, image_location))

            photo = PhotoImage(file=image_location)
            lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)
            cur.connection.commit()
            cur.close()

        def go_to_student_management():
            studentadd.destroy()
            self.student_management()

        studentadd = Toplevel()
        studentadd.title("Student Add From")
        #studentadd.geometry('1024x768+500+100')
        studentadd.maxsize()

        #===================== Frame ===========================
        menu_frame = Frame(studentadd, width=1024, height=18, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Student Add From", font=('arial', 20, 'bold') ).pack()

        frame1 = Frame(studentadd, width=100, height=750, relief='sunken')
        frame2 = Frame(studentadd, width=462, height=700, relief='sunken')
        frame3 = Frame(studentadd, width=462, height=700, relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='left')
        frame3.pack(side='right')
        #============================== Lable=============================
        studentName = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Student Name:", font=('times new roman', 23, 'bold'), bd=2)
        address = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Address:", font=('times new roman', 23, 'bold'), bd=2)
        phone_no = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Phone No:", font=('times new roman', 23, 'bold'), bd=2)
        roll = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Roll:", font=('times new roman', 23, 'bold'), bd=2)
        department = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Department:", font=('times new roman', 23, 'bold'), bd=2)
        semester = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Semester:", font=('times new roman', 23, 'bold'), bd=2)
        shift = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Shift:", font=('times new roman', 23, 'bold'), bd=2)
        date = Label(frame2, width=20, bg='#666666', fg='#ffffff', text="Date:", font=('times new roman', 23, 'bold'), bd=2)
        control = Label(frame3, width=12, text="Controls", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2)

        studentName_Input = StringVar()
        address_Input = StringVar()
        phone_no_Input = StringVar()
        roll_Input = IntVar()
        department_Input = StringVar()
        semester_Input = StringVar()
        shift_Input = StringVar()
        day_Input = StringVar()
        month_Input = StringVar()
        year_Input = StringVar()

        #==============================Entry and combobox =============================
        studentName_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=studentName_Input, bd=10)
        address_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=address_Input, bd=10)
        phone_no_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=phone_no_Input, bd=10)
        roll_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=roll_Input, bd=10)
        department_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=department_Input, value='Computer Civil Electrical Electronics Mechanical Power Elector-Mechanical Mechatonics ')
        semester_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=semester_Input, value='1st 2nd 3rd 4th 5th 6th 7th')
        shift_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=shift_Input, value='1st 2nd')

        date_frame = Frame(frame2)

        daty_label = Label(date_frame, width=5, text="Day", font=('times new roman', 12, 'bold'), bd=2)
        month_label = Label(date_frame, width=5, text="Month", font=('times new roman', 12, 'bold'), bd=2)
        year_label = Label(date_frame, width=8, text="Year", font=('times new roman', 12, 'bold'), bd=2)

        date_spinbox = Spinbox(date_frame, width=4, buttonup=RAISED, textvariable=day_Input, from_=0, to=31)
        date_month = Spinbox(date_frame, width=4, buttonup=RAISED, textvariable=month_Input, from_=0, to=12)
        date_year = Spinbox(date_frame, width=8, buttonup=RAISED, textvariable=year_Input, from_=2000, to=2099)

        daty_label.grid(row=0, column=0)
        month_label.grid(row=0, column=1)
        year_label.grid(row=0, column=2)

        date_spinbox.grid(row=1, column=0)
        date_month.grid(row=1, column=1)
        date_year.grid(row=1, column=2)

        roll_Input.set("")

        studentName.grid(row=0, column=0, padx=2, pady=2)
        address.grid(row=1, column=0, padx=2, pady=2)
        phone_no.grid(row=2, column=0, padx=2, pady=2)
        roll.grid(row=3, column=0, padx=2, pady=2)
        department.grid(row=4, column=0, padx=2, pady=2)
        semester.grid(row=5, column=0, padx=2, pady=2)
        shift.grid(row=6, column=0, padx=2, pady=2)
        date.grid(row=7, column=0, padx=2, pady=2)

        studentName_entry.grid(row=0, column=1)
        address_entry.grid(row=1, column=1)
        phone_no_entry.grid(row=2, column=1)
        roll_entry.grid(row=3, column=1)
        department_combobox.grid(row=4, column=1)
        semester_combobox.grid(row=5, column=1)
        shift_combobox.grid(row=6, column=1)
        date_frame.grid(row=7, column=1)
        #================================== Button =====================================
        clear_button = Button(frame3, width=10, text="Clear", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=cleardata)
        save_button = Button(frame3, width=10, text="Save", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=savedata)
        student_management_button = Button(frame3, width=10, bg='#BDCCD4', text="S M", font=('times new roman', 23, 'bold'), bd=2, command=go_to_student_management)
        exit_button = Button(frame3, width=10, text="Exit",  bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=exitbutt)
        image_button = Button(frame3, width=10, text="Browse", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=student_image)
        #================================== Image Button ==========================================================

        lbl_frame = Frame(frame3, width=200, height=200, bg='pink')
        photo = PhotoImage(file='student_image.png')
        lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
        lbl_img.image = photo
        lbl_img.grid(row=0, column=0)





        lbl_frame.grid(row=0, column=1)
        control.grid(row=1, column=1)
        image_button.grid(row=2, column=1)
        clear_button.grid(row=3, column=1)
        save_button.grid(row=4, column=1)
        student_management_button.grid(row=5, column=1)
        exit_button.grid(row=6, column=1)

    def student_management(self):

        def exitbutt():
            student_management.destroy()

        def cleardata():
            studentName_Input.set("")
            address_Input.set("")
            phone_no_Input.set("")
            roll_Input.set("")
            department_Input.set("")
            semester_Input.set("")
            shift_Input.set("")
            date_Input.set("")
            photo = PhotoImage(file='student_image.png')
            lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)


        def deletedata():
            answer = tkinter.messagebox.askquestion('Delete confirmation', 'Do you want to delete?')
            if answer == 'yes':
                database = sqlite3.connect("LMS.sqlite")
                data = roll_Input.get()

                database.execute("DELETE FROM student_add WHERE roll Like ?", (data,))

                con = sqlite3.connect('imagedb.sqlite')
                con.execute("DELETE FROM image WHERE id Like ?", (data,))

                database.commit()
                con.commit()
                database.close()
                con.close()
                msg = tkinter.messagebox.showinfo('Student Information', 'Successfully Deleted')
                cleardata()

        def editdata():
            database = sqlite3.connect("LMS.sqlite")
            data = roll_Input.get()
            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (data,)):
                if roll == data:
                    studentname = studentName_Input.get()
                    address = address_Input.get()
                    phoneno = phone_no_Input.get()
                    roll = roll_Input.get()
                    department = department_Input.get()
                    semester = semester_Input.get()
                    shift = shift_Input.get()
                    date = date_Input.get()

                    database.execute("UPDATE student_add SET studentname = ? WHERE (roll = ?) ", (studentname, data))
                    database.execute("UPDATE student_add SET address = ? WHERE (roll = ?) ", (address, data))
                    database.execute("UPDATE student_add SET phoneno = ? WHERE (roll = ?) ", (phoneno, data))
                    database.execute("UPDATE student_add SET roll = ? WHERE (roll = ?) ", (roll, data))
                    database.execute("UPDATE student_add SET department = ? WHERE (roll = ?) ", (department, data))
                    database.execute("UPDATE student_add SET semester = ? WHERE (roll = ?) ", (semester, data))
                    database.execute("UPDATE student_add SET shift = ? WHERE (roll = ?) ", (shift, data))
                    database.execute("UPDATE student_add SET date = ? WHERE (roll = ?) ", (date, data))
                    database.commit()
            msg = tkinter.messagebox.showinfo('Student Information', 'Successfully Updated')
            database.close()

        def searchdata():
            database = sqlite3.connect("LMS.sqlite")
            data = roll_Input.get()
            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (data,)):
                if roll == data:
                    studentName_Input.set(studentname)
                    address_Input.set(address)
                    phone_no_Input.set(phoneno)
                    roll_Input.set(roll)
                    department_Input.set(department)
                    semester_Input.set(semester)
                    shift_Input.set(shift)
                    date_Input.set(date)
            database.close()

            student_image()

        def student_image():
            con = sqlite3.connect('imagedb.sqlite')
            cur = con.cursor()
            image_id = roll_Input.get()

            for id, name in con.execute("SELECT * FROM image WHERE id Like ?", (image_id,)):
                if id == image_id:
                    photo = PhotoImage(file=name)
                    lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
                    lbl_img.image = photo
                    lbl_img.grid(row=0, column=0)
            cur.close()


        def go_to_student_add():
            student_management.destroy()
            self.student_add()

        student_management = Toplevel()
        student_management.title("Student Add From")
        #student_management.geometry('1024x768+500+100')
        student_management.maxsize()
        #===================== Frame ===========================
        menu_frame = Frame(student_management, width=1024, height=18, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Student Management From", font=('arial', 20, 'bold') ).pack()

        frame1 = Frame(student_management, width=100, height=750, relief='sunken')
        frame2 = Frame(student_management, width=462, height=700, relief='sunken')
        frame3 = Frame(student_management, width=462, height=700, relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='left')
        frame3.pack(side='right')
        #============================== Lable and Entry =============================
        studentName = Label(frame2, width=20, text="Student Name:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        address = Label(frame2, width=20, text="Address:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        phone_no = Label(frame2, width=20, text="Phone No:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        roll = Label(frame2, width=20, text="Roll:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        department = Label(frame2, width=20, text="Department:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        semester = Label(frame2, width=20, text="semester:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        shift = Label(frame2, width=20, text="shift:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        date = Label(frame2, width=20, text="date:", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        control = Label(frame3, width=12, text="Controls", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2)

        studentName_Input = StringVar()
        address_Input = StringVar()

        phone_no_Input = StringVar()
        roll_Input = IntVar()
        department_Input = StringVar()
        semester_Input = StringVar()
        shift_Input = StringVar()
        date_Input = StringVar()


        studentName_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=studentName_Input, bd=10)
        address_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=address_Input, bd=10)
        phone_no_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=phone_no_Input, bd=10)
        roll_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=roll_Input, bd=5)
        department_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=department_Input, value='Computer Civil Electrical Electronics Mechanical Power Elector-Mechanical Mechatonics ')
        semester_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=semester_Input, value='1st 2nd 3rd 4th 5th 6th 7th')
        shift_combobox = Combobox(frame2, font=('arial', 12, 'bold'), textvariable=shift_Input, value='1st 2nd')
        date_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=date_Input, bd=10)

        roll_Input.set("")

        studentName.grid(row=0, column=0, padx=2, pady=2)
        address.grid(row=1, column=0, padx=2, pady=2)
        phone_no.grid(row=2, column=0, padx=2, pady=2)
        roll.grid(row=3, column=0, padx=2, pady=2)
        department.grid(row=4, column=0, padx=2, pady=2)
        semester.grid(row=5, column=0, padx=2, pady=2)
        shift.grid(row=6, column=0, padx=2, pady=2)
        date.grid(row=7, column=0, padx=2, pady=2)

        studentName_entry.grid(row=0, column=1)
        address_entry.grid(row=1, column=1)
        phone_no_entry.grid(row=2, column=1)
        roll_entry.grid(row=3, column=1)
        department_combobox.grid(row=4, column=1)
        semester_combobox.grid(row=5, column=1)
        shift_combobox.grid(row=6, column=1)
        date_entry.grid(row=7, column=1)
        #================================== Button =====================================
        search_button = Button(frame3, width=10, text="Search", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=searchdata)
        clear_button = Button(frame3, width=10, text="Clear", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=cleardata)
        delete_button = Button(frame3, width=10, text="Delete", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=deletedata)
        edit_button = Button(frame3, width=10, text="Update", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=editdata)
        go_to_student_add_button = Button(frame3, width=10, bg='#BDCCD4', text="S A", font=('times new roman', 23, 'bold'), bd=2, command=go_to_student_add)
        exit_button = Button(frame3, width=10, text="Exit", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=exitbutt)
        #================================== Image Button ==========================================================

        lbl_frame = Frame(frame3, width=200, height=200, bg='pink')
        photo = PhotoImage(file='student_image.png')
        lbl_img = Label(lbl_frame, width=200, height=250, image=photo)
        lbl_img.image = photo
        lbl_img.grid(row=0, column=0)


        lbl_frame.grid(row=0, column=1)
        control.grid(row=1, column=1)
        search_button.grid(row=2, column=1)
        clear_button.grid(row=3, column=1)
        delete_button.grid(row=4, column=1)
        edit_button.grid(row=5, column=1)
        go_to_student_add_button.grid(row=6, column=1)
        exit_button.grid(row=7, column=1)

    def issue_book(self):
        def exitbutt():
            bookissue.destroy()

        def cleardata():
            studentName_Input.set("")
            roll_Input.set("")
            bookName_Input.set("")
            writerName_Input.set("")
            bookUid_Input.set("")
            prize_Input.set("")
            publisher_Input.set("")
            issueDate_Input.set("")
            returnDate_Input.set("")
            day_Input.set(0)
            month_Input.set(0)
            year_Input.set(2000)
            day_Input2.set(0)
            month_Input2.set(0)
            year_Input2.set(2000)

        def searchdata_roll():
            database = sqlite3.connect("LMS.sqlite")
            data = roll_Input.get()
            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (data,)):
                if roll == data:
                    studentName_Input.set(studentname)
                    roll_Input.set(roll)
            database.close()

        def searchdata_book():
            database = sqlite3.connect("LMS.sqlite")
            data2 = bookUid_Input.get()
            for bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory in database.execute("SELECT * FROM book_entry WHERE bookuid Like ?", (data2,)):
                if bookuid == data2:
                    bookName_Input.set(bookname)
                    writerName_Input.set(writername)
                    bookUid_Input.set(bookuid)
                    prize_Input.set(prize)
                    publisher_Input.set(publisher)
            database.close()

        def issuebook():
            database = sqlite3.connect("LMS.sqlite")

            databook = bookUid_Input.get()
            datastudent = roll_Input.get()
            d = day_Input.get()
            m = month_Input.get()

            d2 = day_Input2.get()
            m2 = month_Input2.get()


            if int(d) >31:
                tkinter.messagebox.showinfo('Student Information', 'Date is not correct')
            elif int(m) >12:
                tkinter.messagebox.showinfo('Student Information', 'Month is not correct')
            elif int(d2) >31:
                tkinter.messagebox.showinfo('Student Information', 'Date is not correct')
            elif int(m2) >12:
                tkinter.messagebox.showinfo('Student Information', 'Month is not correct')
            else:
                for bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory in database.execute("SELECT * FROM book_entry WHERE bookuid Like ?", (databook,)):
                    if bookuid == databook:
                        if numberofcopies <=0:
                            tkinter.messagebox.showinfo('Book Information', 'Book out of stock !')
                            cleardata()
                            break
                        else:
                            newbookvalue = numberofcopies - 1

                            database.execute("UPDATE book_entry SET numberofcopies = ? WHERE (bookuid = ?) ", (newbookvalue, databook))
                            database.commit()

                            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (datastudent,)):
                                if roll == datastudent:
                                    if bookonhand >= 2:
                                        tkinter.messagebox.showinfo('Issue Information', 'You reach maximum book laval on hand !')
                                        cleardata()
                                        break
                                    else:
                                        newstudentvalue = bookonhand + 1
                                        database.execute("UPDATE student_add SET bookonhand = ? WHERE (roll = ?) ", (newstudentvalue, datastudent))

                                        cursor = database.execute("SELECT * FROM issuebook")
                                        studentname = studentName_Input.get()
                                        roll = roll_Input.get()
                                        bookname = bookName_Input.get()
                                        writername = writerName_Input.get()
                                        bookuid = bookUid_Input.get()
                                        prize = prize_Input.get()
                                        publisher = publisher_Input.get()
                                        issuedate = dateformat()
                                        returndate = dateformat2()

                                        cursor.execute("INSERT INTO issuebook VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                                       (studentname, roll, bookname, writername, bookuid, prize, publisher, issuedate, returndate))
                                        cursor.connection.commit()
                                        tkinter.messagebox.showinfo('Book Information', 'Successfully Issued')

            database.commit()
            database.close()


        def dateformat():
            d = day_Input.get()
            m = month_Input.get()
            y = year_Input.get()
            date_Input = d + '/' + m + '/' + y
            return date_Input

        def dateformat2():
            d = day_Input2.get()
            m = month_Input2.get()
            y = year_Input2.get()
            date_Input2 = d + '/' + m + '/' + y
            return date_Input2

        def savedata():
            database = sqlite3.connect("LMS.sqlite")
            cursor = database.execute("SELECT * FROM issuebook")
            studentname = studentName_Input.get()
            roll = roll_Input.get()
            bookname = bookName_Input.get()
            writername = writerName_Input.get()
            bookuid = bookUid_Input.get()
            prize = prize_Input.get()
            publisher = publisher_Input.get()
            issuedate = dateformat()
            returndate = dateformat2()

            cursor.execute("INSERT INTO issuebook VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                           (studentname, roll, bookname, writername, bookuid, prize, publisher, issuedate, returndate))
            cursor.connection.commit()
            cursor.close()

        bookissue = Toplevel()
        bookissue.title("Book Issue From")
        #bookissue.geometry('1024x768+500+100')
        bookissue.maxsize()
        #===================== Frame ===========================
        menu_frame = Frame(bookissue, width=1024, height=18, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Book Issue From", font=('arial', 20, 'bold') ).pack()

        frame1 = Frame(bookissue, width=100, height=750, relief='sunken')
        frame2 = Frame(bookissue, width=462, height=700, relief='sunken')
        frame3 = Frame(bookissue, width=462, height=700, bg='red', relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='left')
        frame3.pack(side='right')
        #============================== Lable and Entry =============================
        studentName = Label(frame2, width=20, text="Student Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        roll = Label(frame2, width=20, text="Roll", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookName = Label(frame2, width=20, text="Book Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        WriterNme = Label(frame2, width=20, text="Writer Name", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookUid = Label(frame2, width=20, text="Book UID", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        prize = Label(frame2, width=20, text="Price", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        publisher = Label(frame2, width=20, text="Publisher", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        issueDate = Label(frame2, width=20, text="Issue Date", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        returnDate = Label(frame2, width=20, text="return Date", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)

        studentName_Input = StringVar()
        roll_Input = IntVar()
        bookName_Input = StringVar()
        writerName_Input = StringVar()
        bookUid_Input = IntVar()
        prize_Input = IntVar()
        publisher_Input = StringVar()
        issueDate_Input = StringVar()
        returnDate_Input = StringVar()
        day_Input = StringVar()
        month_Input = StringVar()
        year_Input = StringVar()

        day_Input2 = StringVar()
        month_Input2 = StringVar()
        year_Input2 = StringVar()

        studentName_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=studentName_Input, bd=10)
        roll_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=roll_Input, bd=10)
        bookName_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=bookName_Input, bd=10)
        WriterNme_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=writerName_Input, bd=10)
        bookUid_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=bookUid_Input, bd=10)
        prize_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=prize_Input, bd=10)
        publisher_entry = Entry(frame2, font=('arial', 12, 'bold'), textvariable=publisher_Input, bd=10)


#============================================== Date spinbox ============================================================
        issueDate_frame = Frame(frame2)

        daty_label = Label(issueDate_frame, width=5, text="Day", font=('times new roman', 12, 'bold'), bd=2)
        month_label = Label(issueDate_frame, width=5, text="Month", font=('times new roman', 12, 'bold'), bd=2)
        year_label = Label(issueDate_frame, width=8, text="Year", font=('times new roman', 12, 'bold'), bd=2)

        date_spinbox = Spinbox(issueDate_frame, width=4, buttonup=RAISED, textvariable=day_Input, from_=0, to=31)
        date_month = Spinbox(issueDate_frame, width=4, buttonup=RAISED, textvariable=month_Input, from_=0, to=12)
        date_year = Spinbox(issueDate_frame, width=8, buttonup=RAISED, textvariable=year_Input, from_=2000, to=2099)

        daty_label.grid(row=0, column=0)
        month_label.grid(row=0, column=1)
        year_label.grid(row=0, column=2)

        date_spinbox.grid(row=1, column=0)
        date_month.grid(row=1, column=1)
        date_year.grid(row=1, column=2)

        returnDate_frame = Frame(frame2)
        daty_label = Label(returnDate_frame, width=5, text="Day", font=('times new roman', 12, 'bold'), bd=2)
        month_label = Label(returnDate_frame, width=5, text="Month", font=('times new roman', 12, 'bold'), bd=2)
        year_label = Label(returnDate_frame, width=8, text="Year", font=('times new roman', 12, 'bold'), bd=2)

        date_spinbox = Spinbox(returnDate_frame, width=4, buttonup=RAISED, textvariable=day_Input2, from_=0, to=31)
        date_month = Spinbox(returnDate_frame, width=4, buttonup=RAISED, textvariable=month_Input2, from_=0, to=12)
        date_year = Spinbox(returnDate_frame, width=8, buttonup=RAISED, textvariable=year_Input2, from_=2000, to=2099)

        daty_label.grid(row=0, column=0)
        month_label.grid(row=0, column=1)
        year_label.grid(row=0, column=2)

        date_spinbox.grid(row=1, column=0)
        date_month.grid(row=1, column=1)
        date_year.grid(row=1, column=2)


        roll_Input.set("")
        bookUid_Input.set("")
        prize_Input.set("")

        studentName.grid(row=0, column=0, padx=2, pady=2)
        roll.grid(row=1, column=0, padx=2, pady=2)
        bookName.grid(row=2, column=0, padx=2, pady=2)
        WriterNme.grid(row=3, column=0, padx=2, pady=2)
        bookUid.grid(row=4, column=0, padx=2, pady=2)
        prize.grid(row=5, column=0, padx=2, pady=2)
        publisher.grid(row=6, column=0, padx=2, pady=2)
        issueDate.grid(row=7, column=0, padx=2, pady=2)
        returnDate.grid(row=8, column=0, padx=2, pady=2)

        studentName_entry.grid(row=0, column=1)
        roll_entry.grid(row=1, column=1)
        bookName_entry.grid(row=2, column=1)
        WriterNme_entry.grid(row=3, column=1)
        bookUid_entry.grid(row=4, column=1)
        prize_entry.grid(row=5, column=1)
        publisher_entry.grid(row=6, column=1)
        issueDate_frame.grid(row=7, column=1)
        returnDate_frame.grid(row=8, column=1)

        #================================== Button =====================================
        searchrool_button = Button(frame3, width=10, text="Search Roll", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=searchdata_roll)
        searchbookuid_button = Button(frame3, width=10, text="Search Book", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=searchdata_book)
        clear_button = Button(frame3, width=10, text="Clear", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=cleardata)
        save_button = Button(frame3, width=10, text="Save", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=savedata)
        issue_button = Button(frame3, width=10, text="Issue", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=issuebook)
        exit_button = Button(frame3, width=10, text="Exit", bg='#BDCCD4', font=('times new roman', 23, 'bold'), bd=2, command=exitbutt)

        searchrool_button.grid(row=0, column=1)
        searchbookuid_button.grid(row=1, column=1)
        clear_button.grid(row=2, column=1)
        save_button.grid(row=3, column=1)
        issue_button.grid(row=4, column=1)
        exit_button.grid(row=5, column=1)

    def return_from(self):
        def exitreturnbook():
            returnbook.destroy()


        def cleardata():
            roll_Input.set("")
            bookUid_Input.set("")
            returndate_Input.set("")
            fine_Input.set("")
            rate_Input.set("")
            day_Input.set(0)
            month_Input.set(0)
            year_Input.set(2017)

        def bookreturn():

            database = sqlite3.connect("LMS.sqlite")

            databook = bookUid_Input.get()
            datastudent = roll_Input.get()

            for studentname, address, phoneno, roll, department, semester, shift, date, bookonhand in database.execute("SELECT * FROM student_add WHERE roll Like ?", (datastudent,)):
                if roll == datastudent:
                    if bookonhand <=0:
                        tkinter.messagebox.showinfo('Book Information', 'No Book on hand !')
                    else:
                        newstudentvalue = bookonhand - 1
                        database.execute("UPDATE student_add SET bookonhand = ? WHERE (roll = ?) ", (newstudentvalue, datastudent))

                        for bookname, writername, bookuid, numberofcopies, prize, publisher, bookcategory in database.execute("SELECT * FROM book_entry WHERE bookuid Like ?", (databook,)):
                            if bookuid == databook:
                                newbookvalue = numberofcopies + 1

                                database.execute("UPDATE book_entry SET numberofcopies = ? WHERE (bookuid = ?) ", (newbookvalue, databook))
                                database.commit()
                                tkinter.messagebox.showinfo('Book Information', 'Book successfully returned')
                                cleardata()

            database.commit()
            database.close()


        def finecalculation():
            database = sqlite3.connect("LMS.sqlite")
            databook = bookUid_Input.get()
            rate = rate_Input.get()
            for studentname, roll, bookname, writername, bookuid, prize, publisher, issuedate, returndate in database.execute("SELECT * FROM issuebook WHERE bookuid Like ?", (databook,)):
                if bookuid == databook:
                    date_format = "%d/%m/%Y"
                    date_stat = returndate
                    date_end = dateformat()
                    date_start = datetime.strptime(date_stat, date_format)
                    date_end = datetime.strptime(date_end, date_format)
                    fine = date_end - date_start
                    fine_Input.set(fine.days*rate)

        def dateformat():
            d = day_Input.get()
            m = month_Input.get()
            y = year_Input.get()
            date_Input = d + '/' + m + '/' + y
            return date_Input

        returnbook = Toplevel()
        returnbook.title("Return Book From")
        #returnbook.geometry('650x380+600+300')
        returnbook.maxsize()

        menu_frame = Frame(returnbook, width=550, height=50, bg='pink', relief='sunken')
        menu_frame.pack(side='top')
        text_LMS = Label(menu_frame, text="Book Return From", font=('arial', 20, 'bold') ).pack()

        frame1 = Frame(returnbook, width=50, height=700, relief='sunken')
        frame2 = Frame(returnbook, width=500, height=700, relief='sunken')
        frame1.pack(side='left')
        frame2.pack(side='right')
        #============================== Lable and Entry =============================
        roll = Label(frame2, width=20, text="Roll", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        bookUid = Label(frame2, width=20, text="Book Uid", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        returndate = Label(frame2, width=20, text="Return Date", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)
        fine = Label(frame2, width=20, text="Fine", bg='#666666', fg='#ffffff',font=('times new roman', 23, 'bold'), bd=2)
        rate = Label(frame2, width=20, text="Rate", bg='#666666', fg='#ffffff', font=('times new roman', 23, 'bold'), bd=2)

        roll_Input = IntVar()
        bookUid_Input = IntVar()
        returndate_Input = StringVar()
        fine_Input = IntVar()
        rate_Input = IntVar()

        roll_entry = Entry(frame2, font=('times new roman', 18, 'bold'), textvariable=roll_Input, bd=10)
        bookUid_entry = Entry(frame2, font=('times new roman', 18, 'bold'), textvariable=bookUid_Input, bd=10)
        fine_entry = Entry(frame2,font=('times new roman', 18, 'bold'), textvariable=fine_Input, bd=10)
        rate_entry = Entry(frame2,font=('times new roman', 18, 'bold'), textvariable=rate_Input, bd=10)

        day_Input = StringVar()
        month_Input = StringVar()
        year_Input = StringVar()

        date_frame = Frame(frame2)
        date_spinbox = Spinbox(date_frame, width=4, buttonup=RAISED, bg='#CCCCCC', fg='#000000', textvariable=day_Input, from_=0, to=31)
        date_month = Spinbox(date_frame, width=4, buttonup=RAISED, bg='#CCCCCC', fg='#000000', textvariable=month_Input, from_=0, to=12)
        date_year = Spinbox(date_frame, width=8, buttonup=RAISED, bg='#CCCCCC', fg='#000000', textvariable=year_Input, from_=2017, to=2099)
        date_spinbox.grid(row=0, column=0)
        date_month.grid(row=0, column=1)
        date_year.grid(row=0, column=2)



        roll_Input.set("")
        bookUid_Input.set("")
        returndate_Input.set("")
        fine_Input.set("")
        rate_Input.set("")

        roll.grid(row=0, column=0)
        bookUid.grid(row=1, column=0)
        returndate.grid(row=2, column=0)
        rate.grid(row=3, column=0)
        fine.grid(row=4, column=0)
        button_frame = Frame(frame2)
        button_frame.grid(row=5, columnspan=2)

        roll_entry.grid(row=0, column=1)
        bookUid_entry.grid(row=1, column=1)
        date_frame.grid(row=2, column=1)
        rate_entry.grid(row=3, column=1)
        fine_entry.grid(row=4, column=1)

        #=========================== Button ============================================
        returnButton = Button(button_frame, width=10, text="Return", bg='#BDCCD4', font=('arial', 20, 'bold'), bd=2, command=bookreturn)
        close = Button(button_frame, width=10, text="close", bg='#BDCCD4', font=('arial', 20, 'bold'), bd=2, command=exitreturnbook)
        fine = Button(button_frame, width=10, text="Fine", bg='#BDCCD4', font=('arial', 20, 'bold'), bd=2, command=finecalculation)



        returnButton.grid(row=0, column=0)
        fine.grid(row=0, column=1)
        close.grid(row=0, column=2)

    def about_from(self):

        def cleardata():
            studentName_Input.set("")
            roll_Input.set("")
            department_Input.set("")
            shift_Input.set("")
            semester_Input.set("")

        def touhid():

            name = "Touhidur Rahman"
            roll = "Roll: 808516"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file='image\Touhid.png')
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def subrato():
            cleardata()
            name = "Subroto Roy"
            roll = "Roll: 868199"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = 'image\Touhid.png')
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def rumiyea():
            cleardata()
            name = "Rumiyea Bosori"
            roll = "Roll: 809795"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Rumia Bashori.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)


        def raisul():
            cleardata()
            name = "Raisul Islam"
            roll = "Roll: 808505"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Rumia Bashori.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def tanisa():
            cleardata()
            name = "Tanisa Khatun"
            roll = "Roll: 808525"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Tanisha.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def momin():
            cleardata()
            name = "Abdul Momin "
            roll = "Roll: 809793"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Momin.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def aisha():
            cleardata()
            name = "Aisha Khatun"
            roll = "Roll: 809788"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "aisha.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def ripon():
            cleardata()
            name = "Ripon Ali"
            roll = "Roll: 809776"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\momin.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def rakibul():
            cleardata()
            name = "Rakibul Islam"
            roll = "Roll: 817927"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"

            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Momin.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        def mukti():
            cleardata()
            name = "Asmaul Husna Mukti"
            roll = "Roll: 809785"
            department = "Department: Computer"
            shift = "Shift: 1st"
            semester = "Semester: 7th"


            studentName_Input.set(name)
            roll_Input.set(roll)
            department_Input.set(department)
            shift_Input.set(shift)
            semester_Input.set(semester)

            photo = PhotoImage(file = "image\Asha.png")
            lbl_img = Label(image_frame, width=200, height=250, image=photo)
            lbl_img.image = photo
            lbl_img.grid(row=0, column=0)

        about = Toplevel()
        about.title("About US")
        about.geometry("800x650+500+300")
        Label(about, text="ABOUT US", font=('arial', 20, 'bold')).pack(side='top')

        frame1 = Frame(about, width=600, height=430, relief='sunken')
        frame1.pack(side='top')
        frame2 = Frame(about, width=300, height=350)
        frame2.pack(side='bottom')
        image_frame = Frame(about, width=200, height=250)
        image_frame.pack(side='top')

        touhid_button = Button(frame1, text="Touhid", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='green', bd=2, command=touhid)
        subrato_button = Button(frame1, text="Subrato", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='pink', bd=2, command=subrato)
        raisul_button = Button(frame1, text="Raisul", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='blue', bd=2, command=raisul)
        rumiyea_button = Button(frame1, text="rumia", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='red', bd=2, command=rumiyea)
        tanisa_button = Button(frame1, text="Tanisa", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='blue', bd=2, command=tanisa)
        momin_button = Button(frame1, text="Momin", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='green', bd=2, command=momin)
        aisha_button = Button(frame1, text="Aisha", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='pink', bd=2, command=aisha)
        ripon_button = Button(frame1, text="Ripon", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='blue', bd=2, command=ripon)
        rakibul_button = Button(frame1, text="Rakibul", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='brown', bd=2, command=rakibul)
        mukti_button = Button(frame1, text="Mukti", width=20, font=('times new roman', 12, 'bold italic'), activeforeground='green', bd=2, command=mukti)

        touhid_button.grid(row=0, column=0)
        subrato_button.grid(row=0, column=1)
        raisul_button.grid(row=0, column=2)
        rumiyea_button.grid(row=0, column=3)

        tanisa_button.grid(row=1, column=0)
        momin_button.grid(row=1, column=1)
        aisha_button.grid(row=1, column=2)
        ripon_button.grid(row=1, column=3)

        rakibul_button.grid(row=2, column=1)
        mukti_button.grid(row=2, column=2)

        studentName_Input = StringVar()
        roll_Input = StringVar()
        department_Input = StringVar()
        shift_Input = StringVar()
        semester_Input = StringVar()

        name_entry = Entry(frame2, font=('times new roman', 20, 'bold italic'), state='readonly', textvariable=studentName_Input, relief=RAISED)
        roll_entry = Entry(frame2, font=('times new roman', 20, 'bold italic'), state='readonly', textvariable=roll_Input, relief=RAISED)
        department_entry = Entry(frame2, font=('times new roman', 20, 'bold italic'), state='readonly', textvariable=department_Input, relief=RAISED)
        shift_entry = Entry(frame2, font=('times new roman', 20, 'bold italic'), state='readonly', textvariable=shift_Input, relief=RAISED)
        semester_entry = Entry(frame2, font=('times new roman', 20, 'bold italic'), state='readonly', textvariable=semester_Input, relief=RAISED)

        name_entry.grid(row=0, column=0)
        roll_entry.grid(row=1, column=0)
        department_entry.grid(row=2, column=0)
        shift_entry.grid(row=3, column=0)
        semester_entry.grid(row=4, column=0)


if __name__ == "__main__":
    login = Tk()

    app = Main_window(login)
    login.mainloop()
