import cv2 as cv
import numpy as np
import sys
import multiprocessing as mp

def decodificar_png(planosB,planosG,planosR,plano_bits,imgname):

    largura = len(planosB[0][0])

    msg_shape = []

    plano = 2
    linha = 0
    coluna = 2

    # ESTRAÇÃO DO TAMANHO DA IMAGEM
    for i in range(4):
        byte = 0
        for bit in range(8):
            if plano%3 == 0:
                byte = int(byte + (2**bit)*planosB[plano_bits][linha][coluna])
            elif plano%3 == 1:
                byte = int(byte + (2**bit)*planosG[plano_bits][linha][coluna])
            else:
                byte = int(byte + (2**bit)*planosR[plano_bits][linha][coluna])
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
        
        msg_shape.append(byte)

    msg_altura = msg_shape[0]*256 + msg_shape[1]
    msg_largura = msg_shape[2]*256 + msg_shape[3]

    img_ravel = []

    for i in range(msg_largura*msg_altura):
        byte = 0
        for bit in range(8):
            if plano%3 == 0:
                byte = int(byte + (2**bit)*planosB[plano_bits][linha][coluna])
            elif plano%3 == 1:
                byte = int(byte + (2**bit)*planosG[plano_bits][linha][coluna])
            else:
                byte = int(byte + (2**bit)*planosR[plano_bits][linha][coluna])
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
        
        img_ravel.append(byte)


    img_res = np.zeros((msg_altura,msg_largura))

    for i in range(msg_altura):
        for j in range(msg_largura):
            img_res[i][j] = (img_ravel[i*msg_largura+j])

    img_res = img_res.astype(np.uint8)

    cv.imshow("Imagem codificada",img_res)
    cv.waitKey(0)
    cv.destroyAllWindows()

    cv.imwrite("msgs_encontradas/msg-" + imgname,img_res)

    print("Imagem encontrada salva em:","msgs_encontradas/msg-" + imgname)


def decodificar_txt(planosB,planosG,planosR,plano_bits,imgname):

    largura = len(planosB[0][0])

    tammsg = 0
    plano = 2
    linha = 0
    coluna = 2

    # ESTRAÇÃO DO TAMANHO DA MENSAGEM, POSICIONADO NOS 4 PRIMEIROS BYTES CODIFICADOS
    for i in range(32):
        if plano%3 == 0:
            tammsg = tammsg + (2**i)*planosB[plano_bits][linha][coluna]
        elif plano%3 == 1:
            tammsg = tammsg + (2**i)*planosG[plano_bits][linha][coluna]
        else:
            tammsg = tammsg + (2**i)*planosR[plano_bits][linha][coluna]
            coluna = coluna + 1             
        
        plano = plano + 1

        if coluna == largura:
            coluna = 0
            linha = linha + 1

    plano = 0
    linha = 0
    coluna = 0
    modulo = 0
    msgbytes = []

    for i in range(tammsg+5):
        byte = 0
        for bit in range(8):
            if plano%3 == 0:
                byte = int(byte + (2**bit)*planosB[plano_bits][linha][coluna])
            elif plano%3 == 1:
                byte = int(byte + (2**bit)*planosG[plano_bits][linha][coluna])
            else:
                byte = int(byte + (2**bit)*planosR[plano_bits][linha][coluna])
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
        
        byte = byte.to_bytes(1,'big')
        msgbytes.append(byte)

    del(msgbytes[0])
    del(msgbytes[0])
    del(msgbytes[0])
    del(msgbytes[0])
    del(msgbytes[0])
    msgbytes = b''.join(msgbytes)

    msgfinal = msgbytes.decode("utf-8")

    arqname = "msgs_encontradas/" + imgname.split(".")[0] + "-mensagem.txt"

    arquivo = open(arqname,'w')
    arquivo.write(msgfinal)
    arquivo.close()

    print("Texto encontrado salvo em:",arqname)


def get_tipo(planosB,planosG,planosR,plano_bits):

    largura = len(planosB[0][0])

    plano = 0
    linha = 0
    coluna = 0

    tipo_bytes = 0

    # ESTRAÇÃO DO TAMANHO DA MENSAGEM, POSICIONADO NOS 4 PRIMEIROS BYTES CODIFICADOS
    for i in range(8):
        if plano%3 == 0:
            tipo_bytes = tipo_bytes + (2**i)*planosB[plano_bits][linha][coluna]
        elif plano%3 == 1:
            tipo_bytes = tipo_bytes + (2**i)*planosG[plano_bits][linha][coluna]
        else:
            tipo_bytes = tipo_bytes + (2**i)*planosR[plano_bits][linha][coluna]
            coluna = coluna + 1             
        
        plano = plano + 1

        if coluna == largura:
            coluna = 0
            linha = linha + 1

    if tipo_bytes == 0:
        return "txt"
    elif tipo_bytes == 1:
        return "png"
    else:
        return False


