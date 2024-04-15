import tkinter as tk
from PIL import Image, ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import sympy

def Addition():
    toplevel = tk.Toplevel()
    toplevel.title('Addition')
    toplevel.geometry('500x500')
    toplevel.resizable(False,False)
    toplevel.config(background='grey')
    
    def topla():
        sayilar = e.get()
        sayilar_listesi = sayilar.split("+")
        toplam = 0
        for i in sayilar_listesi:
           toplam += int(i)
        label3 = tk.Label(toplevel,text='',bg='grey',fg='black',font='Times 15 bold')
        label3.place(x=230,y=220)
        label3.config(text=str(toplam))
   

    label2=tk.Label(toplevel,text="Enter the numbers you want to sum like this = 2+2+2+-4",bg='grey',fg='black',font='Times 15 italic').place(x=10,y=60)
    e=tk.StringVar()
    entry1=tk.Entry(toplevel,textvariable=e,font='Times 15 bold').place(x=150, y=120)
    buton1=tk.Button(toplevel,text='Result',font='Times 13 bold',command=topla).place(x=220,y=170)
    
    
def Substraction():
    toplevel = tk.Toplevel()
    toplevel.title('Substraction')
    toplevel.geometry('500x500')
    toplevel.resizable(False,False)
    toplevel.config(background='grey')
    
    def çıkar():
        sayilar = e.get()
        sayilar_listesi = sayilar.split(",")
        toplam = int(sayilar_listesi[0])
        for i in sayilar_listesi[1:]:  # İlk elemanı hariç diğer elemanları döngüye al
            toplam = toplam - int(i)
        label3 = tk.Label(toplevel,text='',bg='grey',fg='black',font='Times 15 bold')
        label3.place(x=230,y=220)
        label3.config(text=str(toplam))
   

    label2=tk.Label(toplevel,text=" Write the numbers you want to subtract\nfrom each other = 2,2,2,-4 ",bg='grey',fg='black',font='Times 15 italic').place(x=90,y=60)
    e=tk.StringVar()
    entry1=tk.Entry(toplevel,textvariable=e,font='Times 15 bold').place(x=150, y=120)
    buton1=tk.Button(toplevel,text='Result',font='Times 13 bold',command=çıkar).place(x=220,y=170)


def Multiplication():
    toplevel = tk.Toplevel()
    toplevel.title('Multiplication')
    toplevel.geometry('500x500')
    toplevel.resizable(False,False)
    toplevel.config(background='grey')
    
    def çarp():
        sayilar = e.get()
        sayilar_listesi = sayilar.split("*")
        toplam = int(sayilar_listesi[0])
        for i in sayilar_listesi[1:]:  # İlk elemanı hariç diğer elemanları döngüye al
            toplam = toplam*int(i)
        label3 = tk.Label(toplevel,text='',bg='grey',fg='black',font='Times 15 bold')
        label3.place(x=230,y=220)
        label3.config(text=str(toplam))
        
        
    label2=tk.Label(toplevel,text="  Enter the numbers you want to multiply like this = 2*2*2*-2 ",bg='grey',fg='black',font='Times 14 italic').place(x=5,y=60)
    e=tk.StringVar()
    entry1=tk.Entry(toplevel,textvariable=e,font='Times 15 bold').place(x=150, y=120)
    buton1=tk.Button(toplevel,text='Result',font='Times 13 bold',command=çarp).place(x=220,y=170)

