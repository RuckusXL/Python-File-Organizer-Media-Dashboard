#Simulated Plex Dashboard
#This code simulates a Plex Media Server dashboard by generating random values for server status, active connections, users connected, and CPU usage. It also provides a menu for the user to interact with the dashboard.
#This code is for educational purposes only and does not interact with an actual Plex Media Server.
#This code is not intended for production use and should be used as a learning tool for understanding basic programming concepts such as functions, conditionals, and user input.
#Author: RuckusXL

from datetime import date
import random

server = "Plex"
connections = random.randrange(0,10000)
users = random.randrange(0,100)
cpu = random.randrange(0,100)
status = random.randrange(0,2)

def plex_status(status):
	if status > 0:
		print("Status: Online")
	else:
		print("Status: Offline")

def plex_connect(connections):
	if connections > 0:
		print(f"Active Connections: {connections}")
	else:
		print("No Active Connections")

def plex_users(users):
	if users > 0:
		print(f"Users Connected: {users}")
	else:
		print("Idle")

def cpu_usage(cpu):
	if cpu > 0:
		print(f"CPU Usuage: {cpu}%")
	else:
		print("Sleeping")

def website_links():
    links = [
        "\n---https://app.plex.tv/desktop/#!/dashboard---",
		"---https://www.plex.tv/---",
    ]

    for link in links:
        
        print(link)

def menu():
    print("\n1. Refresh Dashboard")
    print("2. Show CPU Only")
    print("3. Show Connections Only")
    print("4. Show Users Only")
    print("5. Show Status Only")
    print("6. Show Website Links")
    print("7. Restart Server")
    print("8. Shutdown Server")
    print("9. Exit")

    return int(input("Choose an option: "))

print("\n-------MEDIA SERVER-------")

now = date.today()

print("\nDate:", now.strftime("%m-%d-%Y"))
print("Time:", now.strftime("%H:%M:%S"))

plex_status(status)
print("Server:", server)
plex_connect(connections)
plex_users(users)
cpu_usage(cpu)
print("\n--------------------------")

website_links()

menu()