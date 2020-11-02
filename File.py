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
        self.content = "".join(content)

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
            return file.write(self.content)

    def write_byte(self):
        """function fo write byte to file."""
        with open(self.fileName, "wb") as file:
            return file.write(self.content.encode())

    def add(self):
        """function for add new string for file"""
        with open(self.fileName, "a") as file:
            return file.write(self.content)

    def add_byte(self):
        """function for add new byte to file."""
        with open(self.fileName, "ab") as file:
            return file.write(self.content.encode())
