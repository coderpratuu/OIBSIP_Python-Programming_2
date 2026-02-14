# OIBSIP_Python-Programming_2

📌 Project Objective

The objective of this project is to develop a Body Mass Index (BMI) Calculator using Python. The application calculates BMI based on user input (weight and height), categorizes the result according to standard health ranges, and provides a simple graphical user interface for better user experience.

The project demonstrates the integration of mathematical computation, input validation, GUI development, and basic data handling.

🛠 Tools and Technologies Used

Python 3

Tkinter (for GUI development)

SQLite3 (for data storage)

Matplotlib (for BMI trend visualization)

Datetime Module (for recording date and time)

🧱 Project Structure

GUI Interface for entering:

Name

Weight (kg)

Height (m)

BMI Calculation Module

BMI Category Classification

Data Storage using SQLite database

History Viewer

BMI Trend Graph

⚙️ Steps Performed
1️⃣ GUI Design

Created a user-friendly interface using Tkinter.

Added input fields for name, weight, and height.

Designed buttons for calculating BMI, viewing history, and displaying graph.

Applied a simple styled theme for better appearance.

2️⃣ BMI Calculation Implementation

Used the standard BMI formula:

𝐵
𝑀
𝐼
=
𝑊
𝑒
𝑖
𝑔
ℎ
𝑡
𝐻
𝑒
𝑖
𝑔
ℎ
𝑡
2
BMI=
Height
2
Weight
	​


Rounded result to two decimal places.

3️⃣ Categorization

BMI results are classified into health categories:

Underweight (BMI < 18.5)

Normal Weight (18.5 – 24.9)

Overweight (25 – 29.9)

Obese (30 and above)

4️⃣ Input Validation

Ensured weight and height are positive numbers.

Handled invalid or empty inputs using error messages.

5️⃣ Data Storage

Created a SQLite database to store:

Name

Weight

Height

BMI value

Date and time

Saved records automatically after each calculation.

6️⃣ Data Visualization

Retrieved stored BMI records.

Plotted BMI trends over time using Matplotlib.

Displayed graph showing BMI progression.

🔄 How the Application Works

User enters name, weight, and height.

Application validates inputs.

BMI is calculated using the formula.

Result and category are displayed.

Data is stored in the database.

User can:

View previous BMI records.

Display BMI trend graph.

✅ Key Features

Accurate BMI calculation

Automatic category classification

Error handling and validation

Multiple user record storage

History viewing

BMI trend visualization

Clean and responsive GUI


🚀 Outcome

The final outcome is a fully functional BMI Calculator application that not only calculates BMI but also stores and visualizes historical data.

The project successfully combines beginner-level concepts (calculation and conditions) with intermediate-level concepts (GUI, database, and graph visualization), making it both educational and practical.
