""" import qrcode
img = qrcode.make("Vanakkam thamizha")
img.save("img.jpg")



#pip install opencv-python
import cv2
qr_img = cv2.imread("img.jpg")
qr_det = cv2.QRCodeDetector()
val, pts, st_code = qr_det.detectAndDecode(qr_img)
print("Information:", val)
""" 

""" import qrcode
img = qrcode.make("Sweet Home")
img.save("Rethu.jpg")

import cv2
qr_Rethu = cv2.imread("Rethu.jpg")
qr_det = cv2.QRCodeDetector()
val,pts,st_code = qr_det.detectAndDecode(qr_Rethu)
print("Information:",val) 



from tkinter import *
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
win = Tk()

win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = PhotoImage(Image.open("img.jpg"))
label = Button(frame, image = img)
label.pack()

win.mainloop()

from tkinter import *
from PIL import Image, ImageTk
from PIL.ImageTk import PhotoImage
win = Tk()
win .geometry("600x600")
frame = Frame(win,width=500, height=500)
frame.pack()
frame.place(anchor='center',relx=0.5,rely=0.5)

Rethu = PhotoImage(Image.open("Rethu.jpg"))
label = Button(frame, image = Rethu)
label.pack()
win.mainloop()
"""