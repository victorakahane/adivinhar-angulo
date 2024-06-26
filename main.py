import tkinter as tk
from tkinter import messagebox
import tksvg
import draw

class Application:
    # Método construtor da aplicação
    def __init__(self, master=None):
        self.totalAttempts = 0
        self.secret_number = draw.createDraw()
        self.frmGuess = tk.Frame(master, bg="white")
        self.lblTitle = tk.Label(master, text="ADIVINHE O ÂNGULO", font=("Calibri", "18", "bold"), bg="white")
        self.lblTitle.pack()
        self.svg_image = tksvg.SvgImage(file="drawing.svg")
        self.imgAngle = tk.Label(master, image=self.svg_image, bg="white")
        self.imgAngle.image = self.svg_image
        self.imgAngle.pack()

        self.lblAttempts = tk.Label(master, text=f"Tentativas: {self.totalAttempts}/4", font=("12"), bg="white")
        self.lblAttempts.pack()

        self.txtGuess = tk.Entry(self.frmGuess, bg="white")
        self.txtGuess.pack(side="left", padx=(20, 5))

        self.btnGuess = tk.Button(self.frmGuess, text="Adivinhar!", command=self.getNumber)
        self.btnGuess.pack(side="left")

        self.txtGuess.bind('<Return>', self.onPressed)

        self.frmGuess.pack(pady=(0,3))

    # Obtém o número da caixa de entrada e verifica se é válido
    def getNumber(self):
        try:
            self.number = int(self.txtGuess.get())

            if self.checkLimit():
                if self.number < 0 or self.number > 360:
                    raise ValueError
                
                self.totalAttempts += 1
                self.createHint(self.number)
                self.checkLimit()
        except ValueError:
            messagebox.showerror("Erro", "Tem que ser um número inteiro entre 0 e 360!")

        self.clearText()
        
    # Cria um frame para cada ângulo que foi enviado pelo usuário
    def createHint(self, guess, master=None):
        response = self.isNear(guess)
        gray = "#dddddd"
        self.frmTry = tk.Frame(master, bg="white", pady=(3))
    
        self.lblTry = tk.Label(self.frmTry, text=f"{guess}°", font=12, bg=gray, relief="groove", width=5, justify="center")
        self.lblTry.pack(side="left", padx=(0, 2))

        self.lblEmoji = tk.Label(self.frmTry, text=f"{response[1].strip()}", font=6, bg=gray, relief="groove", width=5, justify="center")
        self.lblEmoji.pack(side="left")

        self.lblHint = tk.Label(self.frmTry, text=f"{response[0]}", font=12, bg=gray, relief="groove", width=15, justify="center")
        self.lblHint.pack(side="left", padx=(2, 0))

        self.frmTry.pack(pady=(0,2))

    # Verifica o quão perto está o ângulo do usuário do ângulo correto
    def isNear(self, guess):
        termomether_per = abs(self.secret_number - guess)
        termomether = self.secret_number - guess
        arrow = ""
        
        self.lblAttempts["text"] = f"Tentativas: {self.totalAttempts}/4"
        if termomether > 0:
            arrow = "⬆"
        elif termomether < 0:
            arrow = "⬇"
        elif termomether == 0:
            arrow = "🥳"

        if termomether_per > 25:
            return "Muito frio! 🥶", arrow
        elif termomether_per < 25 and termomether_per >= 18:
            return "Frio! ❄️", arrow
        elif termomether_per < 18 and termomether_per >= 10:
            return "Morno", arrow
        elif termomether_per < 10 and termomether_per >= 3:
            return "Quente! 🥵", arrow
        elif termomether_per < 3 and termomether_per > 0:
            return "Muito quente! 🔥", arrow
        elif termomether_per == 0:
            self.disableElements()
            messagebox.showinfo("Parabens!", f"Parabéns! Você ganhou!\nO ângulo era {self.secret_number}°")
            return "🎉🎉🎉", arrow
        
    # Checa se ainda existem tentativas restantes
    def checkLimit(self):
        if self.totalAttempts == 4 and self.number != self.secret_number:
            messagebox.showerror("Perdeu!", f"Mais sorte na próxima!\nO ângulo certo era: {self.secret_number}°")
            self.disableElements()
            return False
        else:
            return True
    
    # Apaga o resultado da caixa de texto
    def clearText(self):
        self.txtGuess.delete(0, tk.END)

    # Faz com que não seja possível apertar nos botões ou escrever na caixa
    def disableElements(self):
        self.clearText()
        self.btnGuess.config(state="disabled")
        self.txtGuess.config(state="disabled")

    # Se a tecla enter for pressionada, obter caixa de texto
    def onPressed(self, event):
        self.getNumber()

# Centraliza a janela do aplicativo
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

# Inicia uma classe Application 
root = tk.Tk()
root.geometry("400x500")
root.resizable(0, 0)
root.title("Adivinhe o Ângulo 1.0")
center(root)
root.configure(bg="white")
Application(root)
root.mainloop()