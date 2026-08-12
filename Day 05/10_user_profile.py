name = input("Enter your name: ").strip().title()
p = name.split()
age = int(input("Enter your age: "))
country = input("Enter your country: ").strip().upper()
email = input("Enter your email: ").strip().lower()
income = float(input("Your monthly income is: "))
username, domain = email.split("@")
print(f"\n-------Profile----------\n")
print(f"{'Name':<16}: {name}")
print(f"{'Age':<16}: {age}")
print(f"{'Country':<16}: {country}")
print(f"{'email':<16}: {email}")
print(f"{'Username is':<16}: {username}")
print(f"{'Email domain is':<16}: {domain}")
print(f"{'Name parts':<16}: {len(p)}")    
print(f"{'Annual income:':<16}: {income*12}")















print(f"{'Full name is':<16}: {name}")