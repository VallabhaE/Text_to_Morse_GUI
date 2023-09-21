from tkinter import *
def text_to_morse(text):
    morse_code_rules = {
        'a': '·−',
        'b': '−···',
        'c': '−·−·',
        'd': '−··',
        'e': '·',
        'f': '··−·',
        'g': '−−·',
        'h': '····',
        'i': '··',
        'j': '·−−−',
        'k': '−·−',
        'l': '·−··',
        'm': '−−',
        'n': '−·',
        'o': '−−−',
        'p': '·−−·',
        'q': '−−·−',
        'r': '·−·',
        's': '···',
        't': '−',
        'u': '··−',
        'v': '···−',
        'w': '·−−',
        'x': '−··−',
        'y': '−·−−',
        'z': '−−··',
        '0': '−−−−−',
        '1': '·−−−−',
        '2': '··−−−',
        '3': '···−−',
        '4': '····−',
        '5': '·····',
        '6': '−····',
        '7': '−−···',
        '8': '−−−··',
        '9': '−−−−·',
        ' ': '/'
    }

    res=""
    for i in text:
        res+=(morse_code_rules[i.lower()]+" ")
    Label(text=res,font=(90),bg="blue",foreground="white").grid(column=2,row=6)
    Label(text="Data Has been Copyd to ClipBoard").grid(row=3,column=0,columnspan=3)
    top = Toplevel(gui)
    top.geometry("500x100")
    top.title("Child Window")
    Label(top, text="Data Has Been Copyed!", font=('Mistral 18 bold',20)).pack()
    gui.clipboard_clear()
    gui.clipboard_append(res)
gui=Tk()
gui.config(background="white")
gui.title("TextToMorse")
gui.geometry("300x300")
label1=Label(gui,text="Enter Text To Convert:",background="white",font=(30))
label1.grid(row=0,column=2)
entry1=Entry(gui)
entry1.grid(row=1,column=2)
btn=Button(gui,text="Click Me",command=lambda:text_to_morse(entry1.get()) )
btn.grid(column=2,row=2)
gui.mainloop()