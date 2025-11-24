1. Problem Statement
Traditional banking operations require an organized, secure, and efficient system for managing customer accounts and processing financial transactions. The fundamental problem addressed by this project is the lack of a simplified, reliable, and persistent digital system that can effectively manage customer data and core transactions (deposit and withdrawal). The implementation of this system minimizes reliance on manual records and serves as a practical demonstration of database integration and essential system design principles.
Scope of the Project
2. The scope of this Bank Management System (BMS) is focused on simulating the core, day-to-day operations of a single bank branch using a command-line interface (CLI).

 In-Scope:

Account Management: Creation, retrieval, and modification of account records.

Core Transactions: Handling deposits and withdrawals with logical checks (e.g., insufficient funds).

Data Persistence: Storing all customer and transaction data reliably using a local SQLite database.

Out-of-Scope:

Advanced banking features (e.g., interest calculation, loan processing, fixed deposits).

Complex security features (e.g., password hashing, user roles beyond basic admin).

Multi-user concurrency control or networking capabilities.

3. Target Users
The system is primarily designed for individuals who directly interact with customer accounts.

Primary Users: Bank Tellers or Administrators who use the system's menu to process transactions and manage customer records.

Secondary Users: Developers and Students reviewing the code to understand the application of Python, SQLite, and system design concepts.

 4. High-Level Features
Secure Access: Implement basic credential-based access to protect the system's operational menu.

Customer Account Management: Provide functionality to register new customers and retrieve their account details using a unique identifier (Aadhaar Number).

Financial Transaction Processing: Allow tellers to execute deposits and withdrawals quickly and reliably.

Transaction Validation: Enforce business rules, most notably the check for sufficient balance before processing any withdrawal.

Persistent Data Storage: Ensure all system states (account balances, customer details) are saved immediately to the database for reliability.