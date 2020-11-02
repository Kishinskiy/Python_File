from File import File

f = File("myFile.bin", "Some Content bin data\n")

if __name__ == '__main__':
    # print(f.read())

    f.write_byte()
    f.add_byte()
    print(f.read())

