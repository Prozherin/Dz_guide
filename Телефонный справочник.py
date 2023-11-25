# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, 
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
# ГУИ можно сделать просто на EasyGUI или Tkinter

import json

import os

from tkinter import *

class Contact:
    def __init__(self, name, number, address):
        self.name = name

        self.number = number

        self.address = address


def add_contact():
    name = Name.get()
    number = Number.get()
    address = address_text.get("1.0", "end-1c")
    contact = Contact(name, number, address)
    contacts.append(contact)
    update_contacts_listbox()

def view_contact():
    if select.curselection():
        selected_index = select.curselection()[0]
        name, number, address = contacts[selected_index].name, contacts[selected_index].number, contacts[selected_index].address

        Name.set(name)
        Number.set(number)
        address_text.delete('1.0', 'end')
        address_text.insert('1.0', address)

def delete_contact():
    if select.curselection():
        selected_index = select.curselection()[0]
        del contacts[selected_index]
        update_contacts_listbox()

def update_contact():
    if select.curselection():
        selected_index = select.curselection()[0]
        name = Name.get()
        number = Number.get()
        address = address_text.get('1.0', 'end-1c')
        contacts[selected_index].name = name

        contacts[selected_index].number = number

        contacts[selected_index].address = address

        update_contacts_listbox()

def update_contacts_listbox():
    select.delete(0, END)
    for contact in contacts:
        select.insert(END, contact.name)

def reset_fields():
    Name.set('')
    Number.set('')
    address_text.delete('1.0', 'end')

def save_contacts_to_json():
    with open('contacts.json', 'w') as file:
        data = [{'name': contact.name, 'number': contact.number, 'address': contact.address} for contact in contacts]
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_contacts_from_json():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            contacts.clear()
            for item in data:
                contacts.append(Contact(item['name'], item['number'], item['address']))
            update_contacts_listbox()

def on_closing():
    save_contacts_to_json()
    root.destroy()

root = Tk()
root.geometry('400x500')
root.title('Phone Book')
root.protocol("WM_DELETE_WINDOW", on_closing)
contacts = []

Name = StringVar()
Number = StringVar()

frame = Frame()
frame.pack(pady=10)
frame1 = Frame()
frame1.pack()
frame2 = Frame()
frame2.pack(pady=10)

Label(frame, text='Name', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable=Name, width=50).pack()

Label(frame1, text='Phone No.', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable=Number, width=50).pack()

Label(frame2, text='Address', font='arial 12 bold').pack(side=LEFT)
address_text = Text(frame2, width=37, height=10)
address_text.pack()

Button(root, text="Add", font="arial 12 bold", command=add_contact).place(x=100, y=270)
Button(root, text="View", font="arial 12 bold", command=view_contact).place(x=100, y=310)
Button(root, text="Delete", font="arial 12 bold", command=delete_contact).place(x=100, y=350)
Button(root, text="Update", font="arial 12 bold", command=update_contact).place(x=100, y=390)
Button(root, text="Reset", font="arial 12 bold", command=reset_fields).place(x=100, y=430)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200, y=260)

load_contacts_from_json()

root.mainloop()

