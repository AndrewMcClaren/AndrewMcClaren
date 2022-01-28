from tkinter import*
from PIL import Image, ImageTk
from sklearn.linear_model import Ridge



class SistemaDelHotelDePipe:
    def __init__(self,root):
        self.root= root
        self.root.title("HospitalSistema")
        self.root.geometry("1550x800+0+0")


        img1=Image.open(r"C: \Users\57301\Desktop\Curos de programacion\1.Tipos-de-datos\hotelpipe.jpg")
        img1=img1.recize((1550,140), Image.ANTIALIAS)
        self.photoimg1= ImageTk, PhotoImage(img1)

        lbling= Label(self, root,image=self.photoimg1, bd=4, relief=Ridge)
        lbling.place(x=0, y=0,width=1550,height=140)







if __name__=="__main__":
    root=Tk()
    obj= SistemaDelHotelDePipe(root)
    root.mainloop()
