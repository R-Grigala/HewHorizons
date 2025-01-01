hour = int(input("Starting time (hours): "))
minute = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

def calculate_end_time(start_hour, start_minute, duration_minutes):

    total_start_minutes = start_hour * 60 + start_minute
    total_end_minutes = total_start_minutes + duration_minutes
    
    # Calculate the end time in hours and minutes
    end_hour = (total_end_minutes // 60) % 24
    end_minute = total_end_minutes % 60

    print(f"The event will end at {end_hour:02}:{end_minute:02}")

# Example usage
calculate_end_time(hour, minute, duration)