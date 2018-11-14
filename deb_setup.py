#!/usr/bin/env python3.5
# _*_ coding: utf-8 _*_

"""
debian_setup.py 1.0.0 by cb0n3y ()
Licence: BSD.

Description: This script speedup the basic setup of debian either desktop
             or server. The script is writen in python3.5, so you should
             make sure your dependencies are up to date.

Usage: python3 debian_setup.py

Advice: Please check first  the name of your network interface and after
        that make the required changes on the interfaces and hosts file
        before you run the script for the first time.
        On the interfaces file, change the interface name with the name
        of your own network interface and give all the other information
        such as IP Address, Network and so on,  according to your Network.
"""

__author__ = 'cb0n3y'
__version__ = '1.0.0'
__copyright__ = 'Copyright (c) 2018-2019 cb0n3y'


import os
from subprocess import call
from time import sleep


cp = 'cp'
apt = 'apt'
prompt = '> '
right = 'sudo'
srv = 'Server'
apt_opt = '-y'
go_on = 'ENTER'
editor = 'nano'
desk = 'Desktop'
do_not = 'CTRL-C'
update = 'update'
upgrade = 'upgrade'
install = 'install'
autoremove = 'autoremove'
hosts_path = '/etc/hosts'
hostname_path = '/etc/hostname'
ssh_path = '/etc/ssh/sshd_config'
network_files = ['interfaces', 'hosts']
sources_list_path = '/etc/apt/sources.list'
interfaces_path = '/etc/network/interfaces'
paths = ['/etc/hosts', '/etc/hostname', '/etc/apt/sources.list', '/etc/network/interfaces', '/etc/ssh/sshd_config']
programs_desk = ['htop', 'curl', 'wget', 'perl', 'tree', 'unace', 'p7zip-full', 'p7zip-rar', 'lzip', 'arj', 'sharutils',
                 'mpack', 'lzma', 'lzop', 'unzip', 'zip', 'bzip2', 'lhasa', 'cabextract', 'lrzip', 'rzip', 'zpaq',
                 'kgb', 'xz-utils', 'dnsutils', 'net-tools', 'chkrootkit', 'ufw', 'dpkg', 'wget', 'python-pip',
                 'python-virtualenv', 'openssh-server', 'openssh-client', 'firmware-linux-free', 'nmap', 'macchanger',
                 'john', 'wireshark', 'tcpdump', 'kismet']
programs_srv = ['lm-sensors', 'hddtemp', 'htop', 'curl', 'wget', 'perl', 'tree', 'unace', 'p7zip-full', 'p7zip-rar',
                'lzip', 'arj', 'sharutils', 'mpack', 'lzma', 'lzop', 'unzip', 'zip', 'bzip2', 'lhasa', 'cabextract',
                'lrzip', 'rzip', 'zpaq', 'kgb', 'xz-utils', 'dnsutils', 'net-tools', 'chkrootkit', 'ufw', 'dpkg',
                'wget', 'python-pip', 'python-virtualenv', 'openssh-server', 'openssh-client']


def main_menu():

    while True:
        print("===> Select one of the options bellow... <===\n")
        print("[1] {0}.\n[2] {1}.\n".format(desk, srv))
        menu_choice = input(prompt)

        if menu_choice == str(1):
            desk_menu()
        elif menu_choice == str(2):
            srv_menu()
        else:
            print("===> Try Agin. <===\n")
            main_menu()


def desk_menu():

    while True:
        print("Select one of the options bellow:\n")
        print("[1] Update & Upgrade your system.")
        print("[2] Install a few programs.")
        print("[3] Make a backup of some config-data.")
        print("[4] Change Hostname.")
        print("[5] Set the IP-Address to static.")
        print("[6] Go back to main menu.\n")
        print("\n[i] To exit this menu hit {0}.\n".format(do_not))
        user_choice = int(input(prompt))

        if user_choice == 1:
            sys_update()
            sys_upgrade()
            sys_clean()
            desk_menu()
        elif user_choice == 2:
            install_soft1()
            desk_menu()
        elif user_choice == 3:
            config_backup()
            desk_menu()
        elif user_choice == 4:
            change_hostname()
            desk_menu()
        elif user_choice == 5:
            static_ip()
            # sys_restart()
        elif user_choice == 6:
            main_menu()
        else:
            print("[i] Sorry but I got nothing.\n===> Please try again! <===\n")
            sleep(1)
            desk_menu()


