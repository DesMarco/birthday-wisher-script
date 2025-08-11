# Birthday Wisher Script

This Python script reads a list of birthdays from a CSV file and automatically sends personalized birthday emails using letter templates.  
It picks a random letter template, replaces the placeholder `[NAME]` with the recipient's actual name, and sends the message via SMTP.

## Features
- Reads birthdays from a CSV file
- Sends customized emails on matching birthday dates
- Uses multiple letter templates for variety
- Easy to configure with your email and app password

## How to Use
1. Add your email credentials in the script.
2. Prepare a `birthdays.csv` with names and dates.
3. Add letter templates in the `letter_templates` folder with `[NAME]` as a placeholder.
4. Run the script on the day you want to send the wishes.

## Requirements
- Python 3.x
- `smtplib` (built-in)
- Access to a SMTP server (e.g., Gmail with App Password)

## Notes
Make sure to keep your credentials secure and do not commit them to public repos.

---

*Simple and useful script to never forget a birthday!*
