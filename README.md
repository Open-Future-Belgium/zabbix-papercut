# zabbix-papercut
Papercut Script For Zabbix 3.2

Info
-----
This code will make it able for Zabbix 3.2 and higher to monitor the Papercut server
It will also discover and return the status of all the Printers and Multifunctionals.


How To
-------

For Linux:

* (Tested on Papercut  NG 16.3.37858 and on both NG / MF 17.1.2 on Centos 7.2 with python 2.x but should work OS Independent.
* Install the Zabbix agent on the papercut server
* Make sure the Zabbix agent works in Active / Passive Mode
* Make sure SeLinux is disabled DURING the installation if your OS makes use of SeLinux. When everything works enable again and configure if needed. (check with getenforce, the output should be disabled or permissive during the installation)
* Create 2 Macros on the Papercut host in Zabbix (Configuration –- Hosts –- papercut-server –- Macros)
* From the folder “template” import the template in Zabbix (Configuration – Zabbix –- Templates – Import)
* Copy all the the files from the linux folder + papercut.conf to the folder /etc/zabbix
* Edit the papercut.conf file and add the correct Authorization token and papercut server ip.
* In the Zabbix-Agent configuration enable support for Unsupported parameters (we need this as there are “/” in the printer names)
* Restart the Zabbix-Agent so that it picks up the new configuration files.
* Check the latest data page to see if it works


For Windows:
* Python2 and Python3 scripts are provided in the Windows folder
* Follow the documentation provided for Windows


License
-------

GPLv3


Author Information
------------------

* Patrik Uytterhoeven
* patrik( at )open-future.be
* [www.open-future.be](http://www.open-future.be)
* Feel Free to Improve the code and send me pull requests
