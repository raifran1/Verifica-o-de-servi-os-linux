# -*- coding: utf-8 -*-
import os, subprocess, datetime, getpass

# services to verify
services = ["apache2", 'mysql', 'postgresql']

def is_running_service(services):

	# using getpass to write password root user in terminal
	# password = getpass.getpass("Digite a senha do root: ")

	# Insert password static to automatic restarted
	password = "password__123"

	# create folder and archives the logs
	try:
		f = open("logs/{}.txt".format(datetime.datetime.now().strftime("%d-%m-%Y, %H:%M")), "w+")
	except:
		os.mkdir('{}'.format('logs'))
		f = open("logs/{}.txt".format(datetime.datetime.now().strftime("%d-%m-%Y, %H:%M")), "w+")

	# verify all services the list
	for service in services:
		p = subprocess.Popen(["sudo", "-S", "systemctl",  "is-active", service], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

		(output, err) = p.communicate(password.encode())
		output = output.decode('utf-8')

		# verify the service is active
		if 'inactive' in output:

			# restarting to service if the status is inactive
			p = subprocess.Popen(["sudo", "-S", "systemctl", "restart", service], stdout=subprocess.PIPE,
								 stdin=subprocess.PIPE)
			(output, err) = p.communicate(password.encode())
			output = output.decode('utf-8')

			if '' in output:
				check_restart = 'Restarted'
			else:
				check_restart = 'Not Restarted'

			# subscribe to log archive
			f.write('{} service is not running - Tested on {}. Restarting now.... {}\n'.format(str.upper(service), datetime.datetime.now().strftime("%d/%m/%Y, %H:%M"), check_restart))
		else:
			# subscribe to log archive
			f.write('{} service is running - Tested on {}.\n'.format(str.upper(service), datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")))

	# closed archive log
	f.close()

# call the function
is_running_service(services)
