
from ..config import config_window as config

class DebugMenu:
    def __init__(self):
        pass


    def menu(self):
        while True:
            input_debug = input("Commande debug >")

            if input_debug == "exit":
                break
            try: 
                exec(input_debug)
            except Exception as e:
                print(f"Erreur : {e}")