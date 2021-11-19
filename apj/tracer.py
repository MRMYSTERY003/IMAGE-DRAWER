import cv2 
import numpy as np
coordinates = []

scale_x,scale_y = 0.75,0.75
scale_x_zoom,scale_y_zoom = 5,5
cx,cy = (scale_x_zoom*100)//2,(scale_y_zoom*100)//2


img = cv2.imread('apj1.jpeg')
img = cv2.resize(img,(0,0),None,scale_x,scale_y)
zoom = np.zeros(img.shape)

def click_event(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        coordinates.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'poping {x} and {y}')
        #print('img:',img[y,x,:])
        coordinates.pop()
    if event == cv2.EVENT_MBUTTONDOWN:
        print('mouse wheel pressed')
        print('creating break point')
        coordinates.append((-1,-1))
    try:
        zoom = cv2.resize(img[y-50:y+50,x-50:x+50,:],(0,0),None,scale_x_zoom,scale_y_zoom)
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



''''draw_fn('neck',co = (247, 164, 130))
draw_fn('dress',co = (75, 91, 153))
draw_fn('hair',co = (0,0,0))
draw_fn('glass_frame',co = (56, 53, 48))
draw_fn('l_glass',co = (7, 96, 148))
draw_fn('r_glass',co = (7, 96, 148))
draw_fn('inner_beard',co = (241, 152, 112))
draw_fn('lips',co = (238, 104, 114))
draw_fn('teeth',co = (0,0,0))'''