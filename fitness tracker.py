import random
import datetime

class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.daily_steps = 0
        self.goal_steps = 10000  # Default daily steps goal
        self.last_sync_date = None

    def set_goal(self, goal):
        self.goal_steps = goal

    def sync(self):
        # Simulate syncing with a hypothetical API
        self.last_sync_date = datetime.datetime.now()
        print("Syncing data...")

    def record_steps(self, steps):
        self.daily_steps += steps
        print(f"Recorded {steps} steps today.")

    def check_progress(self):
        if self.last_sync_date is None:
            print("Sync your data first.")
            return

        days_since_last_sync = (datetime.datetime.now() - self.last_sync_date).days
        if days_since_last_sync > 0:
            print("Syncing data from the last sync date...")
            self.sync()

        if self.daily_steps >= self.goal_steps:
            print(f"Congratulations, {self.user_name}! You've reached your daily step goal of {self.goal_steps} steps.")
        else:
            remaining_steps = self.goal_steps - self.daily_steps
            print(f"{self.user_name}, you have {remaining_steps} steps left to reach your goal of {self.goal_steps} steps today.")

    def suggest_activity(self):
        # Suggest a random activity based on the current step count
        if self.daily_steps < 1000:
            print("You need to move more today. Consider taking a short walk.")
        elif self.daily_steps < 5000:
            print("You're making progress! Try going for a jog or cycling.")
        else:
            print("Great job! You've been active today. Keep it up!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    tracker = FitnessTracker(user_name)

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Record Steps")
        print("2. Set Daily Step Goal")
        print("3. Check Progress")
        print("4. Suggest Activity")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            steps = int(input("Enter the number of steps: "))
            tracker.record_steps(steps)
        elif choice == "2":
            goal = int(input("Enter your daily step goal: "))
            tracker.set_goal(goal)
        elif choice == "3":
            tracker.check_progress()
        elif choice == "4":
            tracker.suggest_activity()
        elif choice == "5":
            print("Exiting the Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


