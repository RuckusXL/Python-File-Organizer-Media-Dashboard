#Simulated Plex Dashboard
#This code simulates a Plex Media Server dashboard by generating random values for server status, active connections, users connected, and CPU usage. It also provides a menu for the user to interact with the dashboard.
#This code is for educational purposes only and does not interact with an actual Plex Media Server.
#This code is not intended for production use and should be used as a learning tool for understanding basic programming concepts such as functions, conditionals, and user input.
#Author: RuckusXL

from datetime import date
from http import server
import random

#Simulates the status of the server.
def plex_status(status):
	if status > 0:
		print("Status: Online")
	else:
		print("Status: Offline")

#Simulates the number of active connections to the server.
def plex_connect(connections):
	if connections > 0:
		print(f"Active Connections: {connections}")
	else:
		print("No Active Connections")

#Simulates the number of users connected to the server.
def plex_users(users):
	if users > 0:
		print(f"Users Connected: {users}")
	else:
		print("Idle")

#Simulates the CPU usage of the server shown as a percentage.
def cpu_usage(cpu):
	if cpu > 0:
		print(f"CPU Usuage: {cpu}%")
	else:
		print("Sleeping")

#Simulates links to server web UI.
def website_links():
    links = [
        "\n---https://app.plex.tv/desktop/#!/dashboard---",
		"---https://www.plex.tv/---",
    ]

    for link in links:
        
        print(link)

#Simulates a CLI menu for the user to interact with the dashboard and view different aspects of the server status.
def menu():
	global server, connections, users, cpu, status
	while True:
		print("\n1. Refresh Dashboard")
		print("2. Show CPU Only")
		print("3. Show Connections Only")
		print("4. Show Users Only")
		print("5. Show Status Only")
		print("6. Show Website Links")
		print("7. Restart Server")
		print("8. Shutdown Server")
		print("9. Exit")

		try:
			choice = int(input("Choose an option: "))
		except ValueError:
			print("\nPlease select a number from 1 to 9.")
			continue

		if choice == 1:
			server, connections, users, cpu, status = dashboard()
		elif choice == 2:
			cpu_usage(cpu)
		elif choice == 3:
			plex_connect(connections)
		elif choice == 4:
			plex_users(users)
		elif choice == 5:
			plex_status(status)
		elif choice == 6:
			website_links()
		elif choice == 7:
			print(f"\nRestarting {server} Server... Please wait...")
			dashboard()
		elif choice == 8:
			print(f"\nShutting down {server} Server... Goodbye!")
			break
		elif choice == 9:
			print(f"\nExiting Dashboard... Goodbye!")
			break
		else:
			print("Invalid selection. Please choose a number from 1 to 9.")

#Simulates metrics for Media Server to monitor usage and performance.
def dashboard():
	print("\n-------MEDIA SERVER-------")

	now = date.today()

	print("\nDate:", now.strftime("%m-%d-%Y"))
	print("Time:", now.strftime("%H:%M:%S"))

	server = "Plex"
	connections = random.randrange(0,10000)
	users = random.randrange(0,100)
	cpu = random.randrange(0,100)
	status = random.randrange(0,2)

	plex_status(status)
	print("Server:", server)
	plex_connect(connections)
	plex_users(users)
	cpu_usage(cpu)

	print("\n--------------------------")
	return server, connections, users, cpu, status

website_links()
dashboard()
menu()