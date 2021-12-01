import shutil, os, string
from pathlib import Path

SOURCE = "E:\TEMP_LOCAL\Survey Calculations"
DESTINATION = "Z:\BACKUP\TESTE_BCK\\"

shutil.copytree(SOURCE, DESTINATION)