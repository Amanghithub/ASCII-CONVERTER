from tkinter import *
root = Tk()

root.title("ASCII Converter")
root.geometry("400x200")
root.configure(background="snow")

enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.3,anchor=CENTER)

label=Label(root,text="Name in ASCII: ")
ey_label=Label(root,text="Your Encrypted Name is: ")

def asciiconverter() :
    input_word = enter_word.get()
    
    for letter in input_word:
        label["text"] += str(ord(letter)) + " "
        ascii_i=int(ord(letter))
        encrypted=ascii_i - 1
        ey_label["text"] += str(chr(encrypted))
        
btn=Button(root,text="Show ASCII Name And Encrypted Value",command=asciiconverter)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)
ey_label.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()