def srv_menu():
    while True:
        print("Select one of the options bellow:\n")
        print("[1] Update & Upgrade your system.")
        print("[2] Install a few programs.")
        print("[3] Make a backup of some config-data.")
        print("[4] Change Hostname.")
        print("[5] Set the IP-Address to static.")
        print("[6] Go back to main menu.\n")
        print("\n[i] To exit this menu hit {0}.\n".format(do_not))
        user_choice = int(input(prompt))

        if user_choice == 1:
            sys_update()
            sys_upgrade()
            sys_clean()
            srv_menu()
        elif user_choice == 2:
            install_soft2()
            srv_menu()
        elif user_choice == 3:
            config_backup()
            srv_menu()
        elif user_choice == 4:
            change_hostname()
            srv_menu()
        elif user_choice == 5:
            static_ip()
            srv_menu()
        elif user_choice == 6:
            main_menu()
        else:
            print("[i] Sorry but I got nothing.\n===> Please try again! <===\n")
            sleep(1)


def sys_update():
    print("[+] Your system is being updated. Please wait...\n")
    call([right, apt, update])
    print("\n[i] Done.")
    print("============================================================================\n")
    sleep(1)


def sys_upgrade():
    print("[+] Applying changes to your system. Please wait...\n")
    call([right, apt, apt_opt, upgrade])
    print("\n[i] Done.")
    print("============================================================================\n")
    sleep(1)


def sys_clean():
    print("[+] Cleaning your system...\n")
    call([right, apt, apt_opt, autoremove])
    print("\n[i] Done.")
    print("============================================================================\n")
    sleep(1)


def config_backup():
    print("[i] The following configuration data will be saved:\n")
    print("[+] {0}\n[+] {1}\n[+] {2}\n[+] {3}\n[+] {4}".format(hosts_path, hostname_path,
                                                               interfaces_path, sources_list_path, ssh_path))
    print("\n[*] For security reasons, the copies only will get read (r) rights.\n")
    sleep(5)

    for path in paths:
        if os.path.exists(path):
            print("[+] Making a copy of {0} to {1}".format(path, path + ".bak"))
            call([right, cp, path, path + ".bak"])
            print("[+] Changing the rights to read-only...")
            os.chmod(path + ".bak", 0o444)
            print("\n[i] Done")
            print("==========================================================\n")
        else:
            print("[-] The path {} does not exist.\n".format(path))
    sleep(1)


def install_soft1():
    print("[+] Installing required software...\n")

    for prog in programs_desk:
        call([right, apt, apt_opt, install, prog])
    print("\n[i] Done.")
    print("============================================================================\n")
    sleep(1)


def install_soft2():
    print("[+] nstalling required software...\n")
    for prog in programs_srv:
        call([right, apt, apt_opt, install, prog])
    print("\n[i] Done.")
    print("============================================================================\n")
    sleep(1)


def change_hostname():
    hostname = input("\n==> Please enter the hostname you want to set:\n> ")

    if os.path.exists(hostname_path):
        print("\n[+] Changing the hostname to '{}'...\n".format(hostname))
        f = open(hostname_path, 'w')
        f.write(hostname)
        f.close()
        print("\n[i] Done.")
        print("============================================================================\n")
        sleep(1)
    else:
        print("[-] The path {} does not exists or you wrote it wrong.".format(hostname_path))


def static_ip():
    # Checking if the file interfaces exists
    if os.path.isfile(network_files[0]):
        print("[+] Applying changes...")
        # Writing from interfaces to /etc/network/interfaces
        print("[+] Writing from {} to {}...\n".format(network_files[0], interfaces_path))
        interfaces_data = open(network_files[0])
        indata = interfaces_data.read()
        target1 = open(interfaces_path, 'w')
        target1.truncate()
        target1.write(indata)
        target1.close()
        interfaces_data.close()
        print("\n[i] Done.")
        print("============================================================================\n")
        sleep(1)
    else:
        print("[-] The file {} does not exist...\n".format(network_files[0]))

    if os.path.isfile(network_files[1]):
        # Writing from hosts to /etc/hosts
        print("[+] Writing from {} to {}....\n".format(network_files[1], hosts_path))
        hosts_data = open(network_files[1])
        data = hosts_data.read()
        target2 = open(hosts_path, 'w')
        target2.truncate()
        target2.write(data)
        target2.close()
        hosts_data.close()
    else:
        print("[-] The file {} does not exist...\n".format(network_files[1]))


def sys_restart():
    print("[i] Your system will be restarted...\n")
    call([right, "restart"])


if __name__ == '__main__':
    try:
        main_menu()
    except Exception as e:
        print("[-] Error ==> " + str(e))
