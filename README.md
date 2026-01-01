# Hospital Management System - Setup Guide

## 🚨 CRITICAL: Fix Database Schema First!

If you're seeing errors like "Incorrect integer value" or "IndexError: string index out of range", your database table has the wrong schema.

### Quick Fix:
1. Open `fix_database_schema.py`
2. Update line 13 with your MySQL password
3. Run: `python fix_database_schema.py`
4. Restart the application

**⚠️ This will delete existing data in the table!**

---

## 🔧 Database Setup

### Prerequisites
- MySQL Server installed and running
- Python 3.x installed
- Required Python packages: `tkinter`, `mysql-connector-python`

### Step 1: Install Dependencies
```bash
pip install mysql-connector-python
```

### Step 2: Configure Database Password
1. Open `setup_database.py`
2. Update line 12 with your MySQL password:
   ```python
   password='your_actual_password'
   ```
3. Also update the password in `hospital.py` (appears in multiple functions)

### Step 3: Run Database Setup
```bash
python setup_database.py
```

This will create:
- Database: `kdastestdb`
- Table: `hospital` with all required columns

### Step 4: Run the Application
```bash
python hospital.py
```

## 🎨 What's New

### Fixed Issues ✅
- **"Prescription Data" button now works** - Previously had no command binding
- **Update function now commits changes** - Data updates are now saved to database
- **Error handling added** - Better error messages for database issues
- **All database operations wrapped in try-except blocks**

### UI Improvements ✨
- **Modern color scheme**:
  - Prescription: Blue (#3498DB)
  - Prescription Data: Green (#27AE60)
  - Update: Orange (#F39C12)
  - Delete: Red (#E74C3C)
  - Clear: Gray (#95A5A6)
  - Exit: Dark Gray (#34495E)
- **Professional dark header** (#2C3E50 with white text)
- **Hand cursor on buttons** for better UX

## 📝 How to Use

1. **Add Patient Record**:
   - Fill in all patient and prescription details
   - Click "Prescription Data" button to save to database
   - Data will appear in the table below

2. **View Prescription**:
   - Fill in the details
   - Click "Prescription" to display in the right panel

3. **Update Record**:
   - Click on a record in the table to load it
   - Modify the details
   - Click "Update" to save changes

4. **Delete Record**:
   - Click on a record in the table
   - Click "Delete" to remove it

5. **Clear Form**:
   - Click "Clear" to reset all fields

## ⚠️ Troubleshooting

### "Database Error" message appears
- Check if MySQL server is running
- Verify your password is correct in both files
- Ensure database and table are created (run setup_database.py)

### Data not saving
- Make sure you filled in at least "Names Of Tablet" and "Reference No"
- Check for duplicate Reference Numbers (must be unique)

### Application won't start
- Install required packages: `pip install mysql-connector-python`
- Check Python version (3.x required)
