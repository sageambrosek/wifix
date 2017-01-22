#!/usr/bin/env python
import os
response = os.system('ping 8.8.8.8 -c 1')
if response == 0:
	print 'success'
else:
	print 'restarting network manager...'
	os.system('sudo service network-manager restart')
	print "restart complete"
