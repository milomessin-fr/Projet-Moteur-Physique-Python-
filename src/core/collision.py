#import divers
import threading

#import de fichiers

class Collision:
    def __init__(self):
        self.running = True
        self.thread = threading.Thread(target=self.test)
        self.thread.start()

    def test(self):
        print("zaezae")
        self.running = False  

    def stop(self):
        self.running = False
        print("ierh")
        self.thread.join() 