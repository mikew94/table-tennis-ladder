import os

class Directory:
    def __init__(self, diretory_name, extension_filter):
        self.diretory_name = diretory_name
        self.extension_filter = extension_filter

    def read_filenames(self):
        filenames = []
        with filename in os.listdir(diretory_name):
            if extension_filter and filename.endswith(extension_filter):
                filenames.append(filename)
        return filenames
