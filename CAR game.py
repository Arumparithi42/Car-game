import pygame as pg
import random
import time
def CARGAME():
           pg.init()
           win=pg.display.set_mode((500,500))
           pg.display.set_caption("CAR GAME")

           white=(255,255,255)
           black=(0,0,0)
           red=(255,0,0)
           green=(0,255,0)
           blue=(0,0,255)
           violet=(0,255,255)
           yellow=(255,255,0)
           lblue=(255,0,255)

           carpos=[250,430]
           obj=[random.randrange(0,10)*50,random.randrange(0,1)*50]
           obj2=[random.randrange(0,10)*50,random.randrange(0,1)*50]
           obj3=[random.randrange(0,10)*50,0]
           obj4=[random.randrange(0,10)*50,random.randrange(0,1)*50]
           obj5=[random.randrange(0,10)*50,random.randrange(0,1)*50]
           objspawn=True
           objspawn2=True
           objspawn3=True
           objspawn4=True
           score=0
           flyn=1
           fly=False
           flycount=8

           rpos=[[25,0],[25,130],[25,260],[25,390],[75,30],[75,160],[75,290],[75,420],
                 [125,40],[125,170],[125,300],[125,430],[175,20],[175,150],[175,280],[175,420],
                 [225,10],[225,140],[225,270],[225,400],[275,50],[275,180],[275,310],[275,440],
                 [325,70],[325,200],[325,330],[325,460],[375,60],[375,190],[375,320],[375,450],
                 [425,90],[425,220],[425,350],[425,480],[475,80],[475,210],[475,340],[475,470]]
           n=5
           for i in range(n):
                      scar=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//baby-car.png")
                      win.blit(scar,(100,0))
                      f=pg.font.SysFont("monoco",130)
                      s=f.render("CAR GAME",True,lblue)
                      r=s.get_rect()
                      r.midtop=(250,200)
                      win.blit(s,r)
                      ff=pg.font.SysFont("monoco",30)           
                      ss=ff.render("THE GAME STARTS IN "+str(n)+" SECONDS",True,yellow)
                      rr=ss.get_rect()
                      rr.midtop=(250,400)
                      win.blit(ss,rr)
                      pg.display.flip()
                      time.sleep(1)
                      win.fill(black)
                      if n!=0:
                                 n-=1
                      else:
                                 continue
                      
           def gameover():
                      gsf=pg.font.SysFont("monoco",70)
                      gss=gsf.render("YOUR SCORE is"+str(score),True,violet)
                      gsr=gss.get_rect()
                      gsr.midtop=(250,100)
                      win.blit(gss,gsr)
                      gf=pg.font.SysFont("monoco",120)
                      gs=gf.render("GAME-OVER",True,red)
                      gr=gs.get_rect()
                      gr.midtop=(250,200)
                      win.blit(gs,gr)
                      pg.display.flip()
                      time.sleep(4)
                      pg.quit()
           run=True
           while run:
                      pg.time.delay(50)
                      for event in pg.event.get():
                                 if event.type==pg.QUIT:
                                            run=False
                                            pg.quit()
                                            quit()
                      key=pg.key.get_pressed()
                      if key[pg.K_UP] and carpos[1]>0:
                                 carpos[1]-=5
                      if key[pg.K_DOWN] and carpos[1]<500-50-5-5-5-5:
                                 carpos[1]+=5
                      if not fly:
                                 if key[pg.K_SPACE]:
                                            flyn-=1
                                            fly=True
                      else:
                                 if flyn>0:
                                            if flycount>= 0:
                                                       flycarimg=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//car image-Copy.png")
                                                       flycarpos=[carpos[0]-11,carpos[1]]
                                                       win.blit(flycarimg,(flycarpos[0],flycarpos[1]))
                                                       pg.display.flip()
                                                       pg.display.update()
                                 
                                                       carpos[1]-=flycount**2*0.5
                                                       flycount-=1
                                            else:
                                                       fly=False
                                                       flycount=8
                      if key[pg.K_RIGHT] and carpos[0]<500-50:
                                 carpos[0]+=5
                      if key[pg.K_LEFT] and carpos[0]>0:
                                 carpos[0]-=5
                      if key[pg.K_q]:
                                 run=False
                                 pg.quit()
                                 quit()
                      win.fill(black)
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(0,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(50,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(100,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(150,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(200,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(250,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(300,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//road.png")
                      win.blit(car,(350,0))
                      car=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image/road.png")
                      win.blit(car,(400,0))
                      for pos in rpos:
                                 road=pg.draw.rect(win,(255,255,255),pg.Rect(pos[0]-3,pos[1],5,50))
                                 pos[1]+=10
                                 if pos[1]>500:
                                            pos[1]=-50

                      carimg=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//car image.png")
                      win.blit(carimg,(carpos[0],carpos[1]))
                      width=carimg.get_width()
                      height=carimg.get_height()
                      ecarimg1=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//enemy car2.png")
                      win.blit(ecarimg1,(obj[0],obj[1]))
                      #object speed
                      obj[1]+=20
                      obj2[1]+=10
                      obj3[1]+=25
                      obj4[1]+=15
                      #obj 1
                      if obj[1]>500:
                                 score+=10
                                 flyn+=0.20
                                 flyn=round(flyn,2)
                                 objspawn=False
                      if not objspawn:
                                 obj=[random.randrange(0,10)*50,random.randrange(0,1)*50]
                      objspawn=True
                      #obj 2
                      if score>100:
                                 if obj2[1]>500:
                                            score+=10
                                            objspawn2=False
                                 if not objspawn2:
                                            obj2=[random.randrange(0,10)*50,random.randrange(0,1)*50]
                                 objspawn2=True
                      #obj 3
                      if score>500:
                                 if obj3[1]>500:
                                            score+=10
                                            objspawn3=False
                                 if not objspawn3:
                                            obj3=[random.randrange(0,10)*50,random.randrange(0,1)*50]
                                 objspawn3=True
                      #obj 4
                      if score>1000:
                                 if obj4[1]>500:
                                            score+=10
                                            objspawn4=False
                                 if not objspawn4:
                                            obj4=[random.randrange(0,10)*50,random.randrange(0,1)*50]
                                 objspawn4=True
                      
                      sf=pg.font.SysFont("monoco",25)
                      ss=sf.render("SCORE :"+str(score),True,green)
                      sr=ss.get_rect()
                      sr.midtop=(70,20)
                      win.blit(ss,sr)
                      ff=pg.font.SysFont("monoco",25)
                      fs=ff.render("FLY :"+str(flyn),True,(0,255,255))
                      fr=fs.get_rect()
                      fr.midtop=(450,20)
                      win.blit(fs,fr)
                      pg.draw.line(win,(50,50,50),(0,400),(500,400),3)
                      if score<100:
                                 l=pg.font.SysFont("monoco",25)
                                 ls=l.render("LEVEL 1",True,lblue)
                                 lr=ls.get_rect()
                                 lr.midtop=(250,10)
                                 win.blit(ls,lr)
                      elif score>=100 and score<500:
                                 ll=pg.font.SysFont("monoco",25)
                                 lls=ll.render("LEVEL 2",True,lblue)
                                 llr=lls.get_rect()
                                 llr.midtop=(250,10)
                                 win.blit(lls,llr)
                      elif score>=500 and score<1000:
                                 lll=pg.font.SysFont("monoco",25)
                                 llls=lll.render("LEVEL 3",True,lblue)
                                 lllr=llls.get_rect()
                                 lllr.midtop=(250,10)
                                 win.blit(llls,lllr)
                      else:
                                 llll=pg.font.SysFont("monoco",25)
                                 lllls=llll.render("LEVEL 4",True,lblue)
                                 llllr=lllls.get_rect()
                                 llllr.midtop=(250,10)
                                 win.blit(lllls,llllr)
                      if not fly:
                                 if carpos[1]<obj[1]+50 and carpos[1]+height>obj[1]:
                                            if (carpos[0]>obj[0] and carpos[0]<obj[0]+50 or carpos[0]+width>obj[0] and carpos[0]+width<obj[0]+50)or carpos[0]==obj[0]: 
                                                       gameover()
                                                       n=input("DO YOU WANT TO RESTART :")
                                                       if 'y' in n:
                                                                  CARGAME()
                                                       else:
                                                                  exit()
                                 if score>100:
                                            ecarimg=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//enemy car2.png")
                                            win.blit(ecarimg,(obj2[0],obj2[1]))
                                            if carpos[1]<obj2[1]+50 and carpos[1]+height>obj[1]:
                                                       if (carpos[0]>obj2[0] and carpos[0]<obj2[0]+50 or carpos[0]+width>obj2[0] and carpos[0]+width<obj2[0]+50)or carpos[0]==obj2[0]:
                                                                  gameover()
                                                                  n=input("DO YOU WANT TO RESTART :")
                                                                  if 'y' in n:
                                                                             CARGAME()
                                                                  else:
                                                                             exit()
                                 if score>500:
                                            ecarimg=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//enemy car1.png")
                                            win.blit(ecarimg,(obj3[0],obj3[1]))
                                            if carpos[1]<obj3[1]+50 and carpos[1]+height>obj[1]:
                                                       if (carpos[0]>obj3[0] and carpos[0]<obj3[0]+50 or carpos[0]+width>obj3[0] and carpos[0]+width<obj3[0]+50) or carpos[0]==obj3[0]:
                                                                  gameover()
                                                                  n=input("DO YOU WANT TO RESTART :")
                                                                  if 'y' in n:
                                                                             CARGAME()
                                                                  else:
                                                                             exit()
                                 if score>1000:
                                            ecarimg=pg.image.load("C://Users//Lenovo//Desktop//PYTHON//python games//python image//enemy car3.png")
                                            win.blit(ecarimg,(obj4[0],obj4[1]))
                                            if carpos[1]<obj4[1]+50 and carpos[1]+height>obj[1]:
                                                       if (carpos[0]>obj4[0] and carpos[0]<obj4[0]+50 or carpos[0]+width>obj4[0] and carpos[0]+width<obj4[0]+50) or carpos[0]==obj4[0]:
                                                                  gameover()
                                                                  n=input("DO YOU WANT TO RESTART :")
                                                                  if 'y' in n:
                                                                             CARGAME()
                                                                  else:
                                                                             exit()
                                 pg.display.flip()
                      pg.display.update()
CARGAME()
