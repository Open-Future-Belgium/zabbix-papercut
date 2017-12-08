# zabbix-papercut
Papercut Script For Zabbix 3.2

Info
-----

This code will make it able for Zabbix 3.2 and higher to monitor the Papercut server

It will also discover and return the status of all the Printers and Multifunctionals.

Tested on Papercut  NG 16.3.37858 and on both NG / MF 17.1.2 on Centos 7.2 with python 2.x but should work OS Independent.


How To
-------

1. PaperCut Server confuration on Zabbix server is common for inspite of OS on which PaperServer is installed. Please refer Steps 1 to 6 from "Monitoring PaperCut NG system health using Zabbix.docx" for detail steps of . 

2. On PaperCut Server please check python versions with command : python --version. In case if python is not installed , please installPython 2 or 3..

3. Please refer step 7 from "Monitoring PaperCut NG system health using Zabbix.docx" for Zabbix Agent installations steps base don PaperCut Server OS type.  

		
License
-------

GPLv3


Author Information
------------------

* Patrik Uytterhoeven
* patrik( at )open-future.be
* [www.open-future.be](http://www.open-future.be)
* Feel Free to Improve the code and send me pull requests
