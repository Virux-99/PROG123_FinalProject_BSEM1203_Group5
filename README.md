# PROG123_FinalProject_BSEM1203_Group5
 Project Overview
The Market Management System is a desktop application developed using Python and Tkinter. It is designed to manage client transactions and stock records in a structured and efficient way. The system allows users to record client purchases, manage stock information, and view analytical results using charts.

The application stores all data in JSON files to ensure permanent storage and easy retrieval of records.

Features
 Client Management
- Record client transactions
- Store client details such as name, goods, quantity, total amount, payment, and date
- Automatically calculate remaining balance
- Assign transaction status as Complete or Due
- Validate all input before saving

Stock Management
- Add new stock items
- Store stock name, quantity, cost price, and selling price
- Automatically calculate profit per stock item
- Validate stock input data before saving

 Data Visualization
- Pie chart showing top 10 most sold goods
- Bar chart showing monthly profit
- Graphical representation using Matplotlib

Search and Filter System
- Filter records by month, year, day, and status
- Status options include Complete and Due
- Displays filtered results in a scrollable interface
- Includes input validation and error handling

 Technologies Used
- Python
- Tkinter for graphical user interface
- JSON for data storage
- Matplotlib for charts
- datetime module for date handling

Data Storage
The system uses two main JSON files:
- clients.json for storing client transaction records
- stocks.json for storing stock information

Data is automatically saved whenever a new record is added.

 System Workflow
1. User logs into the system
2. Main menu provides access to:
   - Client records
   - Stock records
   - View and charts
   - Search records
3. Data is validated before saving
4. Records are stored in memory and written to JSON files
5. Charts and filters are used for analysis

 System Structure
The project is divided into three main modules:
- Main module: Handles user interface and system navigation
- Save module: Handles file operations and data storage
- Input validation module: Ensures correctness of user input

overall
The Market Management System demonstrates structured programming using Python. It combines file handling, input validation, graphical user interface design, and data visualization to create a functional system suitable for managing small business transactions.
