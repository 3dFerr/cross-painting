''' 
sketch to run in Processing IDE - mode: Python
go to https://py.processing.org/tutorials/gettingstarted/ 
for setup processing python enviroment
'''

def setup():
  size(600,300) # you can change the size of window
  background(0) # color background set to black. choose you favorite color

def draw():
    # Colors can be changed. Choose the colors you want
    if mousePressed:
        fill(203,112,255)
    else:
        fill(255)
            
    rectMode(CENTER)
    rect(mouseX, mouseY, 80, 20)
    rect(mouseX, mouseY, 20, 80)
