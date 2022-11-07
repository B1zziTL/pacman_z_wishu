#vlozenie modulov
import tkinter
import random

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=300,height=300,bg='white')
canvas.pack()

#premenne a zoznamy
x = 10
y = 10
smer = 'd'
suradnice_x = []
suradnice_y = []
jablcka = []
pouzite = []
n = 3
zmazane = 0

def zrutik(): #funkcia na vykreslovanie zruta a mazanie jablcok
    #globalne premenne
    global x,y
    global nieco, n
    global zmazane, suradnicky

    #vymazanie povednej pozicie zruta
    canvas.delete('zruto')

    #podmienky na vymazavanie jablcok
    for i in range(3):
        #ak sa zrut nachadza v blizkosti -+15, vymaze jablcko
        if x >= (suradnice_x[i] - 15 ) and x <= (suradnice_x[i] + 15 ):
            if y >= (suradnice_y[i] - 15 ) and y <= (suradnice_y[i] + 15 ):
                #ak dana suradnica este nebola pouzita
                if not i in pouzite:
                    daco = jablcka[i]
                    canvas.delete(daco)

                    #nastavenie pomocnych premennych
                    zmazane = 1

                    #priradenie suradnice do pouzitych
                    pouzite.append(i)

                    #prerusenie akcie
                    break

    #pomocna podmienka na spravne fungovanie
    if zmazane == 1:
        n -= 1
        zmazane = 0

    #ak je smer "w", zrut pojde hore (pripadne odznova)
    if smer == 'w':
        canvas.create_oval(x,y,x+30,y+30,fill='blue',tags='zruto')
        if y >= 0:
            y -= 30
        else:
            y = 300
    #ak je smer "a", zrut pojde dolava (pripadne odznova)
    if smer == 'a':
        canvas.create_oval(x,y,x+30,y+30,fill='blue',tags='zruto')
        if x >= 0:
            x -= 30
        else:
            x = 300
    #ak je smer "s", zrut pojde dole (pripadne odznova)
    if smer == 's':
        canvas.create_oval(x,y,x+30,y+30,fill='blue',tags='zruto')
        if y <= 300:
            y += 30
        else:
            y = 0
    #ak je smer "d", zrut pojde doprava (pripadne odznova)
    if smer == 'd':
        canvas.create_oval(x,y,x+30,y+30,fill='blue',tags='zruto')
        if x <= 300:
            x += 30
        else:
            x = 0
            
    #kontrolna podmienka, ci su este jablcka
    if n > 0:
        #vykresli sa zrut
        canvas.after(500,zrutik)
    #ak uz nie su jablcka
    else:
        #zmazanie vsetkeho 
        canvas.delete('all')
        
        #zobrazenie textu
        canvas.create_text(150,150,text='VYHRAL/A SI!',font='Arial 20')

def jabka(): #funkcia na vykreslenie jablcok
    #globalna premenna
    global nieco

    for i in range(3):
        #nakreslenie zadaneho poctu jablcok
        x1 = random.randint(15,269)
        y1 = random.randint(15,269)

        #oznacenie jablcok (tags) pre vyuzitie pri vymazavani
        nieco = 'jabko'+str(i)
        jablcka.append(nieco)
        canvas.create_oval(x1,y1,x1+30,y1+30,fill='red',tags=nieco)

        #ulozenie hodnot do zoznamov
        suradnice_x.append(x1)
        suradnice_y.append(y1)
        
#v pripade stlacenia pismena "w" sa na stavi premenna smer
def hore(event):
    global smer
    smer = 'w'

#v pripade stlacenia pismena "s" sa na stavi premenna smer   
def dole(event):
    global smer
    smer = 's'

#v pripade stlacenia pismena "d" sa na stavi premenna smer    
def doprava(event):
    global smer
    smer = 'd'

#v pripade stlacenia pismena "a" sa na stavi premenna smer    
def dolava(event):
    global smer
    smer = 'a'

#privolanie funkcii
jabka()
zrutik()

#nastavenie klavesov na pohyb
canvas.bind_all('w',hore)
canvas.bind_all('s',dole)
canvas.bind_all('a',dolava)
canvas.bind_all('d',doprava)
