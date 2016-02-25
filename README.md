# Checkpoint_Firewall_Tools

These are python tools to ease some of the administrative tasks for Checkpoint Firewalls running the Gaia OS.  Each script was designed for ease of use, and will ask you for information before executing.  One thing to have ready is a list of firewall IP addresses in a plain text/ascii file to use as input.

You will need to ensure you have Paramiko installed. (pip install paramiko, or apt-get install python paramiko, or zypper in python-paramiko, or any other method)

ssh_fw_password_change.py - Changing passwords can be a pain, especially in a larger environment.  This script will prompt you through the necessary information, then go out and change the password for the account indicated on all firewalls in the list.  A fail log is created as well, for manual follow-up.

ssh_fw_useradd.py - This one adds a user account with admin privileges to all firewalls in the list.  Very useful for making pre-maintenace emergency accounts for local staff to use in emergency situations.  Once the password is disclosed and used, the ssh_fw_password_change.py script can change the password everywhere to keep the account secure and only used in appropriate situations.

ssh_multiplehosts_command.py - Runs the same command on a list of firewalls.  This is great to check what versions of the OS are out there, system load, and numerous other tasks.
