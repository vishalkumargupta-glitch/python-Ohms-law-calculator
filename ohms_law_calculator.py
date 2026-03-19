print("=== Simple Ohm's Law & Power Calculator ===")
print("   V = Voltage (Volts)")
print("   I = Current (Amps)")
print("   R = Resistance (Ohms)")
print("   P = Power (Watts)\n")

while True:
    print("\nWhat do you know? Choose:")
    print("1 = I know Voltage and Resistance")
    print("2 = I know Voltage and Current")
    print("3 = I know Current and Resistance")
    print("4 = Exit")
    
    choice = input("Enter number (1-4): ")
    
    if choice == "4":
        print("Thank you for using the calculator!")
        break
    
    if choice == "1":
        v = float(input("Voltage (V): "))
        r = float(input("Resistance (Ω): "))
        if r == 0:
            print("Error: Resistance cannot be zero!")
            continue
        i = v / r
        p = v * i
        print(f"Current = {i:.3f} A")
        print(f"Power   = {p:.3f} W")
        
    elif choice == "2":
        v = float(input("Voltage (V): "))
        i = float(input("Current (A): "))
        if i == 0:
            print("Error: Current cannot be zero for resistance calculation!")
            continue
        r = v / i
        p = v * i
        print(f"Resistance = {r:.2f} Ω")
        print(f"Power      = {p:.3f} W")
        
    elif choice == "3":
        i = float(input("Current (A): "))
        r = float(input("Resistance (Ω): "))
        v = i * r
        p = i * i * r
        print(f"Voltage = {v:.2f} V")
        print(f"Power   = {p:.3f} W")
    
    else:
        print("Invalid choice, try again.")