from tkinter import *
import tkinter, os, cv2 #tkinter show cb2 camera
from PIL import Image, ImageTk
import face_recognition
from utils import loading_bar
import threading

ventana = Tk()
ventana.geometry("300x400")
ventana.resizable(False, False)
ventana.title('Alta de Usuarios')
ventana.configure(bg='#006241')

if os.name == 'nt':
	#windows
    ventana.iconbitmap("Enigm.ico")
else:
	#linux (falta probar)
    ventana.iconbitmap("Enigm.xbm")


texterror = tkinter.StringVar()

ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(3, weight=1)


windowWidth = ventana.winfo_reqwidth()
windowHeight = ventana.winfo_reqheight()
positionRight = int(ventana.winfo_screenwidth()/2 - windowWidth)
positionDown = int(ventana.winfo_screenheight()/2 - windowHeight)

ventana.geometry("+{}+{}".format(positionRight, positionDown))

label =Label(ventana)
label.grid(row=3, column=1)

cap = None
if os.name == 'posix':
    # linux
    cap= cv2.VideoCapture(0)
elif os.name == 'nt':
    # windows
    cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
else:
    assert False, "agregar el SO"

cv2image = cv2
def show_frames():
	cv2image= cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
	cv2image= cv2.resize(cv2image, (0, 0), fx= 0.4, fy=0.4)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image = img)
	label.imgtk = imgtk
	label.configure(image=imgtk)
	label.after(20, show_frames)

def take_video(name):
	frame_count = 10
	out = cv2.VideoWriter(f'videos/{name}.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (320,320))
	count = 0
	l = loading_bar(frame_count)
	while count < frame_count:
		_, frame = cap.read()

		face = face_recognition.face_locations(frame)
		if face  != []:
			top, right, bottom, left = face[0]

			out.write(cv2.resize(frame[top:bottom, left:right], (320,320)))
			count+=1
			l.add(1)
			print(l, end='\r')

show_frames()

lblUser = tkinter.Label(ventana, text= "Nombre y Apellido:", font="Calibri 14 bold", bg='#006241', fg="#FFFFFF", padx=0, pady=20) 
lblUser.grid(row=0, column=1)

txtBoxUser = tkinter.Entry(ventana, font="Calibri 14", width=25)
txtBoxUser.grid(row=1, column=1,pady=(5,5))

btnUser = tkinter.Button(ventana, text="Tomar foto", font="Calibri 11 bold", fg="#FFFFFF", bg="#FF5733", width=30, borderwidth=5, command= lambda: take_video(txtBoxUser.get()))
btnUser.grid(row=4, column=1, pady=(20,20))

ventana.mainloop()
