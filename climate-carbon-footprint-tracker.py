# ==========================================================
# PROJECT: CLIMATE & CARBON FOOTPRINT TRACKER
# SDG 13: CLIMATE ACTION
# Language: Python
# Purpose: Educational carbon footprint estimation
# ==========================================================

from datetime import datetime

print("=" * 60)
print("       CLIMATE & CARBON FOOTPRINT TRACKER")
print("              SDG 13: CLIMATE ACTION")
print("=" * 60)

print("\nWelcome!")
print("Estimate your monthly carbon emissions and")
print("explore ways to reduce your environmental impact.")

print("\nNOTE:")
print("The default emission factors are illustrative estimates.")
print("They are not official or certified emission values.")

# ----------------------------------------------------------
# 1. INPUT MONTHLY ACTIVITY DATA
# ----------------------------------------------------------

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter a non-negative number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


print("\n--- MONTHLY ACTIVITY DATA ---")

electricity = get_number(
    "Electricity consumption (kWh): "
)

car = get_number(
    "Car travel distance (km): "
)

bus = get_number(
    "Bus travel distance (km): "
)

train = get_number(
    "Train/metro travel distance (km): "
)

flight = get_number(
    "Flight distance (passenger-km): "
)

# ----------------------------------------------------------
# 2. EMISSION FACTORS
# ----------------------------------------------------------

print("\n--- EMISSION FACTORS ---")
print("You can use the illustrative default values below.")

ef_electricity = 0.70
ef_car = 0.12
ef_bus = 0.05
ef_train = 0.03
ef_flight = 0.15

print(f"Electricity: {ef_electricity} kg CO2/kWh")
print(f"Car:         {ef_car} kg CO2/km")
print(f"Bus:         {ef_bus} kg CO2/km")
print(f"Train/metro: {ef_train} kg CO2/km")
print(f"Flight:      {ef_flight} kg CO2/passenger-km")

# ----------------------------------------------------------
# 3. CALCULATE EMISSIONS
# ----------------------------------------------------------

emissions = {
    "Electricity": electricity * ef_electricity,
    "Car Travel": car * ef_car,
    "Bus Travel": bus * ef_bus,
    "Train/Metro": train * ef_train,
    "Flights": flight * ef_flight
}

total_emissions = sum(emissions.values())
daily_average = total_emissions / 30

# ----------------------------------------------------------
# 4. DISPLAY CARBON FOOTPRINT REPORT
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             MONTHLY EMISSIONS REPORT")
print("=" * 60)

print(f"{'Activity':<20}{'Emissions (kg CO2)':>25}")
print("-" * 45)

for activity, amount in emissions.items():
    print(f"{activity:<20}{amount:>25.2f}")

print("-" * 45)

print(f"{'TOTAL':<20}{total_emissions:>25.2f}")

print(f"\nApproximate daily average: {daily_average:.2f} kg CO2")

# ----------------------------------------------------------
# 5. IDENTIFY THE LARGEST EMISSION SOURCE
# ----------------------------------------------------------

print("\n--- EMISSION ANALYSIS ---")

if total_emissions > 0:

    largest_source = max(
        emissions,
        key=emissions.get
    )

    largest_amount = emissions[largest_source]

    percentage = (
        largest_amount / total_emissions
    ) * 100

    print("Largest emission source:", largest_source)
    print(f"Estimated emissions: {largest_amount:.2f} kg CO2")
    print(f"Share of total emissions: {percentage:.1f}%")

else:
    print("No emissions were calculated.")
    print("Enter activity data greater than zero to analyze.")

# ----------------------------------------------------------
# 6. PERSONALIZED CLIMATE ACTION SUGGESTIONS
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             SUGGESTED CLIMATE ACTIONS")
print("=" * 60)

suggestions = []

if car > 0:
    suggestions.append(
        "Consider walking, cycling, carpooling, or public transport."
    )

if electricity > 0:
    suggestions.append(
        "Switch off unused electrical devices and lights."
    )

if bus + train > 0:
    suggestions.append(
        "Continue using shared transport where practical."
    )

if flight > 0:
    suggestions.append(
        "Compare lower-emission travel alternatives when practical."
    )

if total_emissions == 0:
    suggestions.append(
        "Enter monthly activity data to receive relevant suggestions."
    )

