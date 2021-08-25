import tkinter as tk

root=tk.Tk()

e_var=tk.StringVar()
entry=tk.Entry(root,textvariable=e_var)
entry.config(font=("Courier",30,'bold'),bg='#123456',fg='white',width=20)
entry.grid(row=0,column=0,columnspan=4)


exp=""
def exp_var(n):
    global exp
    exp=exp+str(n)
    e_var.set(exp)

def clear():
    global exp
    exp=""
    e_var.set(exp)

def back():
    global exp
    exp=exp[:-1]
    e_var.set(exp)


def equal():
    global exp
    try:
        total=str(eval(exp.lstrip("0"))) 
        e_var.set(total) 
        exp=""
    except:
        e_var.set("error")
        exp=""

bx=tk.Button(root,text="<=",command=back)
bx.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
bx.grid(row=0,column=4)

c=1
for row in range(1,4):
    for col in range(1,4):
        value=str(c)
        b=tk.Button(root,text=str(c),command=lambda value=value:exp_var(value))
        b.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
        b.grid(row=row,column=col) 
        c+=1

b1=tk.Button(root,text="+",command=lambda:exp_var('+'))
b1.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=5,relief=tk.RAISED,bd=3)
b1.grid(row=1,column=4,rowspan=2)

b2=tk.Button(root,text="-",command=lambda:exp_var('-'))
b2.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b2.grid(row=3,column=4)

b3=tk.Button(root,text="0",command=lambda:exp_var('0'))
b3.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b3.grid(row=4,column=1)

b4=tk.Button(root,text="00",command=lambda:exp_var('00'))
b4.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b4.grid(row=4,column=2)

b5=tk.Button(root,text="*",command=lambda:exp_var('*'))
b5.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b5.grid(row=4,column=3,padx=1,pady=1)

#Equal button
b6=tk.Button(root,text="=",command=equal)
b6.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b6.grid(row=4,column=4)

b7=tk.Button(root,text="Clear",command=clear)
b7.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b7.grid(row=1,column=0)

b8=tk.Button(root,text=".",command=lambda:exp_var('.'))
b8.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b8.grid(row=2,column=0)

b9=tk.Button(root,text="%",command=lambda:exp_var('%'))
b9.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b9.grid(row=3,column=0)

b10=tk.Button(root,text="/",command=lambda:exp_var('/'))
b10.config(bg="#eeeeee",fg='#123456',font=("Times",25,'bold'),width=6,height=2,relief=tk.RAISED,bd=3)
b10.grid(row=4,column=0)





root.iconbitmap('images/cal.ico')
root.config(bg='black')
root.title("Calculator")
root.minsize(672,500)
root.resizable(0,0)
root.mainloop()