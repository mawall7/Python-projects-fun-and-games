"9 bitars pussel!. Pusslet använder PIL library för att rotera bilderna (Ctrl) som har ett turnstate. cTYPES används för att hantera klickevents. Bilderna har ett index för att hålla ordning på bildernas position. obs att bilderna behöver finnas i pythonkatalogen
import time
import graphics
from graphics import*
from ctypes import windll, Structure, c_long, byref
import random


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition(): # pointer position unrelative to win
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def mousepos(): # pointer position relative to win
    abs_coord_x = win.master.winfo_pointerx() - win.master.winfo_rootx()# undependent on windowposition relative scree 0,0 is upperleft position 
    abs_coord_y = win.master.winfo_pointery() - win.master.winfo_rooty()
    return {"x":abs_coord_x, "y":abs_coord_y} 



win = GraphWin("Puzzle birdy - by Matte - 2020-07-06",1000,700)
imwall="dunwall.gif"
ims=["bird1.gif","bird2.gif","bird3.gif","bird4.gif","bird5.gif","bird6.gif","bird7.gif","bird8.gif","bird9.gif"]
imsorg=["bird1org.gif","bird2org.gif","bird3org.gif","bird4org.gif","bird5org.gif","bird6org.gif","bird7org.gif","bird8org.gif","bird9org.gif"]
x = 200
#n = 0
#mousepos = ""
pos = 0
done = False

items =[]
d = 0
testim = 0
def Rec():

  for i in (0,167,334):
    print(i)
    y = i
    for d in (0,167,334):
        x = d
        r = Rectangle(Point(x,y),Point(x+167,y+167))
        print(r.getP1().getX(), r.getP1().getY())
        r.setOutline("black")
        r.draw(win)
def newpos():
    x = 1

class imag(Image):
    def __init__(self,x,y,im,indx,active): #inx = indx in matrix that is correct for the picture idx 1 is pict placed to the upperright - from row to column row 1:123 row 2: 456...row 3: 789
        self.x = x
        self.y = y
        self.im = im
        self.i = Image(Point(x,y),self.im) #self.im <- im 
        self.indx = indx
        self.active = active
        imturnstate = 0
        self.imturnstate = imturnstate
    def changeindx(self,newindx):
        self.newindx = newindx
        self.indx = newindx
    def changexy(self,x,y):
        self.i = Image(Point(x,y),self.im)
        self.x = x
        self.y = y
    def changeim(self,im):
        self.im = im
        self.i = Image(Point(self.x,self.y),im)
def randomindxs():
    while len(items)< 9:
        #if len(items)0:
        d = random.randint(1,9)
        while d not in items:  
           items.append(d)
    return items
##    for i in range(0,len(objects)):
##        if objects[i].indx = n:
        

def drawallorder():
         n = 0
         for iy in (0,167,334): # checks for click in a column for column in a 3 x 3 and returns the left upper (x,y) coordinates
                 for ix in (0,167,334):
                        n+= 1
                        for i in range(0,len(objects)):
                            if objects[i].indx == n:
                                objects[i].i.undraw()
                                objects[i].i.draw(win)
                         
                        

def get3x3xy(mcklick):
    for ix in (0,167,334): # checks for click in a column for column in a 3 x 3 and returns the left upper (x,y) coordinates
                if mclick.getX()> ix and  mclick.getX()< ix + 167: 
                  for iy in (0,167,334):
                     if mclick.getY()> iy and  mclick.getY()< iy + 167:
                        x = ix+84
                        y = iy+84
                        print(x,y)
                        im3 = Image(Point(x,y),im5)
                        im3.draw(win) #return x, y
    return x, y


def drawall(ims):
    n = 0
    
    for iy in (0,167,334): # checks for click in a column for column in a 3 x 3 and returns the left upper (x,y) coordinates
                 for ix in (0,167,334):
                        
                        im = ims[n]
                        n+= 1 
                        x = ix+84
                        y = iy+84
                        print(x,y)
                        
                        imx = Image(Point(x,y),im)
                        imx.draw(win)

