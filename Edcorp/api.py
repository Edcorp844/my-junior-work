import requests
from tkinter import *
    
root = Tk()
def web():
    try:    
        response = requests.get('https://amazibaministries.org')
        lable = Label(root, text=response.status_code, fg='purple')
        lable.pack()
        text=response.text
        with open('api.html', 'w') as f:
            f.write(text)
    except:
        lable = Label(root, text='failed!', fg='red')
        lable.pack()
        
    
root.title("Api")
root.geometry("300x850")
icon = PhotoImage(file = 'math//download.png')
root.iconphoto(False, icon)
root.minsize(width=400, height=400)
button = Button(root, text = 'get api', fg='white', bg='green', command=web)
button.place(x=280, y=400)

root.mainloop()