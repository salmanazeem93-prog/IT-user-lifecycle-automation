import csv
from datetime import datetime

def process_users():
    print("Starting user lifecycle automation...\n")

    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row['name']
            role = row['role']
            status = row['status']

            if status.lower() == 'active':
                action = f"[{datetime.now()}] CREATE user: {name} | Role: {role}"
            else:
                action = f"[{datetime.now()}] DISABLE user: {name}"

            print(action)

            with open("logs.txt", "a") as log:
                log.write(action + "\n")

    print("\nProcess completed. Check logs.txt for details.")

if __name__ == "__main__":
    process_users()