Rec()
objects = []
# load original org images save (copy) as ims - workingimages
for i in range(0, len(imsorg)):
    import PIL
    from PIL import Image
    im = imsorg[i]
    bi1= Image.open(im)
    bi1.save(ims[i])

import graphics
from graphics import*

d = -1  # draw pictures and gives them an indx
for iy in (0,167,334): # checks for click in a column for column in a 3 x 3 and returns the left upper (x,y) coordinates
                 for ix in (0,167,334):
                        #im = ims[n]
                        d+= 1 
                        x = ix+84
                        y = iy+84
                        #print(x,y)
                        objects.append(imag(x,y,ims[d],d+1,active = False)) #active means a picture is picked up should follow mouse
                        objects[d].i.draw(win)
                        #print(objects[d].i)
#print(objects[0].indx)
searchindx =0
click = 0
activeindx = 0
mem = 0
start = 0
u = 1
goal = False
##**********************************************
##print(("turnstate"),objects[0].imturnstate)
##
##for h in range(0, len(objects)):
##    objects[h].i.undraw()
###randomize order of pic objs,,  r = randomindxs()
##r = randomindxs()
##f =[]
##for h in range(0, len(objects)):
##    f.append([objects[h].x, objects[h].y])
##print("f:",f)
##    
##for h in range(0, len(objects)):
##    objects[h].indx = r[h]
##
##for h in range(0, len(objects)):
##    print("the Objects", objects[h].indx)    
##
##for i in range(1,10):
##    for u in range(0,9):
##        if objects[u].indx == i:
##            xx = f[i-1][0]
##            yy = f[i-1][1]
##            objects[u].changexy(xx,yy)
# load original images imsorg save as ims
##for h in range(0, len(objects)):
##            








#randomize rotation of pictures at start
for h in range(0, len(objects)):
            
            import PIL
            from PIL import Image
            im = objects[h].im
            bi1= Image.open(im)
            d = random.randint(0,3)
            dgrs = [90,180,270,360]
            d = dgrs[d]#dgrs[d]
            bi1 = bi1.rotate(d)
            bi1.save(im)
            import graphics
            from graphics import*
            #print("active",activeindx)
            objects[h].i.undraw()
            #objects[m].i = Image(Point(x,y),im)
            objects[h].changeim(im)
            # eachturn 90 dgr imtrstate (0 degrees = 0...90 dgrs = 1...
            if d== 90: it = 1
            if d== 180: it = 2
            if d== 270: it = 3
            if d== 360: it = 0 
            objects[h].imturnstate = it
            if objects[h].imturnstate > 3: 
                objects[h].imturnstate = 0
            #objects[h].i.draw(win)    
            
    
for h in range(0, len(objects)):
  objects[h].i.draw(win)
  print("imturnstate of %i object %d"%(h, objects[h].imturnstate))          
u = 1

##print("random",r)
##
##drawallorder()
##print(objects[0].i)
##objects[0].changexy(20,20)
##print(objects[0].i)
##print(objects[0].x)
goaln = 0
while True and goal!=9:
      #objects[1].imturnstate = 0
      for i in range (0,9):
          print("imturnstates: indx:%d state: %d" %(objects[i].indx, objects[i].imturnstate))
      #if goal == True:
       #   break
      # check if all pictures are at right position in right way = puzzle solved
      #goaln = 0
      goaln = 0
      for i in range(0,9):
            if objects[i].imturnstate == 0:
              goaln+= 1
            if objects[i].imturnstate!= 0:
              break
      print("goaln",goaln)
      if goaln == 9:
        goaln = 0
        for i in range(0,9):
                  if objects[i].indx == i+1:
                      goaln+= 1
                      if goaln == 9:
                        print("YESGOAL")
                        print("Goaln",goaln)
                  if  objects[i].indx != i+1:
                      break
                  
        if goaln == 9:
            goaln = 0
            for i in range(0,9):
                if objects[i].active == True:
                    break
                if objects[i].active == False:
                      goaln+= 1
                      if goaln == 9:
                  
                          #print("Goal!!!yes")
                          r = Text(Point(200,200),"     You solved it! good job!")
                          r.setFace("arial")
                          r.setSize(30)
                          r.setTextColor("red")
                          r.setStyle("bold")
                          r.draw(win)
                          break
                  

      if ims[0] == ims[0]:
          print("TRUE!")
      else:
              print("FALSE!")
      #pos = winwin).getMouse()
      #while mousepos()!= pos: # mouse pointer (stores x,y in dict) # do as function?
      pos = mousepos()
      #print(mousepos())
      #if done == False:
      x = pos["x"]
      y = pos["y"]

      #im3.undraw();im3 = Image(Point(x,100),im5); im3.draw(win)
      mclick = win.checkMouse()
      
      print(mclick)

      # check for clicks picture is picked
      if mclick!=None:
             start = 1
             searchindx = 0
