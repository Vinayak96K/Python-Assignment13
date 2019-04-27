import time
import schedule
import FileHelper
import MailSender
import sys

def RemovalTask():
    DirPath=str(sys.argv[1])
    Minitues = int(sys.argv[2])
    MailTo = str(sys.argv[3])
    rList = FileHelper.DuplicateRemover(DirPath)
    LogTime=str(time.ctime())
    LogFileName=str("Duplicates_Removed_at_%s.log"%(LogTime))
    if(FileHelper.GenreateLogFile(rList,LogFileName,LogTime)):
        print('Success: Log file generated.')
        MailSender.SendMail(LogFileName,MailTo)
    else:
        print("Failure: Unable to create logfile.\nPlease enter valid directory path and try again!")

def main():
    if(len(sys.argv)== 2):
        if(str(sys.argv[1])=='-h'):
            print("This is an automation script to find and REMOVE duplicate files from a specified directory path and send REPORT through mail at scheduled time.")
        elif(str(sys.argv[1])=='-u'):
            print("Write command as:\npython RRDuplicate.py <Directory Path> <Minutes> <Mail To> ")
        else:
            print('Improper command!\nTry specifying switches as -u or -h for usage and help.')
    elif(len(sys.argv)== 4):
        iMin=0
        MailTo=''
        DirPath=''
        try:
            DirPath=str(sys.argv[1])
            Minitues = int(sys.argv[2])
            MailTo = str(sys.argv[3])
            schedule.every(int(Minitues)).minutes.do(RemovalTask)
            while True:
                schedule.run_pending()
                time.sleep(1)
        except ValueError as veObj:
            print('Improper command!\nTry specifying switches as -u or -h for usage and help.')
            return
    else:
        print('Improper command!\nTry specifying switches as -u or -h for usage and help.')
    return   

if __name__ == "__main__":
    main()