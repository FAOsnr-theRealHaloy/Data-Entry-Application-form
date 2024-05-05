import customtkinter
from tkinter import *
from tkinter import messagebox
import database


entry=customtkinter.CTk()
entry.title('Data Entry')
entry.geometry('700x495')
entry.config(bg='black')
entry.resizable(False,False)


def new_course():
    identry.delete(0, END)
    nameentry.delete(0, END)
    Variable1.set('1 month')
    Variable2.set('')
    languageentry.delete(0, END)
    priceentry.delete(0, END)

def insert_ids_option():
    ids=database.fetch_all_ids()
    ids_options.configure(values=ids)


def search_course():
    selection=Variable3.get()
    if selection!='Select':
        row= database.search_course(selection)
        id_result_label.configure(text=row[0])
        name_result_label.configure(text=row[1])
        duration_result_label.configure(text=row[2])
        format_result_label.configure(text=row[3])
        language_result_label.configure(text=row[4])    
        price_result_label.configure(text=row[5])
    else:
        messagebox.showinfo('Error','Select ID')
def submit_registration():
    id=identry.get()
    name=nameentry.get()
    duration=Variable1.get()
    format=Variable2.get()
    language=languageentry.get()
    price=priceentry.get()
    try:
        if not(id and name and duration and format and language and price):
            messagebox.showerror('Enter all fields.')
        elif database.id_exist(id):
            messagebox.showerror ('Error','ID already exist')
        else:
            price_value=int(price)
            database.insert_courses(id,name,duration,format,language,price)
            insert_ids_option()
            messagebox.showinfo('Success', 'Data has been inserted')
    except ValueError:
        messagebox.showerror('Error','Price should be an integer')
    except:
        messagebox.showerror('Error','Error occured')


titleLabel=customtkinter.CTkLabel(entry,font=('Times New Romans', 18, 'bold'),text='ENTRY FOR COURSES REGISTRATION', text_color='white',bg_color='black')
titleLabel.place(x=190,y=12)

frame1=customtkinter.CTkFrame(entry,bg_color='black', width=250,fg_color='black',border_width=2,height=395,border_color='white',corner_radius=10)
frame1.place(x=30,y=60)

frame2=customtkinter.CTkFrame(entry,bg_color='black', width=350,fg_color='black',border_width=2,height=260,border_color='yellow',corner_radius=10)
frame2.place(x=319,y=60)

idLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Course Id:',text_color='white',bg_color='black')
idLabel.place(x=10,y=10)
identry=customtkinter.CTkEntry(frame1,font=('Times New Romans', 15, ),text_color='white',fg_color='black',border_color='white', border_width=1, width=230)
identry.place(x=10,y=35)

nameLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Name:',text_color='white',bg_color='black')
nameLabel.place(x=10,y=65)
nameentry=customtkinter.CTkEntry(frame1,font=('Times New Romans', 15,),text_color='white',fg_color='black',border_color='white', border_width=1, width=230)
nameentry.place(x=10,y=90)

durationLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Duration:',text_color='white',bg_color='black')
durationLabel.place(x=10,y=120)
Variable1=StringVar()
options=['1 month','2 months','3 months']

durationoptions=customtkinter.CTkComboBox(frame1,font=('Times New Romans', 12, 'bold'),text_color='white',fg_color='black',dropdown_hover_color='green',button_color='green',border_color='white',width=230,border_width=1, variable=Variable1,values=options,state='readonly')
durationoptions.set('1 month')
durationoptions.place(x=10,y=145)

formatLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Format:',text_color='white',bg_color='black')
formatLabel.place(x=10,y=175)

Variable2= StringVar()
choice_A=customtkinter.CTkRadioButton(frame1,text='Online',font=('Times New Romans', 15,'bold'),text_color='white',fg_color='white',hover_color='green',width=100, variable=Variable2,value='Online')
choice_B=customtkinter.CTkRadioButton(frame1,text='Class',font=('Times New Romans', 15,'bold'),text_color='white',fg_color='white',hover_color='green',width=100,variable=Variable2,value='Class')
choice_A.place(x=10,y=200)
choice_B.place(x=90,y=200)

languageLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Language:',text_color='white',bg_color='black')
languageLabel.place(x=10,y=230)
languageentry=customtkinter.CTkEntry(frame1,font=('Times New Romans', 15, ),text_color='white',fg_color='black',border_color='white', border_width=1, width=230)
languageentry.place(x=10,y=255)

priceLabel=customtkinter.CTkLabel(frame1,font=('Times New Romans', 15, 'bold'),text='Price:',text_color='white',bg_color='black')
priceLabel.place(x=10,y=285)
priceentry=customtkinter.CTkEntry(frame1,font=('Times New Romans', 15, ),text_color='white',fg_color='black',border_color='white', border_width=1, width=230)
priceentry.place(x=10,y=310)

submitbutton=customtkinter.CTkButton(frame1,text='Submit', command=submit_registration, font=('Times New Romans', 15,'bold'),text_color='white',fg_color='green',hover_color='green',width=100,)
submitbutton.place(x=10,y=350)

clearbutton=customtkinter.CTkButton(frame1,text='Clear',command=new_course, font=('Times New Romans', 15,'bold'),text_color='white',fg_color='green',hover_color='green',width=100,)
clearbutton.place(x=137,y=350)


searchLabel=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Search by ID:',text_color='white',bg_color='black')
searchLabel.place(x=10,y=10)

Variable3= StringVar()
ids_options=customtkinter.CTkComboBox(frame2,font=('Times New Romans', 12, 'bold'),text_color='white',fg_color='black',dropdown_hover_color='green',button_color='green',border_color='white',width=150,border_width=1, variable=Variable3,state='readonly')
ids_options.set('Select')
ids_options.place(x=110,y=10)

search_button=customtkinter.CTkButton(frame2,text='Search',command=search_course, font=('Times New Romans', 15,'bold'),text_color='white',fg_color='green',hover_color='green',width=100,)
search_button.place(x=420,y=10)

id_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Course Id:',text_color='white',bg_color='black')
id_result_Label.place(x=10,y=65)

name_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Name:',text_color='white',bg_color='black')
name_result_Label.place(x=180,y=65)

duration_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Duration:',text_color='white',bg_color='black')
duration_result_Label.place(x=10,y=122)

format_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Format:',text_color='white',bg_color='black')
format_result_Label.place(x=180,y=122)

language_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Language:',text_color='white',bg_color='black')
language_result_Label.place(x=10,y=179)

price_result_Label=customtkinter.CTkLabel(frame2,font=('Times New Romans', 15, 'bold'),text='Price:',text_color='white',bg_color='black')
price_result_Label.place(x=180,y=179)

#create the container to hold the ouput
id_result_label=customtkinter.CTkLabel(frame2,text='')
id_result_label.place(x=10,y=90)
name_result_label=customtkinter.CTkLabel(frame2,text='')
name_result_label.place(x=180,y=90)
duration_result_label=customtkinter.CTkLabel(frame2,text='')
duration_result_label.place(x=10,y=147)
format_result_label=customtkinter.CTkLabel(frame2,text='')
format_result_label.place(x=180,y=147)
language_result_label=customtkinter.CTkLabel(frame2,text='')
language_result_label.place(x=10,y=204)
price_result_label=customtkinter.CTkLabel(frame2,text='')
price_result_label.place(x=180,y=204)


insert_ids_option()
entry.mainloop()


