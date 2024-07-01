Pomodoro Timer

A simple Pomodoro timer application to help you manage your time using the Pomodoro Technique.
Features

    Set a Pomodoro timer for 25 minutes of work.
    Set short breaks (5 minutes) and long breaks (20 minutes).
    Notifications when the timer ends.
    Keeps track of the total time passed.

Requirements

    Python 3.x
    Tkinter library (usually included with Python)

Installation

    Ensure that Python 3 is installed on your system.
    Download or clone the project from the repository.
    Open the command line and navigate to the project directory.
    (Optional) Create a virtual environment and activate it.
    Install required libraries (if any additional ones are needed).

How to Use

    Open the command line and navigate to the project directory.

    Run the program using the command:

    bash

    python pomodoro_timer.py

    The Pomodoro Timer window will open.

    Click on the "Start" button to begin a Pomodoro session.

    The timer will count down from 25 minutes, followed by a short break. After four Pomodoros, a long break will be initiated.

    Click on the "Reset" button to reset the timer and view the time passed in the session.

Code Overview
Constants

    PINK, RED, GREEN, YELLOW, BLUE: Color constants used in the UI.
    FONT_NAME: The font used for text in the UI.
    WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN: Duration constants for work sessions and breaks.
    SECOND: Duration of a second in milliseconds.

Functions

    reset_timer(): Resets the timer and displays a summary of the time passed.
    add_check_mark(): Adds a check mark after each Pomodoro session.
    start_timer(): Starts the timer and alternates between work and break sessions.
    english_to_arabic(number): Converts an English number to an Arabic number (for UI display).
    count_down(count): Counts down from the specified time and updates the UI.

UI Setup

    The main window is created using Tkinter.
    The timer is displayed using a canvas with an image of a tomato.
    Labels and buttons are used to control the timer and display information.

Example Screenshot

(Include a screenshot of the running application here)
License

This project is open-source and available under the MIT License.
