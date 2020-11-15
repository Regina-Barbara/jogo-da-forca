print("Bem vindo ao jogo da forca!")
palavra_secreta='banana'
tentantivas=12
letras_descobertas= ['_','_','_','_','_','_']
print("Você tem 12 tentativas para acertar a palavra secreta")
chute=input("Digite uma letra: ")
for letra in palavra_secreta:
    if chute == letra:
        print("Essa letra existe")
    else:
        print('A letra não existe')