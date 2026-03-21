Reflection & Archiving Habit Tracker
A robust, modular Python application designed to help users track habits while maintaining qualitative context through reflections and long-term data through archiving.

Project Architecture
This project is built following the principles of Object-Oriented Programming (OOP) for data modeling and Functional Programming (FP) for data analysis.
1.	habit.py (Data Model): Encapsulates habit state, streak logic, and serialization.
2.	persistence.py (Storage Layer): Manages JSON file I/O and initializes historical test data.
3.	analytics.py (Analysis Engine): Provides functional utilities to filter, map, and aggregate habit data.
4.	main.py (User Interface): A clean Command-Line Interface (CLI) for user interaction.
5.	test_reflection_tracker.py (Quality Assurance): A suite of unit tests verifying all core logic.

Getting Started
1.	Requirement: Python 3.8 or higher.
2.	Installation: Place all .py files in the same folder.
3.	Launch:
python main.py

4.	Initial State: On the first run, the app generates 4 weeks of simulated data so you can immediately test streaks and analytics.

Testing
The professor requires proof of functionality. Run the following command and take a screenshot of the output:
python test_reflection_tracker.py

Key Features
●	Qualitative Input: Add notes to your completions to track how you felt.
●	Logical Deletion (Archiving): Move old habits to the archive to keep your dashboard clean without losing your historical data.
●	Periodicity Support: Accurate streak tracking for both Daily and Weekly routines.
●	Data Persistence: All progress is automatically saved to habit_data.json.

Academic Integrity & Conventions
●	PEP 8: Follows Python naming conventions (snake_case).
●	Modularity: Logic is strictly separated into modules for maintainability.
●	Docstrings: All classes and functions are documented for readability.
