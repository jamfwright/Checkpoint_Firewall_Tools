#!/usr/bin/env python

# By James Wright - Feb 02, 2015
# Adds a user account to Gaia OS Firewalls 

import paramiko
import sys
import getpass

match = 0
port = 22
login_fails=[]


print "\n\nBefore running this script please know that you will need:\n\n[-] A unique username\n[-] A unique UID"
print "\nPlease login to a firewall and review /etc/passwd to see what usernames and UID's already exist."
print "\n\n If you are Not Ready then press Ctrl-C or close the terminal window to cancel"

hostsFile = raw_input("\n\n[?] Enter the file containing the IP address list to use: ")
username = raw_input("\n[?] Enter the username to login with: ")
password = getpass.getpass("\n[?] Enter the password for the '" + username + "' account:") 


new_account = raw_input("\n\n[?] Now enter the new user account name: ")


while (match < 1) :
	if (match < 1) :
		new_password = getpass.getpass("\n[?] Enter the password for the new account: ")
		verify_password = getpass.getpass("\n[?] Enter the same password again: ")
		if (new_password == verify_password) :
			print "[*] Passwords Match"
			match = 1
		else :
			print "[!] Passwords do not match, try again..."
			match = 0


new_uid = raw_input("\n[?] Enter in a UID Number.  This is ideally over 1001: ")
 

command0 = "lock database override"
command1 = "add user " + new_account + " uid " + new_uid + " homedir /home/" + new_account
command2 = "set user " + new_account + " password"
command3 = "add rba user " + new_account + " roles adminRole"
command4 = "save config"

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
	print "[*] Adding user " + new_account + "..."
        stdin, stdout, stderr = s.exec_command(command1)
        print stdout.read()
	print "[*] Setting password..."
        stdin, stdout, stderr = s.exec_command(command2)
	stdin.write(new_password + "\n")
	stdin.write(verify_password + "\n")
        print stdout.read()
	print "[*] Setting user " + new_account + " roles to adminRole..."
	stdin, stdout, stderr = s.exec_command(command3)
	print stdout.read()
	print "[*] Saving Configuration...."
	stdin, stdout, stderr = s.exec_command(command4)
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

