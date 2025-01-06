task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case 'high':
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print("'{task}' is a high priority task but you can do it anytime soon!")
    case 'medium':
        if time_bound == "yes":
            print("'{task}' is a medium priority task that requires average attention but needs to be done soon!")
        else:
            print("'{task}' is a medium priority task that doesn't require immediate attention!")
    case 'low':
        if time_bound == "yes":
            print("'{task}' is a low priority task but have a time bound try to complete it when you have time!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time")
    case _:
        print("Input is not correct.")
