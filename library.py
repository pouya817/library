import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import json
# from fun import inside , out

class book:
    def __init__(self, name_book=None , date_modified=None ,genre=None , author=None):
        self.name_book = name_book 
        self.date_modified = date_modified 
        self.genre = genre
        self.author = author
    
    def __name__(self ,name_book):
        self.name_book = name_book 

    def __date__(self ,date_modified):
        self.date_modified = date_modified 

    def __genre__(self ,genre):
        self.genre = genre

    def __author__(self ,author):
        self.author = author

book_list={}
author_list_name={}
genre_list_name={}
book_new=0

def fun(event):
    def out(event):
        dont_leave["text"] = 'noooo , we missed you'
    pass

    def inside(event):
        dont_leave['text'] = "welcome back "
        pass
    dont_leave=Label(root, text="i say dont push 'f' but you do now dont leave me" ,justify="left")
    dont_leave.place(relx=0.0,rely=1.0,anchor = 'sw')
    root.bind("<Enter>", inside )
    root.bind("<Leave>", out )

def add_book_to_list_library():
    global book_list ,book_new
    book_list[book_new.name_book]={json.dumps(book_new.__dict__)}

def create_book():
    global root , book_new
    while True:
        global root , book_new
        def detail_entry():
            global book_new
            name_book_g=name.get()
            date_modified_g=date.get()
            genre_g=genre.get()
            author_g = author.get()
            book_new=book(name_book_g , date_modified_g , genre_g , author_g)
            print(book_new.name_book)
            return book_new
        root1=tk.Tk()
        root1.title("create desk")
        root1.geometry("400x300")

        name=Label(root1 ,text='pls intere your book name ' )
        name.pack()
        name=Entry(root1)
        name.pack()
        date=Label(root1 ,text='pls intere your book datemodified ' )
        date.pack()
        date=Entry(root1)
        date.pack()
        genre=Label(root1 ,text='pls intere your book genre ' )
        genre.pack()
        genre=Entry(root1)
        genre.pack()
        author=Label(root1 ,text='pls intere your book author ' )
        author.pack()
        author=Entry(root1)
        author.pack()
        
        input_bt=Button(root1,text= 'create book' , command=lambda:[detail_entry() ,add_book_to_list_library() ])
        input_bt.pack()
        quit_witoutsave=Button(root1,text= 'quit_witoutsave' , command=root1.destroy)
        quit_witoutsave.pack()

        close_all=Button(root1,text= 'close all' , command=quit)
        close_all.place(relx=0.5 , rely=1.0 , anchor="s")

        break
    return

def show_list_gui():
    i=0
    while True:
        global root , book_list_bt ,book_list
        list_name_book=list(book_list.keys())
        list_name_book.sort()
        book_list_bt=tk.Button(root,text=list_name_book[i] , command=print(i) )
        book_list_bt.pack()
        i=i+1
        break

def delete():
    global book_list
    def delete_entry():
        del book_list[delete_book_entry.get()]

    root2=tk.Tk()
    root2.title("delete desk")
    root2.geometry("400x300")

    delete_book_entry=Entry(root2)
    delete_book_entry.pack()
    
    delete_book=Button(root2 , text="delete book",command=lambda:delete_entry() , background='red')
    delete_book.pack()

    quit_witoutsave=Button(root2,text= 'quit_witoutsave' , command=root2.destroy)
    quit_witoutsave.pack()

    close_all=Button(root2,text= 'close all' , command=quit)
    close_all.place(relx=0.5 , rely=1.0 , anchor="s")
    pass



root=tk.Tk()
root.title("pouya's library")
root.geometry("400x300")

create_bool_win=Button(root,text='create book' ,command=lambda:[create_book(), ])
create_bool_win.place(relx=0.0 , rely=0.09 ,anchor='nw')

# book_new=create_book()
# print(book_new.__dict__)
# add_book_to_list_library()
# print(book_list)

text=tk.Label(root,text='hello' , justify="center")
text.pack()


book_list_bt=Label(root , text= "dont push f")
book_list_bt.pack()

show_list=Button(root ,text='show list', command=lambda:[book_list_bt.destroy(),show_list_gui()] )
show_list.place(relx=0.0,rely=0.0,anchor='nw')

delete_win=Button(root,text='delete' , command=delete)
delete_win.place(relx=1.0,rely=1.0,anchor = 'se')

root.bind("f",fun)


root.mainloop()