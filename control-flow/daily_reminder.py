# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process priority using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task. Try to schedule it soon."
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"'{task}' has an unrecognized priority level."

# Add time-sensitive note if applicable
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"

# Output the final reminder
print(message)
