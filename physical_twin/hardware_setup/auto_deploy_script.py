import paramiko
import sys
import os

'''
This script was writen by Hari and Managed by Burcu for:
If you want to copy a file/dir from your computer to raspberry we can use this script as to copy the files to them:
also creates the device_name.txt file in the raspberry in /home/pi/ path to name the each device unique.

Data needed:
1. File/Dir to copy should be available in your computer (eg. Folder 'haridir')
2. Ip address, User ID and password of the raspberry
3. device_name (should be unique for among all raspberry

For adding new raspberry you can create new list as 'rasp##' as list below and its details it can automatically copy files to it
'''

# ssh_conn(): This intitiate the cmd:str line in rasberry command teminal whatever command we ginving as string
def ssh_conn(cmd:str, ip_ad, username, password):
    results=[]
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(ip_ad, username=username, password=password)
    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(cmd)
    for line in ssh_stdout:
        results.append(line.strip('\n'))
    return results

# copying_file_to_raspberry() will take source and ip as input and copy file/dir to raspberry
def copy_files(source:str, ip_ad, username, password, device_name):
    os.system('scp -r {} pi@{}:'.format(source, ip_ad)) # Command to copy to the rasberry
    ssh_conn(cmd= 'rm -Rf {}'.format(device_name), ip_ad=ip_ad, username=username, password=password) # Deleting old device.txt file if already exist
    ssh_conn(cmd= 'echo {} > /home/pi/device_id.txt'.format(device_name), ip_ad=ip_ad, username=username, password=password) # Creating new device_name.txt for device name
    return None

def run_data_collection(ip_ad, username, password):
    ssh_conn(cmd= 'python3 {}'.format(sys.argv[1]), ip_ad=ip_ad, username=username, password=password) # to kill the bg process kill $(jobs -p)
    
# Check the dir if already exist if yes deletes and copy the updated file
def create_dir(source, ip_ad, username, password, device_name):
    available_files = ssh_conn(cmd='ls', ip_ad=ip_ad, username=username, password=password) # Getting list of files/dirs
    if source in available_files: 
        ssh_conn(cmd='rm -Rf {}'.format(source), ip_ad= ip_ad, username=username, password=password) # Remove the file if exist


# List of Raspberries that the Files to be transfered with its details
# Args_Format:  <source file/path>, <ip_address>, <host_user_id>, <password>, <device_name>

rasp01 = [sys.argv[1], '140.78.42.104', 'pi', 'cdl', 'Rasp01']
# ADD MORE RASPBERRY HERE AS THE EXAMPLE SHOWN IN NEXT LINE
#rasp02 = ['haridir', '192.168.0.136', 'pi', 'cdl', 'Rasp02']

all_raspberries =[rasp01] # dont forget to mention here all rasp## here as list
for each_raspberry in all_raspberries:
    source, ip_ad, username, password , device_name= each_raspberry
    create_dir(source, ip_ad, username, password, device_name)
    copy_files(source, ip_ad, username, password, device_name)
    run_data_collection(ip_ad, username, password)
sys.exit()
