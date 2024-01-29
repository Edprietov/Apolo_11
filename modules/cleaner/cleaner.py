import shutil
import os

REPORTS_PATH: str = "./reports"
BACKUP_PATH: str = "./backup"
DEVICES_PATH: str = "./devices"

class Cleaner:
    
    def do_initial_cleanup():
        if not os.path.isdir(REPORTS_PATH):
            os.mkdir(REPORTS_PATH)
        if not os.path.isdir(BACKUP_PATH):
            os.mkdir(BACKUP_PATH)
        else:
            shutil.rmtree(BACKUP_PATH)
            os.mkdir(BACKUP_PATH)
        if not os.path.isdir(DEVICES_PATH):
            os.mkdir(DEVICES_PATH)
        else:
            file_names = os.listdir(DEVICES_PATH)
        for f in file_names:
            os.remove(os.path.join(DEVICES_PATH, f))
    
    def do_cleanup(simulation_number):
        os.mkdir(f"./backup/Simulation_{simulation_number}")

        file_names = os.listdir(DEVICES_PATH)
        
        for file_name in file_names:
            shutil.move(os.path.join(DEVICES_PATH, file_name), f"./backup/Simulation_{simulation_number}")