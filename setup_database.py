# Database Setup Script for Hospital Management System

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the database and table for the hospital management system"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # Change this to your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS kdastestdb")
            print("Database 'kdastestdb' created successfully!")
            
            # Use the database
            cursor.execute("USE kdastestdb")
            
            # Create table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS hospital (
                Nameoftablets VARCHAR(200),
                Reference_No VARCHAR(200) PRIMARY KEY,
                NumberofTablets VARCHAR(200),
                DailyDose VARCHAR(200),
                BloodPressure VARCHAR(200),
                VisitDate VARCHAR(200),
                ImpInstructions VARCHAR(200),
                SideEffect VARCHAR(200),
                FurtherInformation VARCHAR(200),
                DoctorsName VARCHAR(200),
                RegistrationNo VARCHAR(200),
                Qualification VARCHAR(200),
                PatientId VARCHAR(200),
                PatientName VARCHAR(200),
                PatientAddress VARCHAR(200),
                DOB VARCHAR(200),
                PatientContact VARCHAR(200)
            )
            """
            cursor.execute(create_table_query)
            print("Table 'hospital' created successfully!")
            
            print("\n✓ Database setup complete!")
            print("You can now run the hospital.py application.")
            
    except Error as e:
        print(f"Error: {e}")
        print("\nPlease make sure:")
        print("1. MySQL server is running")
        print("2. You've updated the password in this script")
        print("3. You have proper permissions")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    print("=" * 50)
    print("Hospital Management System - Database Setup")
    print("=" * 50)
    print("\nIMPORTANT: Update the password in this script before running!")
    print("Line 12: password='your_password'\n")
    
    response = input("Have you updated the password? (yes/no): ")
    if response.lower() == 'yes':
        create_database()
    else:
        print("\nPlease update the password and run this script again.")
