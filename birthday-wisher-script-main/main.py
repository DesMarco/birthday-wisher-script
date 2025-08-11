import random
import datetime as dt
import smtplib

# Your Google App password for Gmail
password = "HERE_YOUR_GOOGLE_APP_PASSWORD"

# Sender email
email_from = "YOUR_EMAIL"

# Receiver email
email_to = "DESTINATION_EMAIL"

# List to store birthday info from CSV
birthdays = []

# Read the CSV file with birthdays
with open("birthdays.csv", "r", encoding="utf-8") as file:
    next(file)  # Skip the header line
    for linea in file:
        linea = linea.strip()
        if linea:  # Ignore empty lines
            elementos = linea.split(",")  # Split by comma
            birthdays.append(elementos)

# Get today's date
today = dt.datetime.today()
today_day = today.day
today_month = today.month

# Loop through each birthday entry
for n in range(len(birthdays)):
    # Check if today matches the birthday
    if int(birthdays[n][3]) == today_month and int(birthdays[n][4]) == today_day:
        birthday_name = birthdays[n][0]
        
        # Choose a random letter template file
        filename = f"letter_templates/letter_{random.randint(1,3)}.txt"

        # Read the original template file
        with open(filename, "r", encoding="utf-8") as file:
            contenido = file.read()

        # Replace [NAME] with the real person's name in memory (not in file)
        contenido_modificado = contenido.replace("[NAME]", birthday_name)

        # Send the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=email_from, password=password)  # Login to Gmail
            connection.sendmail(
                from_addr=email_from,
                to_addrs=email_to,
                msg=f"Subject: HAPPY BIRTHDAY\n\n{contenido_modificado}"
            )
