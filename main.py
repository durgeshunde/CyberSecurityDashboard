# CyberSecurityDashboard - fancy version
import re
import psutil
import subprocess
from prettytable import PrettyTable
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ------------------------------
# Password Strength Checker
# ------------------------------
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search(r"[A-Z]", password):
        return "Weak: Add an uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Add a lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Add a number"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Add a special character"
    return "Strong"

# ------------------------------
# Network Connections Table
# ------------------------------
def list_network_connections():
    print(Fore.CYAN + "\n--- Network Connections ---")
    connections = psutil.net_connections()
    table = PrettyTable()
    table.field_names = ["Local Address", "Remote Address", "Status"]

    for conn in connections:
        local = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        table.add_row([local, remote, conn.status])
    
    print(table)

# ------------------------------
# Python Package Update Reminder
# ------------------------------
def check_outdated_packages():
    print(Fore.MAGENTA + "\n--- Outdated Python Packages ---")
    try:
        result = subprocess.run(["pip", "list", "--outdated"], capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        else:
            print("All packages are up-to-date!")
    except Exception as e:
        print(f"Error checking packages: {e}")

# ------------------------------
# Dashboard Menu
# ------------------------------
def dashboard():
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "   Personal Cyber Security Dashboard ")
    print(Fore.GREEN + "=====================================")

    while True:
        print(Fore.YELLOW + "\nSelect an option:")
        print("1. Check Password Strength")
        print("2. List Network Connections")
        print("3. Check Outdated Python Packages")
        print("4. Exit")

        choice = input(Fore.CYAN + "\nEnter choice (1-4): ")

        if choice == "1":
            password = input("\nEnter a password to check: ")
            strength = check_password_strength(password)
            print(Fore.RED + "Password Strength:", strength)
        elif choice == "2":
            list_network_connections()
        elif choice == "3":
            check_outdated_packages()
        elif choice == "4":
            print(Fore.GREEN + "\nThank you for using your Personal Cyber Security Dashboard!")
            break
        else:
            print(Fore.RED + "Invalid choice. Try again.")

# ------------------------------
# Run the dashboard
# ------------------------------
if __name__ == "__main__":
    dashboard()