#import divers
import threading

#import de fichiers

class Collision:
    def __init__(self): # mettre entity en paramètre
        self.running = True
        #self.entity = entity
        self.verrou = threading.Lock()
        self.thread = threading.Thread(target=self.test)

    def test(self):
        while self.running:
            print("test thread 2")

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self.test, daemon=True)  # recréé proprement
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join() 