print("Swaping Files")
print("Choose Two Files & See What Happens!")
print()
# Give files of same extension so they work efficiently

def swapFileData():
    File1 = input("Enter Your File 1 Name: ")
    File2 = input("Enter Your File 2 Name: ")

    data_a = open(File1,'r+')
    data_b = open(File2,'r+')

    content_data_a = data_a.readlines()
    content_data_b = data_b.readlines()


    data_a.seek(0) 
    data_a.truncate() 


    data_b.seek(0) 
    data_b.truncate() 

    data_a.writelines(content_data_b)
    data_b.writelines(content_data_a)
    data_a.close()
    data_b.close()
    print("Work DOne!!")
    print("Check Your Files", end="")
    print()

swapFileData()