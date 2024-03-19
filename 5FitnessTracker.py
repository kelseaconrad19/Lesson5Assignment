# Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.
def log_activity(activity_list, duration_list):
    compilation = zip(activity_list, duration_list)
    log = list(compilation)
    return log


# Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
def calorie_calculator(log):
    calorie_list = []
    for activity in log:
        time = activity[1]
        calories_burned = time * 3.5
        calorie_list.append(calories_burned)
    return calorie_list


# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
def summary(activity_list, cal_list):
    index = 0
    for i in range(len(activity_list)):
        activity = activity_list[i]
        cals = cal_list[i]
        print(f"You burned {cals} calories {activity}! Great job!")


activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

activity_log = log_activity(activities, duration)
calories = calorie_calculator(activity_log)
summary(activities, calories)

