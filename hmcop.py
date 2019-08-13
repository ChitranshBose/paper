import csv
import cv2
counter = 0
i = 0
classes=['eat','jump','punch','ride_horse','sit','smoke','throw','turn','walk']
#for files in classes:
with open('C:/Users/lenovo/Desktop/train/train.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        for filename in row:
            print (filename, classes[i])
            cap=cv2.VideoCapture('C:\\Users\\lenovo\\Desktop\\research\\hmdb2\\'+classes[i]+'\\'+filename)
            while cap.isOpened():
                check,frame = cap.read()
                if frame is not None:
                    cv2.imshow('frame', frame)
                    cv2.imwrite('C:\\Users\\lenovo\\Desktop\\train\\'+classes[i]+'\\'+filename+str(counter)+'.jpg',frame)
                    check,frame=cap.read()
                    counter+=1
                    cv2.waitKey(1)
                else:
                    break
        
        i+=1
        
