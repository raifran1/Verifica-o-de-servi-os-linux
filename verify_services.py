# -*- coding: utf-8 -*-
import os, subprocess, datetime, getpass

services = ["apache2", 'mysql', 'postgresql']

def is_running_service(services):
	# password = getpass.getpass("Please enter your password: ")
	try:
		f = open("logs/{}.txt".format(datetime.datetime.now().strftime("%d-%m-%Y, %H:%M")), "w+")
	except:
		os.mkdir('{}'.format('logs'))
		f = open("logs/{}.txt".format(datetime.datetime.now().strftime("%d-%m-%Y, %H:%M")), "w+")

	for service in services:
		p = subprocess.Popen(["systemctl",  "is-active", service], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

		(output, err) = p.communicate(input='password')
		output = output.decode('utf-8')

		if 'inactive' in output:
			os.system('systemctl start {}'.format(service))
			f.write('{} service is not running - Tested on {}. Restarting now.... \n'.format(str.upper(service), datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")))
		else:
			f.write('{} service is running - Tested on {}.\n'.format(str.upper(service), datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")))

	f.close()

is_running_service(services)
