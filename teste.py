import subprocess
import os
import time
a = time.sleep(0.5)
desired_directory = "C:\\Users"
command_to_run = "tree /f" 
os.chdir(desired_directory)
subprocess.Popen(f'start /max cmd /K{command_to_run}', shell=True)