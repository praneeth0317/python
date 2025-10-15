items = ["laptop", "mouse", "keyboard", "monitor"]
for item in items:
    if item == "keyboard":
        print("Keyboard found! Stopping search.")
        break
    print(f"Checking {item}...")
