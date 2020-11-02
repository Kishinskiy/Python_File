
class File:
    """
    Class for write and read from file
    Usage:
    make new object from this class
    f = File("myFile.txt", "Some Content bin data\n")
    and use class method for write to or read from file

    f.write() - write to file text  "Some Content bin data\n"
    print(f.read()) - read this text from file
    """
    def __init__(self, file_name, *content):
        self.fileName = file_name
        self.data = content
        self.content = ""
        self.content = self.content.join(self.data)

    def read(self):
        """function for read from file."""
        with open(self.fileName, "r") as file:
            return file.read()

    def read_byte(self):
        """function for read bytes from file."""
        with open(self.fileName, "rb") as file:
            return file.read()

    def write(self):
        """function for write to file."""
        with open(self.fileName, "w") as file:
            file.write(self.content)
        return 0

    def write_byte(self):
        """function fo write byte to file."""
        with open(self.fileName, "wb") as file:
            file.write(self.content.encode())
        return 0

    def add(self):
        """function for add new string for file"""
        with open(self.fileName, "a") as file:
            file.write(self.content)
        return 0

    def add_byte(self):
        """function for add new byte to file."""
        with open(self.fileName, "ab") as file:
            file.write(self.content.encode())
        return 0
