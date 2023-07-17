from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from tkinter.messagebox import askyesno
from sqlite3 import *
import re
#def
def f1():
	mw.withdraw()
	root.deiconify()

def f2():
	mw.withdraw()
	sw.deiconify()
def f3():
	mw.deiconify()
	sw.withdraw()
def f4():
	if (ent_user.get()=="omkar@gmail.com" and ent_pass.get()=="omkar@123"):
		root.withdraw()
		aw.deiconify()
		ent_user.delete(0,END)
		ent_pass.delete(0,END)
		ent_user.focus()
	elif (ent_user.get()=="omkar@gmail.com" and ent_pass.get()!="omkar@123"):
		showerror("sorry","invalid password ")
		#ent_user.delete(0,END)
		ent_pass.delete(0,END)
		ent_pass.focus()
	elif (ent_user.get()!="omkar@gmail.com" and ent_pass.get()=="omkar@123"):
		showerror("sorry","invalid username ")
		ent_user.delete(0,END)
		#ent_pass.delete(0,END)
		ent_user.focus()
	else:
		showerror("sorry","invalid username and password")
		ent_user.delete(0,END)
		ent_pass.delete(0,END)
		ent_user.focus()
def f5():
	aw.withdraw()
	mw.deiconify()
def f6():
	aw.withdraw()
	vw.deiconify()
	st_view.delete(1.0,END)
	con=None
	try:
		con=connect("sfb.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg="Email: "  +   str(d[0]) +"\n" +  "Name: "   +   d[1]  +" \n" + "Feedback: " +  str(d[2])  + "Rating: " +  str(d[3]) + "\n\n"
			st_view.insert(INSERT,msg)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
def f7():
	aw.withdraw()
	uw.deiconify()
def f8():
	aw.withdraw()
	dw.deiconify()
def f9():
	vw.withdraw()
	aw.deiconify()
def f10():
	dw.withdraw()
	aw.deiconify()
def f11():
	uw.withdraw()
	aw.deiconify()

def save():
	con=None
	try:
		con=connect("sfb.db")
		cursor=con.cursor()
		sql="Insert into student values('%s','%s','%s','%s')"
		email=ent_email.get()
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			raise Exception("Invalid Email")

		name=ent_name.get()
		name=name.strip()
		if (name=="") or (not name.isalpha()) :
			raise Exception("invalid name")
			
		feedback=st_fb.get(1.0,END)
		if feedback.strip()=="":
			raise Exception("plz enter feedback")

		rating=""
		if s.get() == 1:
			rating = "*"
		if s.get() == 2:
			rating = "**"
		if s.get() == 3:
			rating = "***"
		if s.get() == 4:
			rating = "****"
		if s.get() == 5:
			rating = "*****"
		cursor.execute(sql % (email,name,feedback,rating))
		con.commit()
		showinfo("Success","feedback created")
		ent_email.delete(0,END)
		ent_name.delete(0,END)
		st_fb.delete(1.0,END)
		s.set(5)
		ent_email.focus()
	except Exception as e:
		con.rollback()
		showerror("issue",e)
		ent_email.delete(0,END)
		ent_name.delete(0,END)
		st_fb.delete(1.0,END)
		s.set(5)
		ent_email.focus()
	finally:
		if con is not None:
			con.close()
def delete():
	con=None
	try:
		con=connect("sfb.db")
		cursor=con.cursor()
		sql="delete from student where email= '%s' "
		email=ent1.get()
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			raise Exception("Invalid email format")
			
		confirmation=askyesno("confirmation","are u sure u want to delete feedback?")
		if confirmation:
			cursor.execute(sql %(email))
			if cursor.rowcount==1:
				con.commit()
				showinfo("congrats","feedback deleted")
				ent1.delete(0,END)
				ent1.focus()
			
			else:
				showerror("sorry","feedback dosen't Exist")
				ent1.delete(0,END)
				ent1.focus()
		else:
			ent1.delete(0, END)
			ent1.focus()
	except Exception as e:
		showerror("issue",e)
		ent1.delete(0,END)
		ent1.focus()
	finally:
		if con is not None:
			con.close()
def update():
	con=None
	try:
		con=connect("sfb.db")
		cursor=con.cursor()
		sql="update student set name='%s',feedback='%s',rating='%s' where email='%s' "
		email=ent_uemail.get()
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			raise Exception("Invalid email format")

		
		name=ent_uname.get()
		name=name.strip()
		if (name=="") or (not name.isalpha()) :
			raise Exception("invalid name")	

		feedback=st_ufb.get(1.0,END)
		if feedback.strip()=="":
			raise Exception("plz enter feedback")
	
		rating=""
		if s.get() == 1:
			rating = "*"
		if s.get() == 2:
			rating = "**"
		if s.get() == 3:
			rating = "***"
		if s.get() == 4:
			rating = "****"
		if s.get() == 5:
			rating = "*****"
		confirmation=askyesno("confirmation","Are u sure u want to update feedback?")
		if confirmation:
			cursor.execute(sql % (name,feedback, rating, email))
			if cursor.rowcount==1:
				con.commit()
				showinfo("congrats","feedback updated")
				ent_uemail.delete(0,END)
				ent_uname.delete(0,END)
				st_ufb.delete(1.0,END)
				s.set(5)
				ent_uemail.focus()
			else:
				showerror("sorry","feedback dosen't exist")
				ent_uemail.delete(0,END)
				ent_uname.delete(0,END)
				st_ufb.delete(1.0,END)
				s.set(5)
				ent_uemail.focus()
		else:
			ent_uemail.delete(0,END)
			ent_uname.delete(0,END)
			st_ufb.delete(1.0,END)
			s.set(5)
			ent_uemail.focus()

	except Exception as e:
		#con.rollback()
		showerror("issue",e)
		ent_uemail.delete(0,END)
		ent_uname.delete(0,END)
		st_ufb.delete(1.0,END)
		s.set(5)
		ent_uemail.focus()
	finally:
		if con is not None:
			con.close()


mw=Tk()
mw.title("Feedback Portal")
mw.geometry("800x550+50+50")
mw.iconbitmap("employee1.ico")
mw.configure(bg="light green")
f=("Arial",60,"bold")
btn_1=Button(mw,text="Admin",font=("Arial",40,"bold"),width=6,bg="yellow",command=f1)
btn_1.pack(pady=100)
btn_2=Button(mw,text="User",font=("Arial",40,"bold"),width=6,bg="yellow",command=f2)
btn_2.pack(pady=2)


#users portal
sw=Toplevel(mw)
sw.title("Users Feedback")
sw.geometry("950x600+100+50")
sw.iconbitmap("employee1.ico")
sw.configure(bg="yellow")
lab_email=Label(sw,text="Enter Your Email",bg="yellow",font=("Arial",30,"bold"))
lab_email.pack(pady=10)
ent_email=Entry(sw,font=("Arial",30,"bold"))
ent_email.pack(pady=10)
lab_name=Label(sw,text="Enter Your Name",bg="yellow",font=("Arial",30,"bold"))
lab_name.pack(pady=10)
ent_name=Entry(sw,font=("Arial",30,"bold"))
ent_name.pack(pady=10)
lab_fb=Label(sw,text="Enter feedback",bg="yellow",font=("Arial",30,"bold"))
lab_fb.pack(pady=10)
st_fb=ScrolledText(sw,font=("Arial",30,"bold"),width=10,height=3)
st_fb.pack(pady=10)
s=IntVar()
s.set(5)
lab_rat=Label(sw,text="Ratings:-",bg="yellow",font=("Arial",30,"bold"))
lab_rat.place(x=30 , y=530)
rb_1=Radiobutton(sw,text="*",font=("Arial",30,"bold"),bg="yellow",variable=s,value=1)
rb_1.place(x=220 ,y=520)
rb_2=Radiobutton(sw,text="**",font=("Arial",30,"bold"),bg="yellow",variable=s,value=2)
rb_2.place(x=370 ,y=520)
rb_3=Radiobutton(sw,text="***",font=("Arial",30,"bold"),bg="yellow",variable=s,value=3)
rb_3.place(x=520 ,y=520)
rb_4=Radiobutton(sw,text="****",font=("Arial",30,"bold"),bg="yellow",variable=s,value=4)
rb_4.place(x=670 ,y=520)
rb_5=Radiobutton(sw,text="*****",font=("Arial",30,"bold"),bg="yellow",variable=s,value=5)
rb_5.place(x=820 ,y=520)
btn_save=Button(sw,text="Save",font=("Arial",30,"bold"),width=5,bg="red",command=save)
btn_save.place(x=600 , y=390)
btn_back=Button(sw,text="Back",font=("Arial",30,"bold"),width=5,bg="red",command=f3)
btn_back.place(x=740 , y=390)
sw.withdraw()

#Admin access portal
root=Toplevel(mw)
root.title("Admin Window")
root.geometry("800x550+50+50")
root.iconbitmap("employee1.ico")
root.configure(bg="red")
f=("Arial",30,"bold")
lab_user=Label(root,text="Enter Username",font=f,bg="red")
lab_user.pack(pady=20)
ent_user=Entry(root,font=f)
ent_user.pack(pady=10)
lab_pass=Label(root,text="Enter Password",font=f,bg="red")
lab_pass.pack(pady=20)
ent_pass=Entry(root,font=f,show="*")
ent_pass.pack(pady=10)
btn_submit=Button(root,text="Submit",font=("Arial",30,"bold"),width=6,bg="green",command=f4)
btn_submit.pack(pady=20)
root.withdraw()


#Admin portal
aw=Toplevel(root)
aw.title("Admin Window")
aw.geometry("800x550+50+50")
aw.iconbitmap("employee1.ico")
aw.configure(bg="light green")
f=("Arial",60,"bold")
btn_view=Button(aw,text="View",font=("Arial",30,"bold"),width=6,bg="yellow",command=f6)
btn_view.pack(pady=10)
btn_upd=Button(aw,text="Update",font=("Arial",30,"bold"),width=6,bg="yellow",command=f7)
btn_upd.pack(pady=10)
btn_del=Button(aw,text="Delete",font=("Arial",30,"bold"),width=6,bg="yellow",command=f8)
btn_del.pack(pady=10)
btn_log=Button(aw,text="Log out",font=("Arial",30,"bold"),width=6,bg="yellow",command=f5)
btn_log.pack(pady=10)
aw.withdraw()

#view portal
vw=Toplevel(aw)
vw.title("Admin Window")
vw.geometry("800x550+50+50")
vw.iconbitmap("employee1.ico")
vw.configure(bg="purple")
f=("Arial",30,"bold")
st_view=ScrolledText(vw,font=f,width=25,height=8)
st_view.pack(pady=10)
btn=Button(vw,text="Back",font=("Arial",30,"bold"),bg="yellow",command=f9)
btn.pack(pady=20)
vw.withdraw()

#update portal
uw=Toplevel(aw)
uw.title("Update Window")
uw.geometry("950x600+100+50")
uw.iconbitmap("employee1.ico")
uw.configure(bg="purple")
f=("Arial",30,"bold")
lab_uemail=Label(uw,text="Enter Your Email",bg="purple",font=("Arial",30,"bold"))
lab_uemail.pack(pady=10)
ent_uemail=Entry(uw,font=("Arial",30,"bold"))
ent_uemail.pack(pady=10)
lab_uname=Label(uw,text="Enter Your Name",bg="purple",font=("Arial",30,"bold"))
lab_uname.pack(pady=10)
ent_uname=Entry(uw,font=("Arial",30,"bold"))
ent_uname.pack(pady=10)
lab_ufb=Label(uw,text="Enter feedback",bg="purple",font=("Arial",30,"bold"))
lab_ufb.pack(pady=10)
st_ufb=ScrolledText(uw,font=("Arial",30,"bold"),width=10,height=3)
st_ufb.pack(pady=10)
lab_ur=Label(uw,text="Ratings:-",bg="purple",font=("Arial",30,"bold"))
lab_ur.place(x=30 , y=530)
rb_u1=Radiobutton(uw,text="*",font=("Arial",30,"bold"),bg="purple",variable=s,value=1)
rb_u1.place(x=220 ,y=520)
rb_u2=Radiobutton(uw,text="**",font=("Arial",30,"bold"),bg="purple",variable=s,value=2)
rb_u2.place(x=370 ,y=520)
rb_u3=Radiobutton(uw,text="***",font=("Arial",30,"bold"),bg="purple",variable=s,value=3)
rb_u3.place(x=520 ,y=520)
rb_u4=Radiobutton(uw,text="****",font=("Arial",30,"bold"),bg="purple",variable=s,value=4)
rb_u4.place(x=670 ,y=520)
rb_u5=Radiobutton(uw,text="*****",font=("Arial",30,"bold"),bg="purple",variable=s,value=5)
rb_u5.place(x=820 ,y=520)
btn_upd=Button(uw,text="Update",font=("Arial",30,"bold"),width=5,bg="yellow",command=update)
btn_upd.place(x=620 , y=390)
btn_ub=Button(uw,text="Back",font=("Arial",30,"bold"),width=5,bg="yellow",command=f11)
btn_ub.place(x=770 , y=390)


uw.withdraw()

#delete portal
dw=Toplevel(aw)
dw.title("Delete Window")
dw.geometry("800x550+50+50")
dw.iconbitmap("employee1.ico")
dw.configure(bg="purple")
f=("Arial",30,"bold")
lab1=Label(dw,text="Enter Email",font=f,bg="purple")
lab1.pack(pady=20)
ent1=Entry(dw,font=f)
ent1.pack(pady=10)
btn_del=Button(dw,text="Delete",font=f,bg="yellow",width=5,command=delete)
btn_del.pack(pady=20)
btn_db=Button(dw,text="Back",font=f,bg="yellow",width=5,command=f10)
btn_db.pack(pady=20)
dw.withdraw()




def on_closing():
	if askyesno("close","Close Window"):
		mw.destroy()
aw.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)
root.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()