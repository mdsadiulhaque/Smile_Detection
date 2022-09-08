#opencv-python pip install
#haaracascade_frontalface_default.xml
#haaracascade_smile.xml



import cv2



cascade_face = cv2.CascadeClassifier('haaracascade_frontalface_default.xml')
cascade_smile = cv2.CascadeClassifier('haaracascade_smile.xml')

cap = cv2.VideoCapture(0)




while True:
    ret, img = cap.read()
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    f = cascade_face.detectMultiScale(
        g,
        scaleFactor =1.3,
        minMeighbors = 5,
        minSize = (30,30)
        )
    
    for (x,y,w,h) in f:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        gray_r = g[y : y+h, x : x+h]
        
        s = cascade_smile.detectMultiScale(
            gray_r,
            scaleFactor =1.5,
            minMeighbors = 15,
            minSize = (25,25),
            
            
            
        )
    
    for i in s:
        if len(s) > 1:
            cv2.putText(img, 'SMILING', (x, y - 30), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),
                        3, cv2.LINE_AA)
            

    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff

    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()


           
    
    
    
    
    
    
    
    
    
    
    