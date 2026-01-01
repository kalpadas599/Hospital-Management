# Rename Database Columns Script

import mysql.connector
from mysql.connector import Error

def rename_columns():
    """Rename database columns to match actual field meanings"""
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
            
            print("Renaming database columns...")
            print("⚠️  This will recreate the table with new column names!")
            print()
            
            # Drop existing table
            cursor.execute("DROP TABLE IF EXISTS hospital")
            print("✓ Dropped old table")
            
            # Create table with correct column names
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
            print("✓ Created new table with renamed columns")
            
            connection.commit()
            print("\n✅ Database columns renamed successfully!")
            print("\nNew column names (17 total):")
            print("  1. Nameoftablets")
            print("  2. Reference_No")
            print("  3. NumberofTablets (was: dose)")
            print("  4. DailyDose (was: Numbersoftablets)")
            print("  5. BloodPressure (was: lot)")
            print("  6. VisitDate (was: issuedate)")
            print("  7. ImpInstructions (was: expdate)")
            print("  8. SideEffect (was: dailydose)")
            print("  9. FurtherInformation (NEW)")
            print(" 10. DoctorsName (NEW)")
            print(" 11. RegistrationNo (was: storage)")
            print(" 12. Qualification (NEW)")
            print(" 13. PatientId (NEW)")
            print(" 14. PatientName (was: nhsnumber)")
            print(" 15. PatientAddress (was: patientname)")
            print(" 16. DOB")
            print(" 17. PatientContact (was: patientaddress)")
            
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
    print("Hospital Management System - Rename Database Columns")
    print("=" * 60)
    print("\n⚠️  WARNING: This will delete all existing data!")
    print("IMPORTANT: Update the password in this script before running!")
    print("Line 11: password='your_password'\n")
    
    response = input("Have you updated the password? (yes/no): ")
    if response.lower() == 'yes':
        confirm = input("This will delete all data. Continue? (yes/no): ")
        if confirm.lower() == 'yes':
            rename_columns()
        else:
            print("\nOperation cancelled.")
    else:
        print("\nPlease update the password and run this script again.")