def codificar_mp_txt(imgname,msgname,plano_bits):

    imgpath = "img/" + imgname

    img = cv.imread(imgpath)

    arq = open("msg/" + msgname,'r')
    lines = arq.readlines()
    msg = ""

    for i in lines:
        msg = msg + i
    arq.close()

    if len(msg) > img.shape[0]*img.shape[1]*3/8:
        print("A imagem que deseja codificar não cabe nessa imagem :(")
        exit()
    else:
        print("Codificando texto dentro de imagem") 

    msgbits = converte_bits(msg)

    msgbits.insert(0,[0,0,0,0,0,0,0,0])         # PRIMEIRO BYTE INFORMA O TIPO DE ARQUIVO CODIFICADO
    
    altura, largura, bandas = img.shape

    imgB = img[:,:,0]           # AZUL  
    imgG = img[:,:,1]           # VERDE
    imgR = img[:,:,2]           # VERMELHO

    planosR = []
    planosG = []
    planosB = []

    for bit in range(8):
        aux = ((imgB/(2**bit))%2).astype(np.uint8)
        planosB.append(aux)

        aux = ((imgG/(2**bit))%2).astype(np.uint8)
        planosG.append(aux)

        aux = ((imgR/(2**bit))%2).astype(np.uint8)
        planosR.append(aux)

    plano = 0
    linha = 0
    coluna = 0

    for i in msgbits:
        for j in i:
            if plano%3 == 0:
                planosB[plano_bits][linha][coluna] = j
            elif plano%3 == 1:
                planosG[plano_bits][linha][coluna] = j
            else:
                planosR[plano_bits][linha][coluna] = j
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
            

    newimg = np.zeros(img.shape)

    parent_connB, child_connB = mp.Pipe()
    parent_connG, child_connG = mp.Pipe()
    parent_connR, child_connR = mp.Pipe()

    p_blue = mp.Process(target = unir_planos, args = (planosB,child_connB,))
    p_green = mp.Process(target = unir_planos, args = (planosG,child_connG,))
    p_red = mp.Process(target = unir_planos, args = (planosR,child_connR,))

    p_blue.start()
    p_green.start()
    p_red.start()

    planoB = parent_connB.recv()
    planoG = parent_connG.recv()
    planoR = parent_connR.recv()

    newimg[:,:,0] = planoB[:,:]
    newimg[:,:,1] = planoG[:,:]
    newimg[:,:,2] = planoR[:,:]

    respath = "imgs_codificadas/" + msgname.split(".")[0] + "-" + str(plano_bits) + "-" + imgname

    cv.imwrite(respath,newimg)

    print("Imagem codificada salva em:",respath)


def codificar_txt(imgname,msgname,plano_bits):

    imgpath = "img/" + imgname
    img = cv.imread(imgpath)

    arq = open("msg/" + msgname,'r')
    lines = arq.readlines()
    msg = ""

    for i in lines:
        msg = msg + i
    arq.close()

    if len(msg) > img.shape[0]*img.shape[1]*3/8:
        print("A imagem que deseja codificar não cabe nessa imagem :(")
        exit()
    else:
        print("Codificando texto dentro de imagem") 

    # CONVERTE A MENSAGEM EM UMA LISTA DE BYTES, ONDE CADA UM É UMA LISTA DE BITS.
    # OS PRIMEIROS BITS SÃO OS MENOS SIGNIFICATIVOS
    msgbits = converte_bits(msg)

    msgbits.insert(0,[0,0,0,0,0,0,0,0])

    

    altura, largura, bandas = img.shape

    imgB = img[:,:,0]           # AZUL  
    imgG = img[:,:,1]           # VERDE
    imgR = img[:,:,2]           # VERMELHO

    planosR = []                # CONTÉM OS PLANOS DE BITS DA BANDA VERMELHA
    planosG = []                # CONTÉM OS PLANOS DE BITS DA BANDA VERDE
    planosB = []                # CONTÉM OS PLANOS DE BITS DA BANDA AZUL


    # SEPARA A IMAGEM EM PLANOS DE BITS PARA CADA BANDA DE COR
    for bit in range(8):
        aux = ((imgB/(2**bit))%2).astype(np.uint8)
        planosB.append(aux)

        aux = ((imgG/(2**bit))%2).astype(np.uint8)
        planosG.append(aux)

        aux = ((imgR/(2**bit))%2).astype(np.uint8)
        planosR.append(aux)



    plano = 0
    linha = 0
    coluna = 0

    # INSERE A MENSAGEM NO PLANO DE BITS ESCOLHIDO, DIVIDINDO DADOS EM TODAS AS BANDAS
    for i in msgbits:
        for j in i:
            if plano%3 == 0:
                planosB[plano_bits][linha][coluna] = j
            elif plano%3 == 1:
                planosG[plano_bits][linha][coluna] = j
            else:
                planosR[plano_bits][linha][coluna] = j
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
            

    newimg = np.zeros(img.shape)

    # REMONTA A IMAGEM
    for i in range(altura):
        for j in range(largura):
            blue = 0
            red = 0
            green = 0
            for bit in range(8):
                blue = (blue + planosB[bit][i][j]*(2**bit))
                green = (green + planosG[bit][i][j]*(2**bit))
                red = (red + planosR[bit][i][j]*(2**bit))


            newimg[i][j][0] = blue
            newimg[i][j][1] = green
            newimg[i][j][2] = red

    respath = "imgs_codificadas/" + msgname.split(".")[0] + "-" + str(plano_bits) + "-" + imgname
    cv.imwrite(respath,newimg)

    print("Imagem codificada salva em:",respath)


