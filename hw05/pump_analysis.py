def read_pump_data(file_name):
    try:
        with open(file_name, "r") as file:
            return [int(line.rstrip()) for line in file]
    except FileNotFoundError:
        print(f"Unable to open {file_name}")
        return None


def calculate_pump_activity(data, pump_power_threshold=500, pump_flow_rate=2):
    running_minutes = sum(1 for power in data if power >= pump_power_threshold)
    total_gallons = running_minutes * pump_flow_rate
    total_power = sum(data)
    return running_minutes, total_gallons, total_power


# Move this function outside of print_report to make it available globally
def minutes_to_reach_gallons(
    data, target_gallons, pump_flow_rate, pump_power_threshold=500
):
    cumulative_gallons = 0
    for i, power in enumerate(data):
        if power >= pump_power_threshold:
            cumulative_gallons += pump_flow_rate
        if cumulative_gallons >= target_gallons:
            return i + 1
    return -1


def generate_report(file_name, targets):
    data = read_pump_data(file_name)
    if data is None:
        return

    total_minutes = len(data)
    hours = total_minutes / 60
    days = hours / 24

    pump_power_threshold = 500  # threshold to consider pump running
    pump_flow_rate = 2  # gallons per minute

    running_minutes, total_gallons, total_power = calculate_pump_activity(
        data, pump_power_threshold, pump_flow_rate
    )
    avg_daily_gallons = total_gallons / days if days > 0 else 0

    total_kwh = total_power / 1000 / 60

    # Build the report as a string
    report = (
        f"Data covers a total of {hours:.1f} hours\n"
        f"(That's {days:.3f} days)\n\n"
        f"Pump was running for {running_minutes} minutes, producing {total_gallons} gallons\n"
        f"(That's {avg_daily_gallons:.1f} gallons per day)\n\n"
        f"Pump required a total of {total_power} watt minutes of power\n"
        f"That's {total_kwh:.3f} kWh\n\n"
    )

    # Time to reach specified water amounts
    for gallons in targets:
        minutes = minutes_to_reach_gallons(
            data, gallons, pump_flow_rate, pump_power_threshold
        )
        if minutes == -1:
            report += f"It took -1 minutes of data to reach {gallons} gallons.\n"
        else:
            report += f"It took {minutes} minutes of data to reach {gallons} gallons.\n"

    return report


def print_report(file_name):
    targets_input = input(
        "Please enter the target gallon amounts separated by commas (e.g., 5,100): "
    )
    targets = [int(gallon.strip()) for gallon in targets_input.split(",")]
    report = generate_report(file_name, targets)
    print(report)


if __name__ == "__main__":
    file_name = input("Please enter the file name: ")
    print_report(file_name)
