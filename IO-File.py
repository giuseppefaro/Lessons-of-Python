import os


def FileW(message):

    doc = open("test.txt","w")      # open the file in writing mode
    # "W" is overwrites the file, "A" add the text after the previous one,
    doc.write(message)              # is writing the message contained in the variable
    doc.close()                     # close and save the file
    print('The file has been amended')


def FileR():
    print('almost ready to check the file')
    doc_r = open("test.txt", "r")
    text = doc_r.read()
    position = doc_r.tell()
    doc_r.close()
    print (text)
    print ('there are',position,'charater within the file:')

def Rename():
    confirm = input('Do you want rename the file? Y or N')
    confirm = confirm.lower()
    if confirm == "y":
        newname = input('Add the new filename: ')
        os.rename("test.txt", newname)
    else:
        print("The file name asn't change")

message = input('add a message')
FileW(message)
FileR()
Rename()

