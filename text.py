import re

print("📧 Email Extractor Tool")

# Read input file
with open("D:/codealpha/input.txt", "r") as file:
    content = file.read()

# Find all email addresses using regex
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", content)

# Save emails to output file
with open("emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("✅ Emails extracted and saved to emails.txt")