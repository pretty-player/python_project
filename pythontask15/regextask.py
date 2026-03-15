import re

def regex_demo():
    # Ask the user for input
    text = input("Enter a text containing emails, phone numbers, and spaces: ")
    print("\n" + "="*30)

    # 1. Find all Email Addresses using findall()
    # Pattern: words/dots + @ + words/dots + domain(2-4 chars)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}'
    emails = re.findall(email_pattern, text)
    print(f"Emails found: {emails if emails else 'None'}")

    # 2. Check if a Phone Number exists and is valid using search()
    # Format: 10 digits (Example: 1234567890 or 123-456-7890)
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"Valid Phone Number found: {phone_match.group()}")
    else:
        print("No valid 10-digit phone number found.")

    # 3. Replace all spaces with underscores using sub()
    # \s matches any whitespace character
    modified_text = re.sub(r'\s', '_', text)
    print(f"Modified text (spaces to underscores): {modified_text}")
    print("="*30)

if __name__ == "__main__":
    regex_demo()