##            im3.undraw()
             done = True
##            get3x3xy(mclick)
            
             # checks for click in a column for column in a 3 x 3 and returns the indx 1...9
             for iy in (0,167,334):
                     for ix in (0,167,334):
                      searchindx+=1
                      print(searchindx)       
                      if mclick.getY()> iy and  mclick.getY()< iy + 167: #if click in this square searchindx will be = the square number from 1 ..9 
                         if mclick.getX()> ix and  mclick.getX()< ix + 167:
                            xx = ix+84
                            yy = iy+84
                            click+= 1
                            if click == 3: click = 1
                            for h in range(0, len(objects)):
                                objects[searchindx-1].i.undraw()
                                if objects[h].active == True: # searches and makes active obj unactive
                                    objects[h].i.undraw()
                                    #objects[h].indx = searchindx
                                    objects[h].changexy(xx,yy)
                                    #objects[h].i.draw(win)
                                    print("x,y,oi:",objects[h].x,objects[h].y,objects[h].i)
                                    objects[h].i.draw(win)
                                    objects[h].active = False
                                    objects[h].indx = searchindx
                                    mem = h
                                    
                                    u = 2
##                            print(x,y)
##                            print("searchindx",searchindx)
##                            for i in range(0,len(objects)):
##                                       if objects[i].indx == searchindx:
##                                           print("serchinx!!!!",searchindx)
##                                           objects[i].indx = 0
##                                           objects[i].active = True
##                                           print(objects[i].active)
                            for i in range(0,len(objects)):
                               if objects[i].indx == searchindx and objects[i].active == False and i!=mem and start ==1:
                                objects[i].active = True; activeindx= i 
                                #objects[i].indx = 0
                                
                                
                               
                            break

             #Draw all picture objects
             for i in range(0, len(objects)):
                objects[i].i.undraw() 
                objects[i].i.draw(win) 
                
                            
      print("activeindex!",activeindx)                  
      
      key = win.checkKey()
      #print(key) # turn picture 90 degrees
      if key =="Control_R":# and done == False:       
            import PIL
            from PIL import Image
            im = objects[activeindx].im
            bi1= Image.open(im)
            bi1 = bi1.rotate(90)
            objects[activeindx].imturnstate += 1
            if objects[activeindx].imturnstate > 3:
                objects[activeindx].imturnstate = 0
            bi1.save(im)
            import graphics
            from graphics import*
            print("active",activeindx)
            objects[activeindx].i.undraw()
            objects[activeindx].i = Image(Point(x,y),im)
            objects[activeindx].m = im
            objects[activeindx].i.draw(win)    


      if pos!= mousepos() and start!= 0:#active obj(picture) should follow mouse
             
            
                for i in range(0, len(objects)):
                    if objects[i].active == True:
                        
                        objects[i].i.undraw()
                        print(objects[i].i, objects[i].active)
                        objects[i].changexy(pos["x"],pos["y"])
                        objects[i].i.draw(win)

                import graphics
                from graphics import*
                        
                   
                
      if win.checkKey=="q" or goaln == 9: 
        break





##main()
##
##if __name__=="__main__":
##    main()
##    

    
