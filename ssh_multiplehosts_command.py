#!/usr/bin/env python

import paramiko
import sys
import getpass

port = 22
hostsFile = raw_input("\nEnter the file containing the IP address list to use: ")
command = raw_input("\nEnter the command to run: ")
username = raw_input("\nEnter the username to login with: ")
password = getpass.getpass("\nEnter the password for the '" + username + "' account:") 
fail_list = []

with open(hostsFile, 'r') as f:
  for hostname in f:
    hostname = hostname.strip()
    print("\nCurrently trying: " + hostname)
    try:
    
      if __name__ == "__main__":
        paramiko.util.log_to_file('ssh_connections.log')
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname, port, username, password)
        stdin, stdout, stderr = s.exec_command(command)
        print stdout.read()
        s.close()
    except:
	print ("Connection or Authentication error\n")
        fail_list.append(hostname)
	continue	

    if not hostname:
      continue

print "\nCould not connect to these hosts.  \nPlease verify the host name or IP address, and/or try manually:\n"
for each in fail_list:
	print each
