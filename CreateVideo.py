import os
import cv2


path = "Images"

images = []
list = os.listdir(path)
print(list)

for file in list:
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)


out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

#For SUNSET
#for i in range(0,count-1):

#For SUNRISE
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # releasing the video generated
print("Done")