machines = ["Loader 1", "Loader 2", "Haul Truck 7"]
defects = {"Loader 2": "Hydraulic leak at boom cylinder"}

for machine in machines:
    if machine in defects:
        print(f"{machine}: DOWN - {defects[machine]}")
    else:
        print(f"{machine}: ready for inspection")