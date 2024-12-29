from EmotionDetector import Emotion_Detector
#---main----#
EmotionDetection = Emotion_Detector()
print('\n')
print("##-----------Emotion---Detector--------##")
print("1. Emotion detection in image")
print("2. Emotion detection in video")
print("3. Real-time emotion detection")
print("4. Exit")

operation = int(input("Enter Task Number : "))

if operation == 1:
    image_path = input("Enter Image file Path : ")
    EmotionDetection.detect_emotion_in_image(image_path)
elif operation == 2:
    video_path = input("Enter video file path : ")
    EmotionDetection.detect_emotion_in_video(video_path)
elif operation == 3:
     print("Starting Web Cam")
     EmotionDetection.detect_emotion_in_video(0)

