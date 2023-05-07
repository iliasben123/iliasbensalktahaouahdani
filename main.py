import tkinter
from  tkinter import ttk
from tkinter import *
import mysql.connector as mc
from PIL import ImageTk, Image
import string
from connexion import  Connexion as con

conn=con()
conn.connect()





rrr = Tk()
rrr.geometry('1000x667')
rrr.title("login page1")
image = Image.open("py2.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = tkinter.Label(rrr, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def menu():
    def tab0():
        user_button.destroy()
        admn_button.destroy()
        def tab3():
            frame1.destroy()
            label5.destroy()
            userclient_name.destroy()
            user_textuser.destroy()
            password_user.destroy()
            password_user_text.destroy()
            password_user_rep_text.destroy()
            password_user_rep.destroy()
            #password_user.destroy()
            button8.destroy()

            label6 = tkinter.Label(rrr, text="page3",bg='#00F')
            label6.pack()
            frame3 = tkinter.Frame(rrr, height=450, width=495, bg="BEIGE")
            frame3.place(x=305, y=189)
            game_frame = Frame(frame3)
            game_frame.pack()

            my_game = ttk.Treeview(game_frame)

            my_game['columns'] = ('id', 'titre', 'edition', 'auteur', 'la date de parution')

            my_game.column("#0", width=0, stretch=NO)
            my_game.column("id", anchor=CENTER, width=80)
            my_game.column("titre", anchor=CENTER, width=80)
            my_game.column("edition", anchor=CENTER, width=80)
            my_game.column("auteur", anchor=CENTER, width=80)
            my_game.column("la date de parution", anchor=CENTER, width=80)

            my_game.heading("#0", text="", anchor=CENTER)
            my_game.heading("id", text="id", anchor=CENTER)
            my_game.heading("titre", text="titre", anchor=CENTER)
            my_game.heading("edition", text="edition", anchor=CENTER)
            my_game.heading("auteur", text="auteur", anchor=CENTER)
            my_game.heading("la date de parution", text="la date de parution", anchor=CENTER)

            my_game.insert(parent='', index='end', iid=0, text='',
                           values=('1', 'Ninja', '101', 'Oklahoma', '1990'))
            my_game.insert(parent='', index='end', iid=1, text='',
                           values=('2', 'Ranger', '102', 'Wisconsin', '1889'))
            my_game.insert(parent='', index='end', iid=2, text='',
                           values=('3', 'Deamon', '103', 'ilyass', '1234'))
            my_game.insert(parent='', index='end', iid=3, text='',
                           values=('4', 'Dragon', '104', 'taha', '1999'))
            my_game.insert(parent='', index='end', iid=4, text='',
                           values=('5', 'CrissCross', '105', 'test', '1888'))
            my_game.insert(parent='', index='end', iid=5, text='',
                           values=('6', 'ZaqueriBlack', '106', 'auteur', '2010'))
            my_game.pack()

            def back1():
                label6.destroy()
                button7.destroy()
                tab0()
            button7 = tkinter.Button(rrr, text="<<< back ",command=back1,bg='BLACK',fg='beige',width=15)
            button7.pack(side=BOTTOM)

        frame1 = tkinter.Frame(rrr, height=350, width=350, bg="BEIGE")
        frame1.place(x=425, y=275)
        label5 = tkinter.Label(rrr, text="login page", font=("Times", "24", "bold italic "), bg="BEIGE")
        label5.place(x=535, y=275)
        userclient_name = tkinter.Label(rrr, text="user_name", bg="BEIGE")
        userclient_name.place(x=425, y=385)
        user_textuser = tkinter.Entry(rrr, width=30)
        user_textuser.place(x=525, y=385)
        password_user = tkinter.Label(rrr, text="password", bg="BEIGE")
        password_user.place(x=425, y=435)
        password_user_text = tkinter.Entry(rrr, width=30)
        password_user_text.place(x=525, y=435)

        password_user_rep = tkinter.Label(rrr, text="repeat password", bg="BEIGE")
        password_user_rep.place(x=425, y=485)
        password_user_rep_text = tkinter.Entry(rrr, width=30)
        password_user_rep_text.place(x=525, y=485)
        # rrr.configure(bg='#00F')

        button8 = tkinter.Button(rrr, text="next",command=tab3, bg='#00F')
        button8 .place(x=525, y=520, width=170)

    user_button = tkinter.Button(rrr, text="user", command=tab0, width=30, bg="black", fg="beige")
    user_button.place(x=125, y=300)

    def tab1():
        admn_button.destroy()
        user_button.destroy()
        def tab2():
            label1.destroy()
            button1.destroy()
            user_name.destroy()
            user_text.destroy()
            password.destroy()
            password_text.destroy()
            frame.destroy()
            label2 = tkinter.Label(rrr, text="page2",bg='#00F')
            label2.pack()
            frame2 = tkinter.Frame(rrr, height=350, width=350, bg="BEIGE")
            frame2.place(x=405, y=275)
            admin_acces_page = tkinter.Label(rrr, text=" admin acces page", font=("Times", "24", "bold italic "),
                                            bg="BEIGE")
            admin_acces_page.place(x=455, y=275)
            buttn_add = tkinter.Button(rrr, text="ADD BOOK", bg="black", fg="beige", height=7, width=15)
            buttn_add.place(x=515, y=385)
            buttn_add = tkinter.Button(rrr, text="DELETE BOOK", bg="black", fg="beige", height=7, width=15)
            buttn_add.place(x=515, y=475)
            def back():
                label2.destroy()
                button2.destroy()
                tab1()
            button2 = tkinter.Button(rrr, text=" <<< back ",command=back,bg='black',fg="beige",width=15)
            button2.pack(side=BOTTOM)


        frame = tkinter.Frame(rrr,height=350,width=350 ,bg="BEIGE")
        frame.place(x=425,y=275)
        label1 = tkinter.Label(rrr, text="login page", font=("Times", "24", "bold italic "),bg="BEIGE")
        label1.place(x=535,y=275)
        user_name = tkinter.Label(rrr,text="user_name",bg="BEIGE")
        user_name.place(x=425, y=385)
        user_text = tkinter.Entry(rrr,width=30)
        user_text.place(x=515, y=385)
        password = tkinter.Label(rrr, text="password",bg="BEIGE")
        password.place(x=425, y=435)
        password_text = tkinter.Entry(rrr,width=30)
        password_text.place(x=515, y=435)

        reppassword = tkinter.Label(rrr, text="repeat password", bg="BEIGE")
        reppassword.place(x=425, y=475)
        reppassword_text = tkinter.Entry(rrr, width=30)
        reppassword_text.place(x=515, y=475)
        #rrr.configure(bg='#00F')


        button1 = tkinter.Button(rrr,text="next", command=tab2,bg='#00F')
        button1.place(x=525,y=520,width=170)

    admn_button = tkinter.Button(rrr, text="admine", command=tab1,width=30,bg="black",fg="beige")
    admn_button.place(x=650,y=300)

menu()

rrr.mainloop()