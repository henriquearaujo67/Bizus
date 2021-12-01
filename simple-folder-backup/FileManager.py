#@module: FileManager.py
#@description: Script to take backup to a fixed location
#@author: Henrique Araujo
#@date: 2021, November 01


# import required libraries
import os, time
import shutil
import sys
import time
from datetime import datetime
import string


# Global variables
# setup backup locations

# folders to backup
locations = [r'E:\OneDrive\Scripts',
    r'K:\My Documents\OEC_Scripts',
    r'E:\GoogleDrive\Projetos\MarketingDigital', 
    r'E:\OneDrive\PROJETOS'
    ]

"""
CONFIG = {[
    {
        "folder": "E:\OneDrive\Scripts",
        "bckType": "ZIP",  # Compress folder
        "destination": "E:\TEMP_LOCAL\FM_BACKUP_TEMP"
    },
    {
        "folder": "E:\TEMP_LOCAL\FM_BACKUP_TEMP",
        "bckType": "FILE",  # Copy folder/file to destination
        "destination": "Z:\BACKUP"
    }    
]}
"""


BACKUP_DIR = r'Z:\BACKUP' # backup destination
RESTORE_DIR = r'E:\TEMP_LOCAL\RESTORE'




def syncFolders():
        
    """
    https://www.instructables.com/Syncing-Folders-With-Python/

    Syncing Folders With Python by chrisbeardy

    https://pypi.python.org/pypi/dirsync/2.2.2

    """

    # Rodar isso na linha de comando do conda para instalar essas duas bibliotecas
    # pip install pyinstaller
    # pip install dirsync

    from dirsync import sync

    SourceFolder = r'E:\WINFILES'
    DestinationFolder = r'Z:\BACKUP\WINFILES'

    sync(SourceFolder, DestinationFolder, 'sync', create=True, purge=True)


def backup1():
    today = target_dir + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')

    comment = input('Enter a comment --> ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + \
            comment.replace(' ', '_') + '.zip'

    if not os.path.exists(today):
        os.mkdir(today) # make directory
        print('Successfully created directory', today)

    zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
    #se preferirem tar tirem o comment da proxima linha
    #tar = 'tar -cvzf %s %s -X /home/triton/excludes.txt' % (target, ' '.join(srcdir))

    if os.system(zip_command) == 0:
        print ('Successful backup to', target)
    else:
        print ('Backup FAILED')


def backup2():
   # 1. The files and directories to be backed up are specified in a list.
   source = [r'C\Users\MySourceDir']

   # 2. The backup must be stored in a # main backup directory
   target_dir = r'C:\Users\MyTargetDir'

   # 3. The files are backed up into a zip file.
   # 4. The name of the zip archive is the current date and time
   target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.7z'

   # Create target directory if it is not present
   if not os.path.exists(target_dir):
       os.mkdir(target_dir)

   # 5. We use the zip command to put the files in a zip archive
   zip_command = 'C:\\"Program Files"\\7-Zip\\7z a -t7z -r "{0}" "{1}"'.format(target,' '.join(source)) # be careful with spaces on each dir specification. Problems could arise if double-quotation marks aren't between them. 

   # Run the backup 
   print('Zip command is:') 
   print(zip_command)
   print('Running:')

   if os.system(zip_command) == 0: 
       print('Successful backup to', target)
   else: 
       print('Backup FAILED')


def backupMIT():
    #!/usr/bin/env python
    #@module: backup.py
    #@description: Script to take backup to a fixed location
    #@author: Prahlad Yeri
    #@copyright: MIT Licensed

    #from __future__ import print_function
    import os
    import os.path
    import sys
    import time
    from datetime import datetime
    import shutil

    backup_loc = '/media/username/1tera/backup'
    #backup_loc = '/tmp/backup'

    locations = ['/home/username/docs',
        '/home/username/source',
        '/home/username/scripts',
        '/home/username/library',
        '/home/username/programs',
        '/home/username/staging',
        '/home/username/soft',
        '/home/username/Desktop',
        '/home/username/Downloads',
        '/home/username/movies',
        '/home/username/songs',
        ]

    """
    if __name__ == "__main__":
        #loop thru the folders
        start = time.clock()
        num=0
        for s in locations: #[0:1]:
            #print s + "\n"
            #files = os.listdir(s)
            print 'listing for '  + s
            for (root, dirs, files) in os.walk(s):
                subpath = root.replace('/home/prahlad','')
                for f in files:
                    filename = os.path.join(root, f)
                    dfilename = backup_loc + subpath + os.sep + f
                    link = ''
                    if os.path.islink(filename):
                        link = os.readlink(filename)


                    if not os.path.exists(dfilename):
                        #check dirs
                        if not os.path.exists(backup_loc + subpath):
                            os.makedirs(backup_loc + subpath)
                            print 'creating directory: ' + backup_loc + subpath

                        #just copy the files
                        print 'copying from: ' + filename
                        print 'to: ' + dfilename
                        if link == '':
                            shutil.copy2(filename, dfilename)
                        else:
                            os.symlink(link, dfilename)
                        num+=1
                    else:
                        sz = os.path.getsize(filename); lm = datetime.fromtimestamp(os.path.getmtime(filename)).timetuple()
                        dsz = os.path.getsize(dfilename); dlm = datetime.fromtimestamp(os.path.getmtime(dfilename)).timetuple()

                        if (sz == dsz and lm == dlm):
                            print 'skipped: ' + dfilename
                            #time.sleep(3)
                        else:
                            #copy the files
                            print 'copying from: ' + filename
                            print 'to: ' + dfilename
                            if link == '':
                                shutil.copy2(filename, dfilename)
                            else:
                                os.symlink(link, dfilename)
                            num+=1

        mins = (time.clock() - start)
        #print "All files copied in %d minutes" % mins
        print "{0} files copied in {1} minutes".format(int(num), round(mins))


    """


def backupZip(source: string, destination: string):
    #shutil.make_archive('a:\\backup\\backup','zip','d:\\temp\\')
    shutil.make_archive(destination + "\\teste",'zip', source)


def restoreZip(zipFile: string, destination: string):
    #shutil.unpack_archive('d:\\temp\\backup.tar','d:\\temp\\extract\\')
    shutil.unpack_archive(zipFile,destination)    


def menuApp():
    print(30 * "-", "File Manager", 30 * "-")
    print("1. Backup folders to destination")
    print("2. Compress folders to destination")
    print("3. Sync folders")
    print("4. Exit/Quit")
    print()
    print("Run 1: Enter choice [1-4]:")    
    print(67 * "-")


def loopApp():
    loop = True
    while loop:
        os.system('cls') # on Windows
        # os.system('clear') # on Linux

        menuApp()
        choice = input()

        if choice == '1':
            print("Menu 1 selected")
        elif choice == '2':
            print("Menu 2 selected")
            folder = "E:\Pictures\Screenshots"
            destination = "E:\\TEMP_LOCAL\\FM_BACKUP_TEMP"
            backupZip(folder, destination)

        elif choice == '3':
            print("Menu 3 selected")
        elif choice == '4':
            print("Menu 4 selected. Exiting")
            loop = False
        else:
            # Any integer inputs other than values 1-4 we print an error message
            input("Wrong option selected. Enter any key to try again..")



def main():


    loopApp()

if __name__ == "__main__":
    main()