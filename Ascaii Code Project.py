from tkinter import *
root=Tk()
root.title("String To Ascii and Ecncrypted Value Converter")
root.geometry("500x500")
root.configure(background='light blue')
entry_word= Entry(root)
entry_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label_ascii=Label(root,text="Name in Ascii: ",bg="magenta",fg="black")
label_encrypted_name=Label(root,text="Encrypted Name: ",bg="cyan",fg="black")
label_encrypted_name.place(relx=0.5,rely=0.6,anchor=CENTER)
label_ascii.place(relx=0.5,rely=0.5,anchor=CENTER)

def ascii_converter():
    input_word=entry_word.get()
    
    for letter in input_word:
        label_ascii["text"]+=str(ord(letter))+ " "
        
        Ascii =int(ord(letter))
        encrypted=Ascii - 1
        label_encrypted_name["text"]+=str(chr(encrypted))+""
    

button1=Button(root,text="Show the Name in Ascaii and Encrypted Value ",command=ascii_converter,bg="yellow",fg="navy blue")
button1.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()