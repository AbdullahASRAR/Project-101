import dropbox


class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,files_from,files_to) : 
        dbx=dropbox.Dropbox(self.access_token)
        f=open(files_from,'rb')
        dbx.files_upload(f.read().file_to)
def main():
    accesToken="4ncoKedk2ngAAAAAAAAAAS36U6Vi7wOM8o-sUIlPur4ExB79IMHmzGetCR6mfFgG" 
    boom=TransferData(accesToken)
    files_from=input("enter the file's name to transfer :-")
    file_to=input("enter the path of the file to be uploaded :-")
    boom.uploadFiles(files_from,file_to)
    print("file has been moved")
main()        