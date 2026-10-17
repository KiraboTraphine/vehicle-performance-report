def calculate_efficiency(distance, fuel):
    return distance / fuel


def classify_vehicle(efficiency):
    if efficiency >= 15:
        return "Efficient"
    elif efficiency >= 10:
        return "Moderate"
    else:
        return "Inefficient"


def process_vehicles():
    vehicles = []

    try:
        count = int(input("Number of vehicles: "))
    except ValueError:
        print("Invalid number of vehicles")
        return

    if count <= 0:
        print("Number of vehicles must be greater than zero")
        return

    for i in range(count):

        print("\nVehicle", i + 1)

        registration = input("Registration: ")

        try:
            distance = float(input("Distance travelled: "))
            fuel = float(input("Fuel consumed: "))
        except ValueError:
            print("Distance and fuel must be numeric")
            continue

        if distance < 0:
            print("Negative distance is not allowed")
            continue

        if fuel < 0:
            print("Negative fuel quantity is not allowed")
            continue

        if fuel == 0:
            print("Fuel consumption cannot be zero")
            continue

        efficiency = calculate_efficiency(distance, fuel)
        classification = classify_vehicle(efficiency)

        vehicles.append({
            "registration": registration,
            "distance": distance,
            "fuel": fuel,
            "efficiency": efficiency,
            "classification": classification
        })

    print("\nVEHICLE PERFORMANCE REPORT")

    if not vehicles:
        print("No valid vehicle records available.")
        return

    total_efficiency = 0
    highest_efficiency = vehicles[0]["efficiency"]

    for vehicle in vehicles:

        print(
            "Registration:", vehicle["registration"],
            "| Distance:", vehicle["distance"], "km",
            "| Fuel:", vehicle["fuel"], "litres",
            "| Efficiency:", round(vehicle["efficiency"], 2), "km/litre",
            "| Classification:", vehicle["classification"]
        )

        total_efficiency += vehicle["efficiency"]

        if vehicle["efficiency"] > highest_efficiency:
            highest_efficiency = vehicle["efficiency"]

    average_efficiency = total_efficiency / len(vehicles)

    print("\nHighest fuel efficiency:",
          round(highest_efficiency, 2), "km/litre")

    print("Average fuel efficiency:",
          round(average_efficiency, 2), "km/litre")


process_vehicles()