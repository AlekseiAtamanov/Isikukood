from datetime import *
from turtle import left


while True:
    ik=input("isikukood: ")
    if len(ik)==11:
        try:            
            ik_list=list(ik)
            if int(ik_list[0]) in [1,2,3,4,5,6]:
                if int(ik_list[0]) in [1,2]:
                    a=1800
                elif int(ik_list[0]) in [3,4]:
                    a=1900
                else:
                    a=2000
                aasta=a+int(ik_list[1]+ik_list[2])
                kuu=int(ik_list[3]+ik_list[4])
                paev=int(ik_list[5]+ik_list[6])
                if datetime(aasta,kuu,paev):
                    s=0
                    for i in range(0,10):
                        s+=(i%9+2)+int(ik_list[i])
                        print(f"{i%9+1}*{int(ik_list[i])}+", end=" ")
                        print (s)                          
                    s=s-(s//11)*11
                    print(s)
                    if s==int(ik_list[10]):
                        print("OK")
                    else:
                        print("Mitte Ok")
                ik3=int(ik[7:10])                
                if ik3>1 and ik3<=10:
                    haigla="Kuressaare Haigla"
                elif ik3>11 and ik3<=19:
                    haigla="Tartu Ulikooli Naistekliinik, Tartumaa, Tartu"
                elif ik3>21 and ik3<=220:
                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sunnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                elif ik3>221 and ik3<=270:
                    haigla="Ida-Viru Keskhaigla (Kohtla-Jarve, endine Johvi)"
                elif ik3>271 and ik3<=370:
                    haigla="Maarjamoisa Kliinikum Tartu, Jogeva Haigla"
                elif ik3>371 and ik3<=420:
                    haigla="Narva Haigla"
                elif ik3>421 and ik3<=470:
                    haigla="Parnu Haigla"
                elif ik3>471 and ik3<=490:
                    haigla="Pelgulinna Sunnitusmaja (Tallinn), Haapsalu haigla"
                elif ik3>491 and ik3<=520:
                    haigla="Jarvamaa Haigla (Paide)"
                elif ik3>521 and ik3<=570:
                    haigla="Rakvere, Tapa haigla"
                elif ik3>571 and ik3<=600:
                    haigla="Valga Haigla"
                elif ik3>601 and ik3<=650:
                    haigla="Viljandi Haigla"
                elif ik3>651 and ik3<=700:
                    haigla="Louna-Eesti Haigla (Voru), Polva Haigla"
                
                print (haigla)
            else:
                print("esimene sumbol/arv on vale")
        except:
            print("Andmetuup on vale, On vaja numbreid sisestada")
    else:
        print("Sumbolite arv peab 11 olema")
