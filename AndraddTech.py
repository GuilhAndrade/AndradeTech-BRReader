import qrcode       # Permite usar a biblioteca "qrcode" sem isso daria erro.
from PIL import ImageTk  # Aqui eu pego sómente a ferramenta "ImageTk" que é a ferramenta q mostra imagem dentro do "tkinter", O "PIL" tem farias ferramenta, ali eu disse q queria uma em especifico.
import tkinter as tk # É a ferramneta q cria janela, e eli eu digo q vou resumir "tkinter" para "tk" para ficar mais limpo a leitura e digitaçao.
import pyperclip # essa ferramenta le oq esta no "Ctrl + C" do ususario.
import time
LARGURA = 108
print("\033[97m")
print("╔" + "═" * (LARGURA - 2) + "╗")
print("║" + "ANDRADE TECH".center(LARGURA - 2) + "║")
print("║" + "Leitor Inteligente de BRs".center(LARGURA - 2) + "║")
print("║" + "           Desenvolvido por Guilherme De Andrade".center(LARGURA - 13) + "Version 1.4║")
print("╚" + "═" * (LARGURA - 2) + "╝")
print("\033[0m")
print()

print()
print()

print("\033[97mOpaaa, Tudo Bem??\033[97m")
print("\033[97mMeu Analista Lindo, Vamos começar!!\033[97m")
print("\033[33mLEMBRETE\033[0m: \033[35mA janela do QRcode pode estar atrás desta janela após iniciar. Fique Atento ao iniciar!!\033[35m")
print('\033[33mATENÇÂO\033[0m: \033[34mNão precisa colar "Ctrl + V"! Apenas copie as BRs onde quer q for, e de ENTER no programa!!\033[34m')
print('\033[33mMODO DE USO\033[0m: \033[32mESPAÇO = Próxima BR\033[0m | \033[31mBACKSPACE = BR anterior\033[0m')
print()

while True:
    input('\033[97mApós ter copiado Clique\033[97m \033[32mENTER\033[0m\033[97m:\033[97m ') # Aqui eu falo para o Analista ou operador do programa por as BRs.
    brs_acumuladas = pyperclip.paste() # Assim q ele cliclar isso pega oq esta no "Ctrl + C" do ususario.
    brs_acumuladas = brs_acumuladas.replace("\n", " ").replace("\t", " ").replace("\r", " ").strip()
    brs_acumuladas_verificar = brs_acumuladas.replace(" ", "").isalnum()
    inicio = time.perf_counter()
    if brs_acumuladas_verificar == True:
        break
    print('ERRO: Analista!! Você copiou errado, tem algum ".", "," ou caracter especial noque você copiou. Copie novamente e de ENTER!')
    print()
print()
print()

lista_brs = brs_acumuladas.split() # tranformo a as BRs coladas em uma lista onde cada BR vira um item.
quantidade_de_br = len(lista_brs)
indice = 0   # Começa mostrando a primeira BR da lista
print(f"Cadastramos \033[32m{quantidade_de_br}\033[0m BRs.")

br_geradas = f"\033[32m{indice + 1}\033[0m"

def mostrar_br(): # Essa função atualiza a tela

    global indice, img_tk # Usa o índice global e mantém a imagem img_tk viva para aparecer no Tkinter.

    br = lista_brs[indice] # Pega primeiro item da lista.

    img = qrcode.make(br) # Manda fazer um QRcode com o texto na variavel "br".
    img_tk = ImageTk.PhotoImage(img) # O "tkinter" nao sabe mostrar este tipo de imagem "img" Então aqui to covertendo ela para uma forma q ele entenda e consiga mostrar.

    texto.config(text=f"BR: {br}\n{indice + 1} de {quantidade_de_br}\n{((indice + 1) / quantidade_de_br) * 100:.0f}% Concluido")# Coloca um texto na tela, é tipo um "print".

    qr.config(image=img_tk) # Atualiza a imagem mostrada no Label do QR Code.



def proxima_br(space):  # Essa função é chamada quando apertar espaço

    global indice # Pega a variavel "indice" fora da função e coloca dentro.

    indice += 1

    # Se acabou a lista fecha o programa
    if indice >= len(lista_brs):
        janela.destroy()
        return 

    mostrar_br()


def voltar_br(backspace):  # Essa função é chamada quando apertar espaço

    global indice # Pega a variavel "indice" fora da função e coloca dentro.

    indice -= 1

    
    if indice < 0:
        indice = 0
        return 
    mostrar_br()


janela = tk.Tk()# Cria uma nova janela q vai mostrar o QRcode/ tipo abrir um programa.

janela.title("Leitor de BR") # Titulo da janela.

# Cria o Label do texto
texto = tk.Label(janela, font=("Arial", 14))
texto.pack() # Coloca o texto do "Label" dentro da janela.

qr = tk.Label(janela) # Cria o "Label"" da imagem vazio.
qr.pack()# Coloca o "Label" imagem na tela.

instrucoes = tk.Label(janela, font=("Arial", 14), text="ESPAÇO → Próxima | BACKSPACE → Anterior")
instrucoes.pack()

mostrar_br() # Executa a funçao, mostrando a primeira BR.

janela.bind("<space>", proxima_br) # Quando apertar espaço chama a função proxima_br

janela.bind("<BackSpace>", voltar_br)

janela.mainloop()# Mantém a janela aberta

fim = time.perf_counter()

tempo = (inicio - fim) * -1
tempo_minutos = tempo // 60
tempo_segundos = tempo % 60

print()

while True:
    print(f"\033[33mAcabou!!!!!\033[0m Você demorou \033[32m{tempo_minutos:.0f}\033[0m minutos e \033[32m{tempo_segundos:.0f}\033[0m segundos para percorrer todos os \033[32m{len(lista_brs)}\033[0m BRs!!")
    if True:
      input("Clique 'ENTER' para fechar o programa: ")
    break