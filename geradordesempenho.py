from time import sleep
from tkinter import *
interface=Tk()
lw=300
aw=300
lt=interface.winfo_screenwidth()
at=interface.winfo_screenheight()
posx=lt/2-lw/2
posy=at/2-aw/2
interface.geometry('%dx%d+%d+%d'%(lw,aw,posx,posy))
interface.wm_minsize(width=300, height=300)
interface.wm_maxsize(width=300, height=300)

temp10=float()
seconds=int()
seg=int()
textmed=StringVar()
numsre=StringVar()
hora=IntVar()
minuto=IntVar()
segundos=IntVar()
decque=bool()
tempcicl=1
varhabili=bool()
numsre.set('00:00:00')


#def funpasso(v):
#    global tempcicl
#    tempcicl=float(v)
def quebra():
    global decque
    print(decque)
    decque=True

def ativar():
    global decque
    decque=False
    textmed.set('')
    ini.germedia()

class ini:
    def __init__(self) -> None:
        pass
    def germedia():   
        if (int(numq.get()))>0 and (float(tp.get()))>0:
            maisde1h=bool()
            valn=int(numq.get())
            valt=float(tp.get())
            temp10=(valn*valt)
            hor1=temp10/60
            seconds=temp10*60
            seg=seconds%60
            resthor=temp10%60
            # Fazer pro caso de resto dos minutos e dos segundos for diferente de 0
            if hor1<=99:
                if temp10>=60 and resthor==0:
                    maisde1h=True
                    textmed.set(str(10.0))
                    numsre.set(f'{int(hor1):02d}:{0:02d}:{0:02d}')
                    interface.update()
                    sleep(tempcicl)
                elif temp10>60 and resthor!=0:
                    maisde1h=True
                    if seg!=0:
                        for segs in range(int(seg),-1,-1):
                            textmed.set(str(10.0))
                            if decque==False:
                                print(f'{int(hor1)} : {int(resthor)} : {segs}')
                                print(decque)
                                numsre.set(f'{int(hor1):02d}:{int(resthor):02d}:{segs:02d}')
                                interface.update()
                                sleep(tempcicl)
                            else:
                                break
                        for res in range(int(resthor)-1,-1,-1):
                            for segs in range(59,-1,-1):
                                textmed.set(str(10.0))
                                if decque==False:
                                    print(f'{int(hor1)} : {res} : {segs}')
                                    print(decque)
                                    numsre.set(f'{int(hor1):02d}:{res:02d}:{segs:02d}')
                                    interface.update()
                                    sleep(tempcicl)
                                else:
                                    break
                        temp10-=resthor
                        seconds-=seg 
                    else:
                        numsre.set(f'{int(hor1):02d}:{int(resthor):02d}:{0:02d}')
                        textmed.set(str(10.0))
                        interface.update()
                        sleep(tempcicl)
                        for res in range(int(resthor)-1,-1,-1):
                            for segs in range(59,-1,-1):
                                if decque==False:
                                    print(f'{int(hor1)} : {res} : {segs}')
                                    print(decque)
                                    numsre.set(f'{int(hor1):02d}:{res:02d}:{segs:02d}')
                                    interface.update()
                                    sleep(tempcicl)
                                else:
                                    break
                        temp10-=resthor
                        seconds-=seg  
                else:
                    for segs in range(int(seg),-1,-1):
                        textmed.set(str(10.0))
                        if decque==False:
                            print(f'{0} : {int(temp10)} : {segs}')
                            print(decque)
                            numsre.set(f'{0:02d}:{int(temp10):02d}:{segs:02d}')
                            interface.update()
                            sleep(tempcicl)
                        else:
                            break
                    seconds-=seg
                if maisde1h==True:
                    for hor in range(int(hor1)-1,-1,-1):
                        for mim in range(int(int(temp10)/int(hor1))-1,-1,-1): 
                            if decque==False:   
                                for segs in range(59,-1,-1):
                                    if decque==False:
                                        print(f'{hor} : {mim} : {segs}')
                                        print('temp10>60')
                                        numsre.set(f'{hor:02d}:{mim:02d}:{segs:02d}')
                                        interface.update()
                                        sleep(tempcicl)
                                    else:
                                        break
                            else:
                                break
                else:
                    for mim in range(int(temp10)-1,-1,-1): 
                            if decque==False:   
                                for seg in range(int((seconds)/int(temp10))-1,-1,-1):
                                    if decque==False:
                                        print(f'{0} : {mim} : {seg}')
                                        print('temp10<60')
                                        numsre.set(f'{0:02d}:{mim:02d}:{seg:02d}')
                                        interface.update()
                                        sleep(tempcicl)
                                    else:
                                        break
                            else:
                                break
                maisde1h=False
                re.resuf()
# x = tempo para resolver 
#-1/3x + 10 = nota
class re:
    def __init__(self) -> None:
        pass
    def resuf():
        a=10
        valt2=float(tp.get())
        valtn2=int(numq.get())
        seconds2=(valt2*valtn2)*60
        for hora1 in range(0,100):
            for mim1 in range(0,60):     
                if decque==False:   
                    for seg1 in range(0,60):
                        if decque==False:
                            print(f'{hora1} : {mim1} : {seg1}')
                            print(decque)
                            numsre.set(f'{hora1:02d}:{mim1:02d}:{seg1:02d}')
                            seconds2-=1
                            a-=((10/(valt2*valtn2))/60)
                            if seconds2<0:
                                textmed.set(str(0.0))
                                quebra()
                                break
                            print(a)
                            if seconds2>0:
                                textmed.set(str(f'{a:.1f}'))
                            interface.update()
                            sleep(tempcicl)
                        else:
                            break
                else:
                    break
interface.title('Gerador de Desempenho')
ndquest=Label(interface, text='N° de questões')
numq=Entry(interface)
tepq=Label(interface, text='Tempo para cada questão(min)')
tp=Entry(interface)
inic=Button(interface, 
            text='INICIAR', 
            command=lambda:ativar())
stop=Button(interface,
            text='PARAR',
            command=lambda:quebra())
relog=Label(interface, font='Arial 20', textvariable=numsre)
medi=Label(interface, font='Arial 15' ,textvariable=textmed)
defiper=Label(interface,text='Definir período:', font='Arial 10')
#passo=Scale(interface, from_=1, to=0.00000001,  
#            orient=HORIZONTAL, 
#            resolution=0.0002,
#            command=funpasso)
ndquest.pack()
numq.pack()
tepq.pack()
tp.pack()
inic.pack()
relog.pack()
stop.pack()
medi.pack()
#defiper.pack(anchor=SW)
#passo.pack(anchor=SW)
interface.mainloop()