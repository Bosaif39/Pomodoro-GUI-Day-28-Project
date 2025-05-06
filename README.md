# **Pomodoro Timer**

## **Overview:**
This is the Day 28 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

The Pomodoro Timer is a productivity tool that helps users break work into intervals (typically 25 minutes), separated by short breaks. After several work sessions, a longer break is taken.

This app visualizes the Pomodoro process using a tomato timer graphic, and includes session tracking through checkmarks.

## **How It Works:**
1. Click the **Start** button to begin a work session.
2. The app will automatically alternate between:
   - **Work sessions**
   - **Short breaks** (after each work session)
   - **A long break** (after every 4 work sessions)
3. A checkmark (✔) is added below the timer for each completed work session.
5. Click **Reset** at any time to stop the timer and reset progress.
6. The user can use the **dropdown menu** to choose work minutes, short breaks and long breaks. Otherwise, it will be 25 min, 5 min and 20 respectively.

## **Session Cycle:**
- 1st → Work  
- 2nd → Short Break  
- 3rd → Work  
- 4th → Short Break  
- 5th → Work  
- 6th → Short Break  
- 7th → Work  
- 8th → Long Break  

## **Example:**
![alt text](https://raw.githubusercontent.com/Bosaif39/example-pics/refs/heads/main/D_28.png?token=GHSAT0AAAAAADDL7KRAMELD5POB3EBXMY342AZUVDA)

## **Requirements:**
- Python 3.x
- Tkinter (pre-installed with Python)
- A tomato image named `tomato.png` in the same directory
