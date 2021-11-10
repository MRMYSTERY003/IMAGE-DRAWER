import cv2 
coordinates = []

def click_event(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        coordinates.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f'poping {x} and {y}')
        coordinates.pop()


img = cv2.imread('gojo1.jpg')
img = cv2.resize(img,(0,0),None,0.75,0.75)
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



