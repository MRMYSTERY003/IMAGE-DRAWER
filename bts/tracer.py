import cv2 
import numpy as np
coordinates = []

scale_x,scale_y = 5,5
cx,cy = (scale_x*100)//2,(scale_y*100)//2


img = cv2.imread('bts.jpg')
img = cv2.resize(img,(0,0),None,1.25,1.25)
zoom = np.zeros(img.shape)

def click_event(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        coordinates.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'poping {x} and {y}')
        #print('img:',img[y,x,:])
        coordinates.pop()
    try:
        zoom = cv2.resize(img[y-50:y+50,x-50:x+50,:],(0,0),None,scale_x,scale_y)
        zoom[cx-3:cx+3,cx-3:cx+3,:] = 0
        cv2.imshow('zoom',zoom)
    except:
        print('out of range!!')




cv2.imshow('test',img)
cv2.setMouseCallback('test',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(coordinates)
file = input('enter the name the file: ')
data = open(f'{file}.txt','w')
for i in coordinates:
    x,y = i
    data.write(str(i)+'\n')
print(f'all the coordinates are save in {file}')
data.close()



