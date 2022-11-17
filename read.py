
class Archivo:
    def read():
        file= open("2388865_METGRAM.TXT")
        file_read = file.read()
        n=file_read.find('+')
        file_read=file_read[n:]
        file_read=file_read.split()
        for i in range(9):
            file_read.remove('+')
        #print(file_read)
        #for n in range(1,27,3):
        #    print(n)
        return(file_read)