
import persistence
import analytics
from habit import Habit

def display_menu(habits):
    active = analytics.get_active_habits(habits)
    score = analytics.calculate_total_consistency_score(habits)
    print("\n" + "="*45)
    print(" REFLECTION & ARCHIVING HABIT TRACKER ")
    print("="*45)
    print(f"Active Habits: {len(active)} | Consistency Score: {score}")
    print("-" * 45)
    print("1. View My Active Habits & Streaks")
    print("2. Check-off Habit (Log Progress & Note)")
    print("3. Create New Habit")
    print("4. Analytics Dashboard")
    print("5. Archive/Unarchive a Habit")
    print("6. Exit")
    print("-" * 45)

def run():
    habits = persistence.load_all()

    while True:
        display_menu(habits)
        choice = input("Enter choice (1-6): ")

        if choice == '1':
            active = analytics.get_active_habits(habits)
            print("\nYOUR CURRENT HABITS:")
            for h in active:
                print(f"• [{h.name}] | Streak: {h.get_streak()} {h.periodicity}")

        elif choice == '2':
            name = input("Enter habit name to complete: ")
            h = analytics.find_habit(habits, name)
            if h and not h.is_archived:
                note = input("Add a reflection for today (Optional): ")
                h.add_completion(reflection=note)
                persistence.save_all(habits)
                print(f"Success! {h.name} logged. Current streak: {h.get_streak()}")
            else:
                print("Error: Active habit not found.")

        elif choice == '3':
            name = input("Habit Name: ")
            period = input("Periodicity (daily/weekly): ").lower()
            if period in ['daily', 'weekly']:
                habits.append(Habit(name, period))
                persistence.save_all(habits)
                print(f"Habit '{name}' created!")
            else:
                print("Invalid periodicity.")

        elif choice == '4':
            print("\n--- ANALYTICS DASHBOARD ---")
            print(f"Global Longest Streak: {analytics.get_longest_streak_all(habits)}")
            print(f"Daily Habits Count: {len(analytics.get_habits_by_periodicity(habits, 'daily'))}")
            print(f"Total Reflections Logged: {len(analytics.get_all_reflections(habits))}")

        elif choice == '5':
            name = input("Enter habit name to archive/unarchive: ")
            h = analytics.find_habit(habits, name)
            if h:
                h.toggle_archive()
                persistence.save_all(habits)
                status = "Archived" if h.is_archived else "Restored"
                print(f"Habit '{h.name}' has been {status}.")
            else:
                print("Habit not found.")

        elif choice == '6':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run()