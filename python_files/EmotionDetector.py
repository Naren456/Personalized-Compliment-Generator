import cv2
import numpy as np
from fer import FER
from TTS import TextToSpeech



class Emotion_Detector:
   
    #-creating---class--constructor-#
    def __init__(self):
         #--load--pretrained--modal--face--detection--#
        cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

        #initial-emotion-detection--lib#
        self.emotion_detector = FER()
        
        self.compliment_generator = Compliment()

        self.tts = TextToSpeech()

        self.previous_compliment = None



  
#----------------detect-emotion-----------------#
     
    def detect_emotion(self,image):
        
        if image is None:
            print("Error: Unable to load image.")
            return None
   
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        faces = self.face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=7,minSize=(30,30))
        
        for (x, y, w, h) in faces:
            face_roi = image[y:y+h, x:x+w]
            emotion, score = self.emotion_detector.top_emotion(face_roi)
            if emotion is None or score is None:
                emotion = "Unknown"
                score = 0.0
            compliment = self.compliment_generator.get_compliment(emotion)

            if compliment != self.previous_compliment:
               
                self.tts.speak(compliment)
                self.previous_compliment = compliment

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255,0 ), 2)
            cv2.putText(image, f"{emotion}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255,0), 2)
            #cv2.putText(image, f"Emotion: {emotion}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            cv2.rectangle(image, (0, 0), (image.shape[1] , 50), (0, 0, 0), thickness=cv2.FILLED)
            cv2.putText(image, compliment, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1)

        return image
    


 #---------- resize--image--and--video---frames ----------------#   
    
    def resize_image(self, image, max_width=800):
        (height, width) = image.shape[:2]
        
        if width > max_width:
            aspect_ratio = max_width / float(width)
            new_width = max_width
            new_height = int(height * aspect_ratio)
            resized_image = cv2.resize(image, (new_width, new_height))
            return resized_image
        
        return image 



#-------------detect--emotion--in--image---------------#
    def detect_emotion_in_image(self, image_path):
        
        image = cv2.imread(image_path)
        
        if image is None:
            
            print(f"Error: Unable to load image at {image_path}")
            
            return
        
        image = self.resize_image(image)
        
        image_out = self.detect_emotion(image)

        cv2.imshow("face",image_out)
        
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()


    
#----------detect--emotion--in--Video--Source--------------#

    def detect_emotion_in_video(self,video_source=0):

        cap = cv2.VideoCapture(video_source)

        if not cap.isOpened():
            print("error:could not open camera")
            return
        
        
        
        while cap.isOpened():

            ret , frame = cap.read()
              
            if not ret:
                break
              
            if video_source==0:
                frame = cv2.flip(frame, 1)
            frame = self.resize_image(frame)    

            frame_detect = self.detect_emotion(frame)
           

            cv2.imshow("Face Detection-press q", frame_detect)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                
                break
        
        cap.release()
        
        cv2.destroyAllWindows()

#-----------------Compliments--------------------#
class Compliment:
    def __init__(self):
        self.compliments = {
            'happy': "You're doing great! Keep smiling!",
            'sad': "It's okay to feel down sometimes, but you'll get through this.",
            'angry': "Take a deep breath, you're stronger than you think.",
            'surprise': "Wow! That was unexpected, but you're handling it well!",
            'neutral': "You're calm and collected, stay positive!",
            'disgust': "It's okay, not everything needs to be perfect!",
            'fear': "You're brave for facing your fears, keep going!",
            'unknown': "Keep up the good work, stay strong!"
        }
    
    def get_compliment(self, emotion):
        return self.compliments.get(emotion.lower(), "You're doing your best, keep it up!")
    



#Emotion_Detector().detect_emotion_in_video('Python/myenv/Smart-Mirro/assets/video/video.mp4')
#Emotion_Detector().detect_emotion_in_video('Python/myenv/Smart-Mirro/assets/video/video2.mp4')
#Facial_Emotion_Detector().detect_face_in_image('Mywork/h.jpg')
#Facial_Emotion_Detector().detect_face_in_image('Mywork/img.jpg')
#Emotion_Detector().detect_emotion_in_video()

