# How to make a copy/backup for my files
import shutil
import os
import datetime

def create_backup(source_path,destinaton_path):
    backup_date = datetime.date.today()
    backup_name = os.path.join(destination_path,f"backup_{backup_date}")
    try:
        shutil.make_archive(backup_name,'gztar',source_path)
        print("Backup completed")
    except Exception as e :
        print(e)



source_path = ""  # Source path the files to want to create a backup for 
destination_path = "" # destination path where you want to keep the backups

create_backup(source_path,destination_path)