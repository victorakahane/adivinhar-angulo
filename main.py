import tkinter as tk
import tksvg
import draw

class Application:
    def __init__(self, master=None):
        self.totalAttempts = 0
        self.secret_number = draw.createDraw()
        self.frmGuess = tk.Frame(master)
        self.lblTitle = tk.Label(master, text="Adivinhador de ângulo", font=("Calibri", "18", "bold"))
        self.lblTitle.pack()
        self.svg_image = tksvg.SvgImage(file="drawing.svg")
        self.imgAngle = tk.Label(master, image=self.svg_image)
        self.imgAngle.image = self.svg_image
        self.imgAngle.pack()

        self.lblAttempts = tk.Label(master, text=f"Tentativas: {self.totalAttempts}/4", font=("12"))
        self.lblAttempts.pack()

        self.txtGuess = tk.Entry(self.frmGuess)
        self.txtGuess.pack(side="left", padx=(20, 5))

        self.btnGuess = tk.Button(self.frmGuess, text="Adivinhar!", command=self.getNumber)
        self.btnGuess.pack(side="left")

        self.frmGuess.pack()

    def getNumber(self):
        number = int(self.txtGuess.get())
        self.createHint(number)

    def createHint(self, guess, master=None):
        response = self.isNear(guess)
        self.lblTherm = tk.Label(master, text=f"{guess}° | {response[0]} | {response[1]}", font=12)  
        self.lblTherm.pack(pady=(2))

    def isNear(self, guess):
        termometer_per = abs(self.secret_number - guess)
        termometer = self.secret_number - guess
        arrow = ""
        self.totalAttempts += 1
        self.lblAttempts["text"] = f"Tentativas: {self.totalAttempts}/4"
        if termometer > 0:
            arrow = "↑"
        elif termometer < 0:
            arrow = "↓"
        else:
            arrow = "Oba"

        if termometer_per > 20:
            return "Muito frio! ", arrow
        elif termometer_per < 20 and termometer_per >= 15:
            return "Frio! ", arrow
        elif termometer_per < 15 and termometer_per >= 12:
            return "Morno! ", arrow
        elif termometer_per < 12 and termometer_per > 5:
            return "Quente! ", arrow
        elif termometer_per < 5 and termometer_per > 0:
            return "Muito quente! ", arrow
        else:
            return "Acertou!", arrow

root = tk.Tk()



root.geometry("400x500")
Application(root)
root.mainloop()