def codificar_png(imgname,msgname,plano_bits):

    msgpath = "msg/" + msgname
    imgpath = "img/" + imgname

    #imgmsg = cv.imread(msgpath)[:,:,0]
    imgmsg = cv.imread(msgpath)
    imgmsg = cv.cvtColor(imgmsg, cv.COLOR_BGR2GRAY)

    img = cv.imread(imgpath)

    if imgmsg.shape[0]*imgmsg.shape[1] > img.shape[0]*img.shape[1]*3/8:
        print("A imagem que deseja codificar não cabe nessa imagem :(")
        exit()
    else:
        print("Codificando imagem dentro de imagem")

    altura,largura = imgmsg.shape

    imgmsg = imgmsg.ravel()

    imgmsg = np.insert(imgmsg,0,[1,altura>>8,altura%256,largura>>8,largura%256])

    msgbits = []
    
    for i in imgmsg:
        aux = []
        for bit in range(8):
            aux.append(int(((i/(2**bit))%2)))
        
        msgbits.append(aux)

    altura, largura, bandas = img.shape

    imgB = img[:,:,0]           # AZUL  
    imgG = img[:,:,1]           # VERDE
    imgR = img[:,:,2]           # VERMELHO

    planosR = []
    planosG = []
    planosB = []

    for bit in range(8):
        aux = ((imgB/(2**bit))%2).astype(np.uint8)
        planosB.append(aux)

        aux = ((imgG/(2**bit))%2).astype(np.uint8)
        planosG.append(aux)

        aux = ((imgR/(2**bit))%2).astype(np.uint8)
        planosR.append(aux)

    plano = 0
    linha = 0
    coluna = 0

    for i in msgbits:
        for j in i:
            if plano%3 == 0:
                planosB[plano_bits][linha][coluna] = j
            elif plano%3 == 1:
                planosG[plano_bits][linha][coluna] = j
            else:
                planosR[plano_bits][linha][coluna] = j
                coluna = coluna + 1             
            
            plano = plano + 1

            if coluna == largura:
                coluna = 0
                linha = linha + 1
            

    newimg = np.zeros(img.shape)

    parent_connB, child_connB = mp.Pipe()
    parent_connG, child_connG = mp.Pipe()
    parent_connR, child_connR = mp.Pipe()

    p_blue = mp.Process(target = unir_planos, args = (planosB,child_connB,))
    p_green = mp.Process(target = unir_planos, args = (planosG,child_connG,))
    p_red = mp.Process(target = unir_planos, args = (planosR,child_connR,))

    p_blue.start()
    p_green.start()
    p_red.start()

    planoB = parent_connB.recv()
    planoG = parent_connG.recv()
    planoR = parent_connR.recv()

    newimg[:,:,0] = planoB[:,:]
    newimg[:,:,1] = planoG[:,:]
    newimg[:,:,2] = planoR[:,:]

    respath = "imgs_codificadas/" + msgname.split(".")[0] + "-" + str(plano_bits) + "-" + imgname

    cv.imwrite(respath,newimg)

    print("Imagem codificada salva em:",respath)


def unir_planos(planos,p):
    altura, largura = planos[0].shape
    saida = np.zeros((altura,largura))
    for i in range(altura):
        for j in range(largura):
            pixel = 0

            for bit in range(8):
                pixel = (pixel + planos[bit][i][j]*(2**bit))

            saida[i][j] = pixel
    
    p.send(saida)
    return


def converte_bits(entrada):
    codificada = entrada.encode("utf-8")
    tam = len(codificada)
    saida = []

    aux = []
    for i in range(32):
        aux.append(int(((tam/(2**i))%2)))
    saida.append(aux)

    
    for c in codificada:
        aux = []
        for i in range(8):
            aux.append(int(((c/(2**i))%2)))
        saida.append(aux)
    return saida