# State
**Progress**

# Project Overview
"PyQtCaminando_Deprisa", is an easy-to-use PyQt5-based CRUD (Create, Read, Update, Delete) application, specifically designed to integrate seamlessly with MySQL databases. This project serves as a practical implementation for the Software Engineering class in which the following case was addressed:

The company Caminando de Prisa is having serious problems because billing is done manually, so it has decided to hire you as a Systems Engineer to develop billing software tailored to your needs.

In the interview, the Director of the company informs you what you have and what you want for your company:

1. The company is a seller of office supplies.
2. The budget is limited since it is a small institution.
3. There are no computers, they will have to be obtained for the implementation and development of the software.
4. The software is needed to be ready within one month from the date.
5. The system will keep track of sequentially numbered invoices.
6. You will have the option to calculate and invoice with or without VAT.
7. You will have the option to apply a discount, where the cashier can enter the discount percentage to apply, according to some rules established by the company.
8. The items to be invoiced must be obtained from a database, which the company will provide.
9. At the end of the day, a cash count format is generated on the screen, where the cashier will enter the data and the system will add up the consecutive invoices and print the day's cash balance.
10. It is desired that a weekly and biweekly sales report be generated.
11. That it has passwords to access the system.

## Prerequisites
Before you begin, make sure MySQL Server is installed on your system. If it is not already installed, you can download it from the official MySQL website.

# Installation Guide
To get started with "PyQtCaminando_Deprisa", follow these simple installation steps:

1. **Open Your Terminal:**
   Begin by opening your terminal or command prompt.

2. **Clone the Repository:**
   Use the following command to clone the project repository and navigate into the project directory:

   ```sh
   git clone https://github.com/osmarmora05/PyQtCaminando_Deprisa && cd PyQtCaminando_Deprisa
   ```

3. **Set Up a Virtual Environment:**
   Create a virtual environment to manage the project's dependencies separately:

   ```sh
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   Depending on your operating system, activate the virtual environment using one of these commands:

   - Windows:

     ```sh
     .\venv\Scripts\activate
     ```

   - Unix/Linux:
     ```sh
     source venv/bin/activate
     ```

5. **Install Required Dependencies:**
   Install all the necessary Python packages as listed in the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

Once the setup is complete, you're ready to launch the application. Execute the following command to start "PyQtCaminando_Deprisa":

```sh
python main.py
```