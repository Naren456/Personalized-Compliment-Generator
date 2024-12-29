import pyttsx3
import threading
from queue import Queue

class TextToSpeech:
    
#-------Initialize--the--TTS--engine--and--queue---------#
    def __init__(self, rate=150):
 
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)  
        self.speech_queue = Queue(maxsize=1)  
        self.speech_thread = threading.Thread(target=self._process_speech, daemon=True)
        self.running = True
        self.speech_thread.start()


#------Continuously--process--speech--commands--from--the--queue------#
    def _process_speech(self):
        
        while self.running:
            try:
              
                text = self.speech_queue.get(timeout=1)
                if text == "STOP":
                    break
                self.engine.say(text)
                self.engine.runAndWait()
            except:
               
                continue


#------Clear--the--queue--and--immediately--speak--the--latest--text------#.
    def speak(self, text):
        if not self.speech_queue.empty():
            self.clear_queue() 
        self.speech_queue.put(text)


#-----Clear--all--pending--items--in--the--queue-----#
    def clear_queue(self):
        with self.speech_queue.mutex:
            self.speech_queue.queue.clear()
