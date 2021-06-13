
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.AylfwQCc9hUQQb1Yn-_LC6AymswddWrWcJJ3VJOgERovHWPmn7lfwgPHnMmLcHTNTawKkBlqGUzMtTQF2aNne0m7u8JkUpClDaS0pwZfZo6pDWpsGWr5ebQ-VP3JR1oZ6SBA-BQ'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer: ")
    #enter the full path to upload the file including the file name that we want once uploaded
    file_to = input("Enter the full path to upload in dropbox: ")

    transferData.upload_file(file_from,file_to)

    print("file has been moved!")

if __name__ == '__main__':
    main()

#C:\Users\DeLL\Dropbox\test
#F:\F Drive\coding\class files\C99\test folder\txt
#https://www.dropbox.com/home/test 