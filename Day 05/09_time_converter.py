time = int(input("Enter total seconds: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
print(f"{'Hours':<16}: {hours}")
print(f"{'Minutes':<16}: {minutes}")
print(f"{'Seconds':<16}: {seconds}")