suggestions.append(
    "Record monthly activities to track changes over time."
)

for number, suggestion in enumerate(suggestions, start=1):
    print(f"{number}. {suggestion}")

# ----------------------------------------------------------
# 7. WHAT-IF CARBON REDUCTION SIMULATOR
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             CARBON REDUCTION SIMULATOR")
print("=" * 60)

active_sources = {
    activity: amount
    for activity, amount in emissions.items()
    if amount > 0
}

if active_sources:

    print("\nChoose an activity to reduce:")

    activities = list(active_sources.keys())

    for number, activity in enumerate(activities, start=1):
        print(f"{number}. {activity}")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))

            if 1 <= choice <= len(activities):
                break

            print("Please choose a valid activity number.")

        except ValueError:
            print("Please enter a valid integer.")

    selected_activity = activities[choice - 1]

    while True:
        reduction = get_number(
            "Enter hypothetical reduction percentage (0-50): "
        )

        if reduction <= 50:
            break

        print("Please enter a percentage between 0 and 50.")

    saved_emissions = (
        active_sources[selected_activity] * reduction / 100
    )

    projected_emissions = total_emissions - saved_emissions

    print("\n--- SIMULATION RESULTS ---")
    print("Selected activity:", selected_activity)
    print(f"Reduction selected: {reduction:.1f}%")

    print(
        f"Potential monthly reduction: "
        f"{saved_emissions:.2f} kg CO2"
    )

    print(
        f"Projected monthly emissions: "
        f"{projected_emissions:.2f} kg CO2"
    )

    print(
        "\nNote: These results are hypothetical estimates, "
        "not guaranteed reductions."
    )

else:
    print("Enter at least one non-zero activity to run a simulation.")

# ----------------------------------------------------------
# 8. GENERATE A DOWNLOADABLE CSV REPORT
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             SAVE YOUR REPORT")
print("=" * 60)

save_report = input(
    "Save the report as a CSV file? (yes/no): "
).strip().lower()

if save_report in ("yes", "y"):

    filename = "carbon_footprint_report.csv"

    try:
        with open(filename, "w", encoding="utf-8") as file:

            file.write("Climate & Carbon Footprint Tracker\n")
            file.write("SDG 13: Climate Action\n")
            file.write(
                "Report generated,"
                + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n\n"
            )

            file.write(
                "Activity,Monthly Usage,Unit,"
                "Emission Factor,Estimated Emissions (kg CO2)\n"
            )

            report_data = [
                ("Electricity", electricity, "kWh", ef_electricity),
                ("Car Travel", car, "km", ef_car),
                ("Bus Travel", bus, "km", ef_bus),
                ("Train/Metro", train, "km", ef_train),
                ("Flights", flight, "passenger-km", ef_flight)
            ]

            for activity, usage, unit, factor in report_data:
                result = usage * factor

                file.write(
                    f"{activity},{usage},{unit},{factor},{result:.2f}\n"
                )

            file.write(
                f"\nTotal monthly emissions (kg CO2),"
                f"{total_emissions:.2f}\n"
            )

            file.write(
                f"Approximate daily average (kg CO2),"
                f"{daily_average:.2f}\n"
            )

        print(f"\nReport saved as {filename}")

        print(
            "If your online compiler supports file downloads, "
            "download the generated CSV file from its file panel."
        )

    except OSError:
        print(
            "The compiler could not save the report. "
            "You can still view your results above."
        )

else:
    print("Report not saved.")

# ----------------------------------------------------------
# 9. PROJECT METHODOLOGY
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("             PROJECT METHODOLOGY")
print("=" * 60)

print("Calculation: Activity amount x Emission factor.")

print("\nProject limitations:")
print("- Emission factors are illustrative estimates.")
print("- Electricity and selected travel activities are included.")
print("- Food, shopping, waste, and other indirect emissions")
print("  are excluded.")
print("- Results depend on the accuracy of the input data.")
print("- The application is an educational prototype.")

print("\nProject objective:")
print("Promote climate awareness and encourage responsible")
print("energy use and lower-emission travel choices.")

print("\nThank you for using the tracker!")
print("Together, we can support SDG 13: Climate Action.")

print("=" * 60)
