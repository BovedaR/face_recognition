from tkinter import *
import tkinter, os, cv2, crop_image #tkinter show cb2 camera
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("300x400")
ventana.resizable(False, False)
ventana.title('Alta de Usuarios')
ventana.configure(bg='#006241')
ventana.iconbitmap("Enigm.ico")


texterror = tkinter.StringVar()
#text.set("a")
#textBox = tkinter.Entry(ventana, textvariable = text)
#ocupan espacio, para modificar la posicion de otros widgets
ventana.columnconfigure(0, weight=0)
ventana.columnconfigure(1, weight=1)
#ventana.rowconfigure(7, weight=1)
ventana.rowconfigure(3, weight=1)
#ventana.eval('tk::PlaceWindow . center')

windowWidth = ventana.winfo_reqwidth()
windowHeight = ventana.winfo_reqheight()
#print("Width",windowWidth,"Height",windowHeight)
positionRight = int(ventana.winfo_screenwidth()/2 - windowWidth)
positionDown = int(ventana.winfo_screenheight()/2 - windowHeight)

ventana.geometry("+{}+{}".format(positionRight, positionDown))

# Create an instance of TKinter Window or frame
# Set the size of the window

# Create a Label to capture the Video frames
label =Label(ventana)
label.grid(row=3, column=1)
#cap= cv2.VideoCapture(0)
#cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)- Agregar esto sino se rompe
cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)

cv2image = cv2

# Define function to show frame
def show_frames():
# Get the latest frame and convert into Image
	cv2image= cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
	cv2image= cv2.resize(cv2image, (0, 0), fx= 0.4, fy=0.4)
	img = Image.fromarray(cv2image)
	# Convert image to PhotoImage
	imgtk = ImageTk.PhotoImage(image = img)
	label.imgtk = imgtk
	label.configure(image=imgtk)
	# Repeat after an interval to capture continiously
	label.after(20, show_frames)

def CrearCarpeta(user):	
	try:

		numeros = [0,1,2,3,4,5,6,7,8,9]
		nombreUser = ""
		completo = False
		completoDNI = False
		guionBajo = False
		for i, letra in enumerate(user):
			nombreUser = nombreUser + letra
			if letra == "_":
				if guionBajo == True:
					break
				else:
					guionBajo = True
					if nombreUser == "_":
						break
					completo = True
					nombreUser = nombreUser.rstrip(nombreUser[-1])
					if nombreUser.isalpha() == False:
						break
					else:
						for x in numeros:
							if nombreUser.find(str(x)) != -1:
								completo = False

						nombreUser = ""

			if i == (len(user) - 1):
				if nombreUser.isdigit() == True:
					completoDNI = True

		if completo == True and completoDNI == True:
				os.mkdir(user.lower())
				texterror.set("")
				
				for i in range(50):
					cv2.imwrite(user + "/" + user + "_" + str(i) + ".jpg", cv2.cvtColor(cap.read()[1],0))
					crop_image.main(user + "/" + user + "_" + str(i) + ".jpg")
					texterror.set("Creado con exito!")
		else:
			texterror.set("Error o carpeta ya creada")
		
		#txtBoxUser.delete(0, 'end')	
		#txtBoxFoto.insert(0,user)
		#falta crear si no existe, meter foto en carpeta si existe
	except:
		texterror.set("Error o carpeta ya creada")


show_frames()


lblUser = tkinter.Label(ventana, text= "Nombre y Apellido:", font="Calibri 14 bold", bg='#006241', fg="#FFFFFF", padx=0, pady=20) 
lblUser.grid(row=0, column=1)

txtBoxUser = tkinter.Entry(ventana, font="Calibri 14", width=25)
txtBoxUser.grid(row=1, column=1,pady=(5,5))

lblUserError = tkinter.Label(ventana, textvariable=texterror, font="Calibri 12 bold", fg="#FFFFFF", bg='#006241') 
lblUserError.grid(row=2, column=1)

btnUser = tkinter.Button(ventana, text="Tomar foto", font="Calibri 11 bold", fg="#FFFFFF", bg="#FF5733", width=30, borderwidth=5, command= lambda: CrearCarpeta(txtBoxUser.get()))
btnUser.grid(row=4, column=1, pady=(20,20))

ventana.mainloop()