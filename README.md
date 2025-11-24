 Overview of the Project:-The Bank Management System (BMS) is a console application developed to    
                        simulate essential banking operations. It allows a bank teller or administrator to manage customer accounts, process financial transactions (deposits and withdrawals), and check account balances. The project primarily demonstrates the practical application of database integration using SQLite and fundamental procedural programming concepts in Python.
Features:-
Secure Authentication: Requires a hardcoded username and password (Abhi, 1234) for system 
                        access.
Account Creation: Registers new accounts by collecting customer details 
                    (Name, Aadhaar, Phone, Age, Gender).Includes validation to check for duplicate Aadhaar Numbers and a 10-digit Phone Number.
Transaction Processing:Handles Deposits and updates the account balance.Handles Withdrawals with a 
                        critical check for Insufficient Balance.
Balance Inquiry: Allows quick retrieval and display of the current balance for any account using 
                the Aadhaar number.Data Persistence: All account data is stored permanently in a structured SQLite database file (BANK.db).
 Technologies/Tools Used
 core language         python3
 database              SQLite3
 library               sqlite3
 version control       Git
Steps to Install & Run the ProjectClone the Repository:
1. git clone [Your_Repository_URL]
Navigate to the Project Directory:
2. cd bank-management-system
Run the Application:
The system uses Python's standard libraries, so no extra installations are needed.Execute the main script (assuming your file is named main.py):
3. python main.py
The system will automatically create the BANK.db file upon first execution. Instructions for TestingUse the following scenarios to verify all key functionalities and error handling:
Login Test:Enter username Abhi and password 1234. 
Verify access to the main menu.
Account Creation Test (Choice 1):Create a new account.
Attempt to create a second account using the same Aadhaar Number (Verify the "Account already exists" error).
Attempt to enter a phone number that is not 10 digits (Verify the validation error).
Deposit Test (Choice 2) & Balance Check (Choice 4):Deposit an amount (e.g., 5000) into the new account.Immediately use Choice 4 to check the balance and confirm it reflects the deposit.Withdrawal Test (Choice 3):Success Case: Withdraw an amount less than the current balance (e.g., 1000). Check the balance to confirm the deduction.Failure Case (Critical Logic Check): Attempt to withdraw an amount greater than the remaining balance (Verify the "Insufficient balance!" error message).Exit Test (Choice 5):Select option 5 to confirm the application gracefully closes the database connection and exits.