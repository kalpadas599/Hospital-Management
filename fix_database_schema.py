# Fix Database Schema Script for Hospital Management System

import mysql.connector
from mysql.connector import Error

def fix_database():
    """Drop and recreate the hospital table with correct schema"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',  # Change this to your MySQL password
            database='kdastestdb'
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            print("Fixing database schema...")
            
            # Drop existing table if it exists
            cursor.execute("DROP TABLE IF EXISTS hospital")
            print("✓ Dropped old table")
            
            # Create table with correct schema (all VARCHAR)
            create_table_query = """
            CREATE TABLE hospital (
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
            print("✓ Created new table with correct schema")
            
            connection.commit()
            print("\n✅ Database schema fixed successfully!")
            print("You can now run the hospital.py application.")
            
    except Error as e:
        print(f"❌ Error: {e}")
        print("\nPlease make sure:")
        print("1. MySQL server is running")
        print("2. You've updated the password in this script")
        print("3. Database 'kdastestdb' exists")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    print("=" * 60)
    print("Hospital Management System - Database Schema Fix")
    print("=" * 60)
    print("\n⚠️  WARNING: This will delete all existing data!")
    print("IMPORTANT: Update the password in this script before running!")
    print("Line 13: password='your_password'\n")
    
    response = input("Have you updated the password? (yes/no): ")
    if response.lower() == 'yes':
        confirm = input("This will delete all data. Continue? (yes/no): ")
        if confirm.lower() == 'yes':
            fix_database()
        else:
            print("\nOperation cancelled.")
    else:
        print("\nPlease update the password and run this script again.")
