import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to,local_path):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dir, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
        access_token = 'sl.AylfwQCc9hUQQb1Yn-_LC6AymswddWrWcJJ3VJOgERovHWPmn7lfwgPHnMmLcHTNTawKkBlqGUzMtTQF2aNne0m7u8JkUpClDaS0pwZfZo6pDWpsGWr5ebQ-VP3JR1oZ6SBA-BQ'
        transferData = TransferData(access_token)
        file_from = input("Enter the file path to upload: ")
        #enter the full path to upload the file including the file name that we want once uploaded
        file_to = input("Enter the full path to uploaded in dropbox: ")

        transferData.upload_file(file_from,file_to)
        print("file has been uploaded!")
if __name__ == '__main__':
    main()



