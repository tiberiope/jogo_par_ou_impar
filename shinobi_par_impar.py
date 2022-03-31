import tkinter
from constantes import *
from calc_par_impar import *

class Janela():
    def __init__(self, raiz):
        self.fr1 = tkinter.Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr2 = tkinter.Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = tkinter.Frame(raiz, bg=cinza1)
        self.fr3.pack()

        self.fr4 = tkinter.Frame(raiz, bg=cinza1)
        self.fr4.pack()

        self.fr5 = tkinter.Frame(raiz, bg=cinza1)
        self.fr5.pack()

        self.fr6 = tkinter.Frame(raiz, bg=cinza1)
        self.fr6.pack()

        self.img_player = tkinter.PhotoImage(file='images/ninja.png')
        self.img_pc = tkinter.PhotoImage(file='images/robo.png')
        self.img0 = tkinter.PhotoImage(file='images/numero_0.png')
        self.img1 = tkinter.PhotoImage(file='images/numero_1.png')
        self.img2 = tkinter.PhotoImage(file='images/numero_2.png')
        self.img3 = tkinter.PhotoImage(file='images/numero_3.png')
        self.img4 = tkinter.PhotoImage(file='images/numero_4.png')
        self.img5 = tkinter.PhotoImage(file='images/numero_5.png')
        self.img6 = tkinter.PhotoImage(file='images/numero_6.png')
        self.img7 = tkinter.PhotoImage(file='images/numero_7.png')
        self.img8 = tkinter.PhotoImage(file='images/numero_8.png')
        self.img9 = tkinter.PhotoImage(file='images/numero_9.png')
        self.img10 = tkinter.PhotoImage(file='images/numero_10.png')

        self.lb1 = tkinter.Label(self.fr1, text='BATALHA PAR OU IMPAR', font=fonte1, bg=cinza1, fg=azul2, pady=10)
        self.lb1.pack()

        self.lb_result = tkinter.Label(self.fr1, text='', bg=cinza1, font=fonte1, fg='green')
        self.lb_result.pack()

        self.placar1 = 0
        self.placar2 = 0

        self.lb2 = tkinter.Label(self.fr2, text= '       Jogador          ',font=fonte2, bg=cinza1, fg=azul2, pady=10)
        self.lb2.pack(side='left')

        self.lb3 = tkinter.Label(self.fr2, text=str(self.placar1) + ' x ' + str(self.placar2), font=fonte2, bg=cinza1, fg=azul2, pady=10)
        self.lb3.pack(side='left')

        self.lb4 = tkinter.Label(self.fr2, text='          Computador', font=fonte2, bg=cinza1, fg=azul2, pady=10)
        self.lb4.pack(side='right')

        self.lb_img_player = tkinter.Label(self.fr3, image=self.img_player)
        self.lb_img_player.pack(side='left')

        self.lb_separa = tkinter.Label(self.fr3, text='            ', bg=cinza1)
        self.lb_separa.pack(side='left')

        self.lb_img_pc = tkinter.Label(self.fr3, image=self.img_pc)
        self.lb_img_pc.pack(side='right')

        self.escolha = tkinter.StringVar()

        self.rb_par = tkinter.Radiobutton(self.fr4, text='Par', value='par', variable=self.escolha, bg=cinza1,
                                          fg=azul2, font=fonte2, pady=20)
        self.rb_par.pack(side='left')

        self.rb_impar = tkinter.Radiobutton(self.fr4, text='Ímpar', value='impar', variable=self.escolha, bg=cinza1,
                                          fg=azul2, font=fonte2, pady=20)
        self.rb_impar.pack(side='right')

        self.lb5 = tkinter.Label(self.fr5, text='Número de 01 a 10: ', bg=cinza1, fg=azul2, font=fonte3, width=16, pady=20)
        self.lb5.pack(side='left')

        self.num = tkinter.Entry(self.fr5, font=fonte3, width=2)
        self.num.pack(side='right')

        self.bt_jogar = tkinter.Button(self.fr6, font=fonte3, text='JOGAR', bg=cinza2, relief='raised', border=8,
                                       command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.pack()

        self.lb_erro = tkinter.Label(self.fr6, text='', font=fonte4, bg=cinza1, fg='red')
        self.lb_erro.pack()

    def jogar(self):
        pass

    def jogar2(self, event):
        pass


raiz = tkinter.Tk()

#Definições da janela
raiz.geometry('800x610+300+30')
raiz.iconbitmap('images/ninja.ico')
raiz.title('Jogo de Par ou Impar')
raiz['bg'] = cinza1

janela = Janela(raiz)

raiz.mainloop()