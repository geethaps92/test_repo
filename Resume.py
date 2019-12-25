from tkinter import *
from tkinter import messagebox

from struct import *
import sys



class ResumeForm :
    
    def OkClicked(self) :

        
        messagebox.showinfo("TextBox",self.text1.get())

        
        enc = sys.getdefaultencoding()
        self.f = open("reg.bin","ab")
        un = self.text1.get()
        self.packed_data = pack("30s",un.encode(enc))

        self.f.write(self.packed_data)

        self.f.close()
        
        messagebox.showinfo("RadioButton",self.v.get())
        messagebox.showinfo("Msg",self.Lb1.get(self.Lb1.curselection()))
        messagebox.showinfo("Msg",self.var.get())
        messagebox.showinfo("Msg",self.var1.get())
        messagebox.showinfo("Msg",self.var2.get())
        messagebox.showinfo("Msg","ok clicked")
        
    
    def __init__(self, master) :

        self.parent = master
        self.parent.title("Resume")
        self.v = StringVar()
        self.label1 = Label(self.parent, text = "Full Name")
        self.label1.grid(row = 0, column=0, sticky=E)
        self.label1.grid_configure(sticky="nsew")

        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(1, weight=1)
        self.parent.grid_columnconfigure(1, weight=1)
        self.text1 = Entry(self.parent, relief = "groove")
        self.text1.grid(row = 0, column=1,sticky=W)
        self.label1.grid_configure(sticky="nsew")
                                                   
        self.rb1 = Radiobutton(self.parent, 
              text="Male",
              padx = 20, 
              variable=self.v, 
              value="M").grid(row = 1, column=0)
        
        self.rb2 = Radiobutton(self.parent, 
              text="Female",
              padx = 20, 
              variable=self.v, 
              value="F").grid(row=1, column = 1)

        self.label2 = Label(self.parent, text = "UnderGraduate Course")
        self.label2.grid(row = 2, column=0)
        self.Lb1 = Listbox(self.parent)
        self.Lb1.insert(1, "B.Sc")
        self.Lb1.insert(2, "B.Com")
        self.Lb1.insert(3, "B.A")
        self.Lb1.insert(4, "B.Tech")
    
        self.Lb1.grid(row=2,column=1)

        data1 = ['python','java']
        
        self.var = StringVar()
        self.var.set('Python')
        self.op1 = OptionMenu(self.parent, self.var, *data1)
        self.op1.grid(row=3,column=1)


        self.var1 = StringVar()
        self.cb1 = Checkbutton(self.parent, text="Kannada", variable=self.var1).grid(row=4, column=1)
        self.var2 = StringVar()
        self.cb2 = Checkbutton(self.parent, text="English", variable=self.var2).grid(row=5, column=1)        


        self.b1 = Button(self.parent, text ="Ok",command=self.OkClicked)
        
        self.b1.grid(row = 3, column=0)


root = Tk()
my_gui = ResumeForm(root)
root.mainloop()
