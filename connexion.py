
import tkinter
from tkinter import *
import mysql.connector as mc
from PIL import ImageTk, Image
import string


class Connexion:
    def __init__(self):
        self.host="localhost"
        self.database="bibliodb"
        self.user="root"
        self.password=""
        self.port=3306
        self.conn=None
        self.cursor=None


    def connect(self):
        try:
            self.conn=mc.connect(host=self.host,database=self.database,user=self.user,password=self.password)
            print("connect to database")
        except mc.Error as err:
            print(err)
        self.cursor=self.conn.cursor()
    def disconnect(self):
        if self.cursor:
            self.cursor.close
        if self.conn:
            self.conn.close
    def getAll(self):
        req=f"select * from user"
        self.cursor.execute(req)
        tasks=self.cursor.fetchall()
        return tasks
    def add(self,username,password,repPassword):
        req=f"insert into user (username,password,repPassword)values(%s,%s,%s)"
        values=(username,password,repPassword,)
        self.cursor.execute(req,values)
        self.conn.commit()
    def update(self,description,id):
        req=f"update {self.table} set description=%s where id=%s"
        values=(description,id)
        self.cursor.execute(req,values)
        self.conn.commit()
    def delete(self,id):
        req=f"delete from {self.table} where id=%s"
        values=(id,)
        self.cursor.execute(req,values)
        self.conn.commit()

