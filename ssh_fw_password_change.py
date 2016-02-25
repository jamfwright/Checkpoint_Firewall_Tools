#!/usr/bin/env python

# By James Wright - April 13, 2015
# Changes account password on Gaia OS

import paramiko
import sys
import getpass

match = 0
port = 22
login_fails=[]



hostsFile = raw_input("\n\n[?] Enter the file containing the IP address list to use: ")
username = raw_input("\n[?] Enter the username to login with: ")
password = getpass.getpass("\n[?] Enter the password for the '" + username + "' account:") 


new_account= raw_input("\n\n[?] Now enter the account you are changing the password for.\nThis can be the same account as you log in with: ")


while (match < 1) :
	if (match < 1) :
		new_password = getpass.getpass("\n[?] Enter the new password for " + new_account + ": ")
		verify_password = getpass.getpass("\n[?] Enter the same password again: ")
		if (new_password == verify_password) :
			print "[*] Passwords Match"
			match = 1
		else :
			print "[!] Passwords do not match, try again..."
			match = 0


 

command0 = "lock database override"
command1 = "set user " + new_account + " password"


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
	print "[*] Getting configuration lock..."
	stdin, stdout, stderr = s.exec_command(command0)
	print "[*] Changing password for " + new_account + "..."
        stdin, stdout, stderr = s.exec_command(command1)
	stdin.write(new_password + "\n")
	stdin.write(verify_password + "\n")
        print stdout.read()
	print "[*] Process for " + hostname + " complete"
        s.close()
    except:
	print ("Connection or Authentication error\n")
	login_fails.append(hostname)
        continue	

    if not hostname:
      continue

if fail_list:
	print "\nCould not connect to these hosts.  \nPlease verify the host name or IP address, and/or try manually:\n"
	for each in fail_list:
        	print each

