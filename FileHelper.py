import hashlib
import os

LogFileName=""

def getChecksum(FilePath):
    if(os.path.exists(FilePath)):
        hashObj=hashlib.md5()
        fd=open(FilePath,"rb")
        hashObj.update(fd.read())
        return str(hashObj.hexdigest())
    else:
        pass

def DuplicateRemover(dirFilePath):
    RemovedList = []
    if(os.path.isabs(dirFilePath)==False):
        dirFilePath=os.path.getabs(dirFilePath)
    if(os.path.isdir(dirFilePath)):
        try:
            for foldername,subfolder,filename in os.walk(dirFilePath):
                dVar=dict()
                for file in filename:
                    strCheckSum=getChecksum(os.path.join(foldername,file))
                    if((dVar.get(strCheckSum)!=None)):
                        os.remove(os.path.join(foldername,file))
                        RemovedList.append(str("Removed: "+foldername+'/'+file+'\n'))
                    else:
                        dVar.update({strCheckSum :str(dirFilePath+'/'+file) })
        except OSError as eObj:
            pass
    return RemovedList

def GenreateLogFile(RList,LogFilePath,LogFileTime):
    try:
        strHeader = "-" * 80
        strHeader += "\n\t\t\t\tLog generated at %s\n"%(LogFileTime)
        strHeader += "-" * 80
        fd=open(LogFilePath,'a+')
        fd.write(str(strHeader+'\n'))
        for line in RList:
            fd.write(str(line))
        fd.close
        return True
    except Exception as eObj:
        print(eObj)
        return False