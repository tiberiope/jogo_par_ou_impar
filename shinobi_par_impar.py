import tkinter
from constantes import *
import random
import tkinter.messagebox

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

        self.fr7 = tkinter.Frame(raiz, bg=cinza1)
        self.fr7.pack()

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

        self.lb1 = tkinter.Label(self.fr1, text='BATALHA DE PAR OU ÍMPAR', font=fonte1, bg=cinza1, fg=azul2, pady=10)
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

        self.lb5 = tkinter.Label(self.fr5, text='Número de 0 a 10: ', bg=cinza1, fg=azul2, font=fonte3, width=16, pady=20)
        self.lb5.pack(side='left')

        self.num_player = tkinter.Entry(self.fr5, font=fonte3, width=2)
        self.num_player.pack(side='right')

        self.bt_jogar = tkinter.Button(self.fr6, font=fonte3, text='JOGAR', bg=cinza2, relief='raised', border=8,
                                       command=self.jogar, width= 8, height=1)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack(side='left')

        self.lb_vazio = tkinter.Label(self.fr6, text='   ', bg=cinza1, fg=azul2, font=fonte3)
        self.lb_vazio.pack(side='left')

        self.bt_restart = tkinter.Button(self.fr6, font=fonte3, text='RESTART', bg=cinza2, relief='raised', border=8,
                                         width=8, height=1, command=self.resetar)
        self.bt_restart.bind('<Return>', self.resetar2)
        self.bt_restart.pack(side='right')

        self.lb_erro = tkinter.Label(self.fr7, text='', font=fonte4, bg=cinza1, fg='red', pady=12)
        self.lb_erro.pack()

    def jogar(self):
        try:
            escolha = self.escolha.get()
            self.lb_result['text'] = ''

            if escolha != '':
                num_player = int(self.num_player.get())
                num_robo = random.randrange(0, 11)
                self.lb_erro['text'] = ''
                self.lb_erro.pack()

                #mão do player.
                if num_player == 0:
                    self.lb_img_player['image'] = self.img0
                    self.lb_img_player.pack()

                elif num_player == 1:
                    self.lb_img_player['image'] = self.img1
                    self.lb_img_player.pack()

                elif num_player == 2:
                    self.lb_img_player['image'] = self.img2
                    self.lb_img_player.pack()

                elif num_player == 3:
                    self.lb_img_player['image'] = self.img3
                    self.lb_img_player.pack()

                elif num_player == 4:
                    self.lb_img_player['image'] = self.img4
                    self.lb_img_player.pack()

                elif num_player == 5:
                    self.lb_img_player['image'] = self.img5
                    self.lb_img_player.pack()

                elif num_player == 6:
                    self.lb_img_player['image'] = self.img6
                    self.lb_img_player.pack()

                elif num_player == 7:
                    self.lb_img_player['image'] = self.img7
                    self.lb_img_player.pack()

                elif num_player == 8:
                    self.lb_img_player['image'] = self.img8
                    self.lb_img_player.pack()

                elif num_player == 9:
                    self.lb_img_player['image'] = self.img9
                    self.lb_img_player.pack()

                elif num_player == 10:
                    self.lb_img_player['image'] = self.img10
                    self.lb_img_player.pack()
                else:
                    self.lb_img_player['image'] = self.img_player
                    self.lb_img_player.pack()
                    self.lb_img_pc['image'] = self.img_pc
                    self.lb_img_pc.pack()
                    self.lb_erro['text'] = 'Insira um número de 0 a 10!'
                    self.lb_erro.pack()

                #mão do robô.
                if (num_player >= 0) and (num_player <= 10):
                    if num_robo == 0:
                        self.lb_img_pc['image'] = self.img0
                        self.lb_img_pc.pack()

                    elif num_robo == 1:
                        self.lb_img_pc['image'] = self.img1
                        self.lb_img_pc.pack()

                    elif num_robo == 2:
                        self.lb_img_pc['image'] = self.img2
                        self.lb_img_pc.pack()

                    elif num_robo == 3:
                        self.lb_img_pc['image'] = self.img3
                        self.lb_img_pc.pack()

                    elif num_robo == 4:
                        self.lb_img_pc['image'] = self.img4
                        self.lb_img_pc.pack()

                    elif num_robo == 5:
                        self.lb_img_pc['image'] = self.img5
                        self.lb_img_pc.pack()

                    elif num_robo == 6:
                        self.lb_img_pc['image'] = self.img6
                        self.lb_img_pc.pack()

                    elif num_robo == 7:
                        self.lb_img_pc['image'] = self.img7
                        self.lb_img_pc.pack()

                    elif num_robo == 8:
                        self.lb_img_pc['image'] = self.img8
                        self.lb_img_pc.pack()

                    elif num_robo == 9:
                        self.lb_img_pc['image'] = self.img9
                        self.lb_img_pc.pack()

                    elif num_robo == 10:
                        self.lb_img_pc['image'] = self.img10
                        self.lb_img_pc.pack()

                    resultado = (num_player + num_robo) % 2

                    if (resultado == 1):
                        self.lb_result['text'] = 'DEU ÍMPAR!'

                        if escolha == 'impar':
                            self.placar1 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)

                        else:
                            self.placar2 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)

                    else:
                        self.lb_result['text'] = 'DEU PAR!'

                        if escolha == 'par':
                            self.placar1 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)
                        else:
                            self.placar2 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)

            else:
                self.lb_erro['text'] = 'Escolha PAR ou ÍMPAR!'
                self.lb_erro.pack()

        except:
            self.lb_img_player['image'] = self.img_player
            self.lb_img_player.pack()
            self.lb_img_pc['image'] = self.img_pc
            self.lb_img_pc.pack()
            self.lb_erro['text'] = 'Insira um número de 0 a 10!'
            self.lb_erro.pack()

    def jogar2(self, event):
        try:
            escolha = self.escolha.get()
            self.lb_result['text'] = ''

            if escolha != '':
                num_player = int(self.num_player.get())
                num_robo = random.randrange(0, 11)
                self.lb_erro['text'] = ''
                self.lb_erro.pack()

                # mão do player.
                if num_player == 0:
                    self.lb_img_player['image'] = self.img0
                    self.lb_img_player.pack()

                elif num_player == 1:
                    self.lb_img_player['image'] = self.img1
                    self.lb_img_player.pack()

                elif num_player == 2:
                    self.lb_img_player['image'] = self.img2
                    self.lb_img_player.pack()

                elif num_player == 3:
                    self.lb_img_player['image'] = self.img3
                    self.lb_img_player.pack()

                elif num_player == 4:
                    self.lb_img_player['image'] = self.img4
                    self.lb_img_player.pack()

                elif num_player == 5:
                    self.lb_img_player['image'] = self.img5
                    self.lb_img_player.pack()

                elif num_player == 6:
                    self.lb_img_player['image'] = self.img6
                    self.lb_img_player.pack()

                elif num_player == 7:
                    self.lb_img_player['image'] = self.img7
                    self.lb_img_player.pack()

                elif num_player == 8:
                    self.lb_img_player['image'] = self.img8
                    self.lb_img_player.pack()

                elif num_player == 9:
                    self.lb_img_player['image'] = self.img9
                    self.lb_img_player.pack()

                elif num_player == 10:
                    self.lb_img_player['image'] = self.img10
                    self.lb_img_player.pack()
                else:
                    self.lb_img_player['image'] = self.img_player
                    self.lb_img_player.pack()
                    self.lb_img_pc['image'] = self.img_pc
                    self.lb_img_pc.pack()
                    self.lb_erro['text'] = 'Insira um número de 0 a 10!'
                    self.lb_erro.pack()

                # mão do robô.
                if (num_player >= 0) and (num_player <= 10):
                    if num_robo == 0:
                        self.lb_img_pc['image'] = self.img0
                        self.lb_img_pc.pack()

                    elif num_robo == 1:
                        self.lb_img_pc['image'] = self.img1
                        self.lb_img_pc.pack()

                    elif num_robo == 2:
                        self.lb_img_pc['image'] = self.img2
                        self.lb_img_pc.pack()

                    elif num_robo == 3:
                        self.lb_img_pc['image'] = self.img3
                        self.lb_img_pc.pack()

                    elif num_robo == 4:
                        self.lb_img_pc['image'] = self.img4
                        self.lb_img_pc.pack()

                    elif num_robo == 5:
                        self.lb_img_pc['image'] = self.img5
                        self.lb_img_pc.pack()

                    elif num_robo == 6:
                        self.lb_img_pc['image'] = self.img6
                        self.lb_img_pc.pack()

                    elif num_robo == 7:
                        self.lb_img_pc['image'] = self.img7
                        self.lb_img_pc.pack()

                    elif num_robo == 8:
                        self.lb_img_pc['image'] = self.img8
                        self.lb_img_pc.pack()

                    elif num_robo == 9:
                        self.lb_img_pc['image'] = self.img9
                        self.lb_img_pc.pack()

                    elif num_robo == 10:
                        self.lb_img_pc['image'] = self.img10
                        self.lb_img_pc.pack()

                    resultado = (num_player + num_robo) % 2

                    if (resultado == 1):
                        self.lb_result['text'] = 'DEU ÍMPAR!'

                        if escolha == 'impar':
                            self.placar1 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)
                            self.lb3.pack()
                        else:
                            self.placar2 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)

                    else:
                        self.lb_result['text'] = 'DEU PAR!'

                        if escolha == 'par':
                            self.placar1 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)
                        else:
                            self.placar2 += 1
                            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)

            else:
                self.lb_erro['text'] = 'Escolha PAR ou ÍMPAR!'
                self.lb_erro.pack()

        except:
            self.lb_img_player['image'] = self.img_player
            self.lb_img_player.pack()
            self.lb_img_pc['image'] = self.img_pc
            self.lb_img_pc.pack()
            self.lb_erro['text'] = 'Insira um número de 0 a 10!'
            self.lb_erro.pack()

    def resetar(self):
        resposta = tkinter.messagebox.askquestion('Reiniciar', 'Deseja Reiniciar?')

        if resposta == 'yes':
            self.lb_result['text'] = ''
            self.lb_img_pc['image'] = self.img_pc
            self.lb_img_player['image'] = self.img_player
            self.placar1 = 0
            self.placar2 = 0
            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)
            self.lb_erro['text'] = ''

    def resetar2(self, event):
        resposta = tkinter.messagebox.askquestion('Reiniciar', 'Deseja Reiniciar?')

        if resposta == 'yes':
            self.lb_result['text'] = ''
            self.lb_img_pc['image'] = self.img_pc
            self.lb_img_player['image'] = self.img_player
            self.placar1 = 0
            self.placar2 = 0
            self.lb3['text'] = str(self.placar1) + ' x ' + str(self.placar2)
            self.lb_erro['text'] = ''

raiz = tkinter.Tk()

#Definições da janela
raiz.geometry('800x615+300+30')
raiz.iconbitmap('images/ninja.ico')
raiz.title('Jogo de Par ou Impar')
raiz['bg'] = cinza1

janela = Janela(raiz)

raiz.mainloop()