def Division():
    toplevel = tk.Toplevel()
    toplevel.title('Division')
    toplevel.geometry('500x500')
    toplevel.resizable(False,False)
    toplevel.config(background='grey')
    
    def çıkar():
        sayilar = e.get()
        sayilar_listesi = sayilar.split("/")
        toplam = int(sayilar_listesi[0])
        for i in sayilar_listesi[1:]:  
            toplam = toplam/int(i)
        label3 = tk.Label(toplevel,text='',bg='grey',fg='black',font='Times 15 bold')
        label3.place(x=230,y=220)
        label3.config(text=str(toplam))
   

    label2=tk.Label(toplevel,text=" Enter the numbers you want to divide like this = 2/2/2/-4 ",bg='grey',fg='black',font='Times 15 italic').place(x=5,y=60)
    e=tk.StringVar()
    entry1=tk.Entry(toplevel,textvariable=e,font='Times 15 bold').place(x=150, y=120)
    buton1=tk.Button(toplevel,text='Result',font='Times 13 bold',command=çıkar).place(x=220,y=170)

def Factorial():
    toplevel = tk.Toplevel()
    toplevel.title('Factorial')
    toplevel.geometry('500x500')
    toplevel.resizable(False,False)
    toplevel.config(background='grey')
    
    def factorial():
        try:
            num = int(e.get())
            if num < 0:
                messagebox.showerror("Error", "Negative numbers do not have factorials.")
            else:
                factorial_result = 1
                for i in range(1, num + 1):
                    factorial_result *= i
                label3 = tk.Label(toplevel, text='', bg='grey', fg='black', font='Times 15 bold')
                label3.config(text=f"Factorial of {num} is {factorial_result}")
                label3.place(x=165, y=210)  
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")


    label2=tk.Label(toplevel,text="Factorial Calculator",bg='grey',fg='black',font='Times 15 italic').place(x=165,y=70)
    e=tk.StringVar()
    entry1=tk.Entry(toplevel,textvariable=e,font='Times 15 bold').place(x=150, y=120)
    buton1=tk.Button(toplevel,text='Result',font='Times 13 bold',command=factorial).place(x=220,y=170)


def Derivative():
    toplevel = tk.Toplevel()
    toplevel.title('Derivative')
    toplevel.geometry('500x500')
    toplevel.resizable(False, False)
    toplevel.config(background='grey')

    def derivative():
        expression = e.get()
        x = sympy.symbols('x')
        try:
            f = sympy.sympify(expression)
            f_prime = sympy.diff(f, x)
            label3 = tk.Label(toplevel, text='', bg='grey', fg='black', font='Times 15 bold')
            label3.config(text=f"The derivative of {expression} is {f_prime}")
            label3.place(x=30, y=210)
        except sympy.SympifyError:
            messagebox.showerror("Error", "Invalid expression.")

    label2 = tk.Label(toplevel, text="Enter the function to calculate its derivative \n            (e.g., x**2+3*x+x+4)",
                      bg='grey', fg='black', font='Times 15 italic').place(x=30, y=60)
    e = tk.StringVar()
    entry1 = tk.Entry(toplevel, textvariable=e, font='Times 15 bold').place(x=150, y=120)
    button1 = tk.Button(toplevel, text='Result', font='Times 13 bold', command=derivative).place(x=220, y=170)

    
def secilenislem(event):
    seçilen_islem= x.get()
    if seçilen_islem == "Addition '+'":
        Addition()
    elif seçilen_islem == "Substraction '-'":
        Substraction()
    elif seçilen_islem == "Multiplication 'x'":
        Multiplication() 
    elif seçilen_islem == "Division '÷'":
        Division()
    elif seçilen_islem == "Factorial '!'":
        Factorial()
    elif seçilen_islem == "Derivative":
        Derivative()
     
    

form = tk.Tk()
form.title('MathLab')
form.geometry('500x500')
form.resizable(False, False)

resim = ImageTk.PhotoImage(Image.open('5.png'))
label1 = tk.Label(font='Times 20', image=resim)
label1.pack()

x = tk.StringVar()
a = ["Addition '+'", "Substraction '-'", "Multiplication 'x'", "Division '÷'","Factorial '!'","Derivative"]
kutu = Combobox(form, values=a, font='Times 15 bold', textvariable=x)
kutu.place(x=135, y=170)
kutu.bind("<<ComboboxSelected>>",secilenislem)  

form.mainloop()
