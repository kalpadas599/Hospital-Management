# 💊 MediScript Pro - Medical Prescription Management System

> A Python-based desktop application for managing medical prescriptions with database persistence and PDF export capabilities.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)](https://www.mysql.com/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Table of Contents
- [About the Project](#about-the-project)
- [Problem Statement](#problem-statement)
- [Who Benefits](#who-benefits)
- [Features](#features)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Challenges Faced](#challenges-faced)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 About the Project

**MediScript Pro** is a comprehensive prescription management system designed to streamline the process of creating, storing, and sharing medical prescriptions. Built with Python and MySQL, it provides doctors and medical practitioners with an intuitive interface to manage patient prescriptions efficiently.

Unlike full-scale Hospital Management Systems, MediScript Pro focuses specifically on **prescription workflows**, making it lightweight, fast, and easy to use for clinics and small medical practices.

---

## 🔍 Problem Statement

Medical practitioners face several challenges in prescription management:

1. **Manual Record Keeping**: Paper-based prescriptions are prone to loss and difficult to retrieve
2. **Data Inconsistency**: Handwritten prescriptions can be illegible and lead to medication errors
3. **Lack of Digital Backup**: No centralized system to store and retrieve historical prescription data
4. **Sharing Difficulties**: Hard to share prescriptions with patients digitally
5. **Data Entry Errors**: Misalignment between form fields and database storage causing incorrect data mapping

**MediScript Pro solves these problems** by providing a digital, database-backed system with proper data validation, PDF export, and intuitive data management.

---

## 👥 Who Benefits

- **🩺 Doctors & Medical Practitioners**: Quickly create and manage prescriptions
- **🏥 Small Clinics**: Affordable prescription management without complex HMS
- **👨‍⚕️ Medical Students**: Learn database-backed application development
- **👴 Patients & Relatives**: Receive professional, shareable PDF prescriptions
- **📊 Medical Records Departments**: Maintain digital prescription archives

---

## ✨ Features

### Core Functionality
- ✅ **Create Prescriptions**: Intuitive form for patient and medication details
- ✅ **Database Storage**: Persistent MySQL storage with 17-column schema
- ✅ **CRUD Operations**: Create, Read, Update, Delete prescription records
- ✅ **PDF Export**: Generate professional prescription PDFs for sharing
- ✅ **Data Validation**: Error handling and input validation
- ✅ **Dynamic Tablet Names**: Editable medication field (not limited to dropdown)

### Technical Features
- 🔧 **Proper Data Mapping**: Fixed variable-to-database column alignment
- 🎨 **Modern UI**: Color-coded buttons with professional styling
- 📊 **Table View**: Scrollable data grid with all 17 columns
- 🔒 **Error Handling**: Comprehensive try-catch blocks for database operations
- 💾 **Auto-naming**: PDF files named with patient name and timestamp

---

## 📸 Screenshots

### Main Application Interface
<img width="1902" height="969" alt="Image" src="https://github.com/user-attachments/assets/611b71bd-52b9-4706-8c73-ca1704357b5f" />

### PDF Prescription Report

*See PDF prescription report named Prescription_STEVE...*

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Tkinter** | GUI framework for desktop interface |
| **MySQL** | Relational database for data persistence |
| **mysql-connector-python** | Python-MySQL database connector |
| **ReportLab** | PDF generation library |

---

## 📦 Installation

### Prerequisites
- Python 3.x installed
- MySQL Server running
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/mediScript-pro.git
cd mediScript-pro
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure Database
1. Open `setup_database.py`, `fix_database_schema.py`, and `hospital.py`
2. Update MySQL password on line 13 (or wherever `password='your_password'` appears):
   ```python
   password = "your_actual_mysql_password"
   ```

### Step 4: Initialize Database
```bash
python setup_database.py
```

This creates:
- Database: `kdastestdb`
- Table: `hospital` (17 columns with proper schema)

### Step 5: Run the Application
```bash
python hospital.py
```

---

## 🚀 Usage

### Adding a Prescription
1. Fill in patient details (Name, ID, DOB, Address, Contact)
2. Enter medication information (Tablets, dosage, blood pressure, etc.)
3. Add doctor information (Name, Registration No, Qualification)
4. Click **"Prescription Data"** to save to database

### Viewing Prescription
1. Fill in the form
2. Click **"Prescription"** to display in the text area

### Updating a Record
1. Click on a row in the data table
2. Modify the details in the form
3. Click **"Update"**

### Deleting a Record
1. Select a row from the table
2. Click **"Delete"**

### Downloading PDF
1. Fill in prescription details
2. Click **"Download PDF"**
3. Choose save location
4. Share the PDF with patient/relatives

---

## 🧗 Challenges Faced

### Challenge: Data Mapping Misalignment

**Problem**: The most critical challenge was incorrect data mapping between UI form fields and database columns. For example:
- "Patient Name" field was bound to `nhsNumber` variable
- "Patient Address" field was bound to `PatientName` variable
- This caused data to be stored in completely wrong columns

**Impact**: 
- Patient names appeared in contact number columns
- Addresses appeared in name columns
- Data retrieval was completely incorrect

**Solution**:
1. Identified all variable-to-field mismatches
2. Corrected Entry widget `textvariable` bindings
3. Updated INSERT/UPDATE SQL queries to match correct order
4. Fixed `get_cursor()` function to load data into correct variables
5. Renamed database columns to meaningful names (e.g., `dose` → `NumberofTablets`)

**Result**: All 17 fields now map correctly from UI → Database → Display

---

## 🔮 Future Improvements

1. **🔐 User Authentication**: Add login system for multiple doctors
2. **📊 Analytics Dashboard**: Prescription statistics and patient history graphs
3. **🔍 Advanced Search**: Filter prescriptions by date, patient, medication
4. **☁️ Cloud Backup**: Automatic cloud synchronization for data safety
5. **📱 Mobile App**: React Native companion app for on-the-go access
6. **🖨️ Direct Printing**: Print prescriptions without PDF intermediate step
7. **📧 Email Integration**: Send PDFs directly to patient email
8. **🌐 Multi-language Support**: Support for regional languages
9. **💊 Drug Database**: Integration with medication database for auto-suggestions
10. **📅 Appointment Integration**: Link prescriptions with appointment scheduling

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Kalpa Das**
- GitHub: [@kalpadas599](https://github.com/kalpadas599)
- Project: Academic Project

---

## 🙏 Acknowledgments

- Python Tkinter Documentation
- MySQL Community
- ReportLab Library Contributors
- Stack Overflow Community

---

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Email: kalpadas599@gmail.com

---

<div align="center">
Made with ❤️ for better healthcare management
</div>

