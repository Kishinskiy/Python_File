from File import File

f = File("myFile.txt", "Some Content bin data\n")

if __name__ == '__main__':
    # print(f.read())

    f.write_byte()
    f.add()
    print(f.read())

    print(help(File))
