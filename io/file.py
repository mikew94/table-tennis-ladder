import os

class File:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        content = ""
        with open(self.filename, "r") as f:
            for line in f:
                content.append(line
        return content

    def write(self, text):
        with open(self.filename, "w") as f:
            f.write(text)
