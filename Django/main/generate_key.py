import os
from django.core.management.utils import get_random_secret_key

class Key():
    def __init__(self):
        if not(self.VerifyKey()):
            self.CreateKey()
        self.KEY = self.ReadKey()
        
    # Verify if file exists
    def VerifyKey(self):
        if os.path.exists("key.txt"):
            return True
        return False

    # Create a new key
    def CreateKey(self):
        with open("key.txt", "w") as f: f.write(get_random_secret_key())
    
    # Read a key
    def ReadKey(self):
        with open("key.txt", "r") as f: return f.readline()

    # Get a key
    def GetKey(self):
        return self.KEY