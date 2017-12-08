'''
Created on 28 Oct. 2017 @author: nikhil
>Purpose: To install Zabbix on Agent and PaperCut Custom script on Windows
>Steps: Install latest python 3.x; create folder "c:\zabbix"; place "zabbix-papercut-linux-py3.zip" and "zabbix-3.4.3.tar.gz" in there.
Run this script
'''
import os
import shutil
import socket
from subprocess import check_output
import zipfile
import glob
import tarfile
import sys
import re

os.chdir('c:\\zabbix')
#create binz file all file in operations are placed here.
if not os.path.exists('binz'):
    os.makedirs('binz')

# Unzip zabbix folder for all python scrips and papercut.conf
def PcZipCopy():
    zip_ref = zipfile.ZipFile('zabbix-papercut-master.zip', 'r')
    zip_ref.extractall('tmpz')
    zip_ref.close()            
    for file in glob.glob(r'tmpz\zabbix-papercut-master\linux\py3\*.py'):
        shutil.copy(file,'binz')
    shutil.copy('tmpz\zabbix-papercut-master\papercut.conf','binz')    

# Untar zabbix conf file for windows and agentd.exe and place in binz file 
def Ztarcopy(): 
    tar = tarfile.open("zabbix-3.4.3.tar.gz", 'r:gz')
#    print (tar.getmembers())
    tar.extract('zabbix-3.4.3/conf/zabbix_agentd.win.conf', 'tmpz')
    tar.extract('zabbix-3.4.3/bin/win64/zabbix_agentd.exe', 'tmpz')
    tar.close()
    shutil.copy('tmpz\\zabbix-3.4.3\\conf\\zabbix_agentd.win.conf','binz\\zabbix_agentd.conf')
    shutil.copy('tmpz\\zabbix-3.4.3\\bin\\win64\\zabbix_agentd.exe','binz\\zabbix_agentd.exe')
    
# Edit all file to make them compatible for windows
def Zedit():    
    os.chdir(r'c:\\zabbix\\binz\\')
    filelist = ['discovery-device.py', 'discovery-devicestatus.py','discovery-printer.py','discovery-printerstatus.py','papercut.py']
    for file in filelist:
        lines = []
        with open(file, 'r') as infile:
            for line in infile:
                line = line.replace('/etc/zabbix/', r'c:\\zabbix\\binz\\')
                lines.append(line)
        infile.close()
        with open(file, 'w') as outfile:
            for line in lines:
                outfile.write(line)
        outfile.close
# Edit /binz/papercut.conf file
    p = '(?:http.*://)?(?P<host>[^:/ ]+).*=(?P<auth>.*)'
    hmu = input('Enter PaperCut System Health Monitoring URL: ').strip()
    m = re.search(p,hmu)
    pcip = m.group('host') # 'www.abc.com'
    pcAuth = m.group('auth') # '123'
    print (pcip)
    print (pcAuth)
#    pcip = input('Enter PaperCut server IP address [127.0.0.1] : ').strip()
    if not pcip:
        pcip = '127.0.0.1'     
#    pcAuth = input('Enter Authorization code : ').strip()
    if not pcAuth:
        pcAuth = 'oFxc5nFBKBAkqb8MAg98HFGZlovFVpXG' 
    replacements = {'10.5.1.92': pcip, 'oFxc5nFBKBAkqb8MAg98HFGZlovFVpXG': pcAuth}
    lines = []
    with open('papercut.conf', 'r') as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            lines.append(line)
    infile.close()
    with open('papercut.conf', 'w') as outfile:
        for line in lines:
            outfile.write(line)
    outfile.close
#Edit binz/zabbix_agent.d.conf file
    zxip = input('Enter Zabbix Server IP address [127.0.0.1] : ').strip()
    if not zxip:
        zxip = '127.0.0.1'
        szxip = 'Server='+ zxip     
    else:
        szxip = 'Server='+ zxip        
    zxaip = input('Enter Zabbix active Server IP address [] : ').strip()
    if not zxaip:
        szxaip = 'ServerActive='+ zxip     
    else:
        szxaip = 'ServerActive='+ zxaip        
    myhost = socket.gethostname()    
    replacements = {'LogFile=c:\zabbix_agentd.log': 'LogFile=c:\\zabbix\\binz\\zabbix_agentd.log','Server=127.0.0.1': szxip, 'ServerActive=127.0.0.1': szxaip, 'Windows host': myhost}
    lines = []
    with open('zabbix_agentd.conf', 'r') as infile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            lines.append(line)
    infile.close()
    with open('zabbix_agentd.conf', 'w') as outfile:
        for line in lines:
            outfile.write(line)   
    outfile.close
    PythonPath=sys.executable
    f = open('zabbix_agentd.conf', 'a')        
    f.write('\nUnsafeUserParameters=1')
    f.write('\nUserParameter=papercut[*],'+PythonPath+r' C:\\\zabbix\\\binz\\\papercut.py "$1"')
    f.write('\nUserParameter=device.discovery,'+PythonPath+r' C:\\\zabbix\\\binz\\\discovery-device.py')
    f.write('\nUserParameter=device.status[*],'+PythonPath+r' C:\\\zabbix\\\binz\\\discovery-devicestatus.py "$1"')
    f.write('\nUserParameter=printer.discovery,'+PythonPath+r' C:\\\zabbix\\\binz\\\discovery-printer.py')
    f.write('\nUserParameter=printer.status[*],'+PythonPath+r' C:\\\zabbix\\\binz\\\discovery-printerstatus.py "$1"')
    f.close            

def Zbat():
    f = open('zagent-install-start.bat', 'w')
    f.write('@echo off')
    f.write('\nC:\\zabbix\\binz\\zabbix_agentd.exe -c C:\\zabbix\\binz\\zabbix_agentd.conf --install')
    f.write('\nC:\\zabbix\\binz\\zabbix_agentd.exe --start')
    f.write ('\npause')
    f.close()    
    f = open('zagent-stop-uninstall.bat', 'w')
    f.write('@echo off')
    f.write('\nC:\\zabbix\\binz\\zabbix_agentd.exe --stop')
    f.write('\nC:\\zabbix\\binz\\zabbix_agentd.exe --uninstall')
    f.write('\npause')
    f.close()              

def Zstart():
    check_output("C:\\zabbix\\binz\\zabbix_agentd.exe -c C:\\zabbix\\binz\\zabbix_agentd.conf --install", shell=True)
    check_output("C:\\zabbix\\binz\\zabbix_agentd.exe --start", shell=True)

def main():
    PcZipCopy()
    Ztarcopy()
    Zedit()
    Zbat()
    Zstart()

if __name__ == "__main__":
    main()
    