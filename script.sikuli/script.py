from math import *
region = Region(718,105,482,907)
startX = region.getCenter().getX()
startY = region.getCenter().getY()
hover(region.getCenter())

print(startX, startY)
endButton = find("1460942481244.png") 
click("1460942481244.png")

endX = endButton.getX()
endY = endButton.getY()

diffX = startX - endX
diffY = startY - endY

diffX2 = diffX*diffX
diffY2 = diffY*diffY
dist = sqrt(diffX2+diffY2)

print(endX, endY)
print(diffX2, diffY2)
print(dist)

