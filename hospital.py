from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management Information")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffects=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.Howtousemedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,fg="white",bg="#2C3E50",font=("times new roman",50,"bold"),text="HOSPITAL MANAGEMENT INFORMATION")
        lbltitle.pack(side=TOP,fill=X)


        # =========DataFrame=================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)


        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                        font=("times new roman",12,"bold"),text="Patient & Doctor Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                        font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)


        # =============Buttons Frame===================     
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)


        # =============Details Frame===================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)


        #==============DataFrameLeft======================
        lblNameTablet=Label(DataframeLeft,text="Names Of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        txtNameTablet=Entry(DataframeLeft,textvariable=self.Nameoftablets,font=("arial",13,"bold"),width=35)
        txtNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="No of tablets:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNooftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Visit Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Imp Instructions:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffects,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Doctor's Name:",padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        #lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure",padx=2,pady=6)
        #lblBloodPressure.grid(row=1,column=2,sticky=W)
        #txtBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)#ekhane driving dekhacche
        #txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Registration No:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Qualification:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Contact:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtPatientAddress.grid(row=8,column=3)


        #===================DataFrameRight===========================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
     

        #=====================Buttons=======================
        btnPrescription=Button(Buttonframe,command=self.iPrescription,font=("arial",12,"bold"),text="Prescription",bg="#3498DB",fg="white",width=23,padx=2,pady=6,cursor="hand2")
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="#27AE60",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnPrescriptionData.grid(row=0,column=1)

        btnDownloadPDF=Button(Buttonframe,command=self.download_prescription_pdf,text="Download PDF",bg="#9B59B6",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnDownloadPDF.grid(row=0,column=2)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="#F39C12",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnUpdate.grid(row=0,column=3)

        btnDelete=Button(Buttonframe,command=self.idelete,text="Delete",bg="#E74C3C",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnDelete.grid(row=0,column=4)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="#95A5A6",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnClear.grid(row=0,column=5)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="#34495E",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6,cursor="hand2")
        btnExit.grid(row=0,column=6)



        #======================Table=============================
        #=========================ScrollBar===============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","numberoftablets","dailydose","bloodpressure","visitdate",
                                    "impinstructions","sideeffect","furtherinfo","doctorsname","registrationno","qualification","patientid","patientname","patientaddress","dob","patientcontact"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name Of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("numberoftablets",text="Number Of Tablets")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("bloodpressure",text="Blood Pressure")
        self.hospital_table.heading("visitdate",text="Visit Date")
        self.hospital_table.heading("impinstructions",text="Imp Instructions")
        self.hospital_table.heading("sideeffect",text="Side Effect")
        self.hospital_table.heading("furtherinfo",text="Further Info")
        self.hospital_table.heading("doctorsname",text="Doctor's Name")
        self.hospital_table.heading("registrationno",text="Registration No")
        self.hospital_table.heading("qualification",text="Qualification")
        self.hospital_table.heading("patientid",text="Patient ID")
        self.hospital_table.heading("patientname",text="Patient Name")
        self.hospital_table.heading("patientaddress",text="Patient Address")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("patientcontact",text="Patient Contact")

        self.hospital_table["show"]="headings"
       

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("numberoftablets",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("bloodpressure",width=100)
        self.hospital_table.column("visitdate",width=100)
        self.hospital_table.column("impinstructions",width=100)
        self.hospital_table.column("sideeffect",width=100)
        self.hospital_table.column("furtherinfo",width=100)
        self.hospital_table.column("doctorsname",width=100)
        self.hospital_table.column("registrationno",width=100)
        self.hospital_table.column("qualification",width=100)
        self.hospital_table.column("patientid",width=100)
        self.hospital_table.column("patientname",width=100)
        self.hospital_table.column("patientaddress",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("patientcontact",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    #==================Fuunctionally Declaration==================
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="your_password",database="kdastestdb")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                    self.Nameoftablets.get(),
                                                                                                    self.ref.get(),
                                                                                                    self.Dose.get(),
                                                                                                    self.NumberofTablets.get(),
                                                                                                    self.Lot.get(),
                                                                                                    self.Issuedate.get(),
                                                                                                    self.ExpDate.get(),
                                                                                                    self.DailyDose.get(),
                                                                                                    self.sideEffects.get(),
                                                                                                    self.FurtherInformation.get(),
                                                                                                    self.StorageAdvice.get(),
                                                                                                    self.DrivingUsingMachine.get(),
                                                                                                    self.PatientId.get(),
                                                                                                    self.PatientName.get(),
                                                                                                    self.PatientAddress.get(),
                                                                                                    self.DateOfBirth.get(),
                                                                                                    self.nhsNumber.get()

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Record has been inserted.")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error",f"Error: {err}")



    def update_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="your_password",database="kdastestdb")
            my_cursor=conn.cursor()
            my_cursor.execute("update hospital set Nameoftablets=%s,NumberofTablets=%s,DailyDose=%s,BloodPressure=%s,VisitDate=%s,ImpInstructions=%s,SideEffect=%s,FurtherInformation=%s,DoctorsName=%s,RegistrationNo=%s,Qualification=%s,PatientId=%s,PatientName=%s,PatientAddress=%s,DOB=%s,PatientContact=%s where Reference_No=%s",(

                                                                                                                    self.Nameoftablets.get(),
                                                                                                                    self.Dose.get(),
                                                                                                                    self.NumberofTablets.get(),
                                                                                                                    self.Lot.get(),
                                                                                                                    self.Issuedate.get(),
                                                                                                                    self.ExpDate.get(),
                                                                                                                    self.DailyDose.get(),
                                                                                                                    self.sideEffects.get(),
                                                                                                                    self.FurtherInformation.get(),
                                                                                                                    self.StorageAdvice.get(),
                                                                                                                    self.DrivingUsingMachine.get(),
                                                                                                                    self.PatientId.get(),
                                                                                                                    self.PatientName.get(),
                                                                                                                    self.PatientAddress.get(),
                                                                                                                    self.DateOfBirth.get(),
                                                                                                                    self.nhsNumber.get(),
                                                                                                                    self.ref.get()

                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been updated successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error",f"Error: {err}")


    def fetch_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="your_password",database="kdastestdb")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from hospital")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                for item in self.hospital_table.get_children():
                    self.hospital_table.delete(item)
                for i in rows:
                    self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error",f"Error: {err}\n\nPlease check your database connection and credentials.")


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        
        # Check if row has data before accessing
        if row and len(row) >= 17:
            self.Nameoftablets.set(row[0])      
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.Issuedate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.sideEffects.set(row[8])
            self.FurtherInformation.set(row[9])
            self.StorageAdvice.set(row[10])
            self.DrivingUsingMachine.set(row[11])
            self.PatientId.set(row[12])
            self.PatientName.set(row[13])
            self.PatientAddress.set(row[14])
            self.DateOfBirth.set(row[15])
            self.nhsNumber.set(row[16])


    def iPrescription(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Blood Pressure:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Visit Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Imp Instructions:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.sideEffects.get()+"\n")
        self.txtPrescription.insert(END,"Doctor's Name:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Registration No:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"Qualification:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Contact:\t\t\t"+self.nhsNumber.get()+"\n")

        
    def idelete(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="your_password",database="kdastestdb")
            my_cursor=conn.cursor()
            query="delete from hospital where Reference_No=%s"
            value=(self.ref.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Delete","Patient has been deleted successfully.")
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error",f"Error: {err}")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffects.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.Howtousemedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)



    def download_prescription_pdf(self):
        """Generate and download prescription as PDF"""
        try:
            # Check if prescription data exists
            if not self.ref.get():
                messagebox.showerror("Error", "Please fill in the prescription details first!")
                return
            
            # Ask user where to save the file
            patient_name = self.PatientName.get() if self.PatientName.get() else "Patient"
            default_filename = f"Prescription_{patient_name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile=default_filename
            )
            
            if not filename:
                return  # User cancelled
            
            # Create PDF
            doc = SimpleDocTemplate(filename, pagesize=letter)
            story = []
            styles = getSampleStyleSheet()
            
            # Custom styles
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#2C3E50'),
                spaceAfter=30,
                alignment=TA_CENTER
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                textColor=colors.HexColor('#34495E'),
                spaceAfter=12,
                spaceBefore=12
            )
            
            # Title
            title = Paragraph("MEDICAL PRESCRIPTION", title_style)
            story.append(title)
            story.append(Spacer(1, 0.2*inch))
            
            # Date and Reference
            date_text = f"Date: {datetime.datetime.now().strftime('%d-%m-%Y')}<br/>Reference No: {self.ref.get()}"
            story.append(Paragraph(date_text, styles['Normal']))
            story.append(Spacer(1, 0.3*inch))
            
            # Patient Information Section
            story.append(Paragraph("PATIENT INFORMATION", heading_style))
            patient_data = [
                ['Patient Name:', self.PatientName.get()],
                ['Patient ID:', self.PatientId.get()],
                ['Date of Birth:', self.DateOfBirth.get()],
                ['Address:', self.PatientAddress.get()],
                ['Contact:', self.nhsNumber.get()],
            ]
            
            patient_table = Table(patient_data, colWidths=[2*inch, 4*inch])
            patient_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ]))
            story.append(patient_table)
            story.append(Spacer(1, 0.3*inch))
            
            # Medication Information Section
            story.append(Paragraph("MEDICATION DETAILS", heading_style))
            medication_data = [
                ['Medication:', self.Nameoftablets.get()],
                ['Number of Tablets:', self.Dose.get()],
                ['Daily Dose:', self.NumberofTablets.get()],
                ['Blood Pressure:', self.Lot.get()],
                ['Visit Date:', self.Issuedate.get()],
                ['Important Instructions:', self.ExpDate.get()],
                ['Side Effects:', self.DailyDose.get()],
                ['Further Information:', self.sideEffects.get()],
            ]
            
            medication_table = Table(medication_data, colWidths=[2*inch, 4*inch])
            medication_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ]))
            story.append(medication_table)
            story.append(Spacer(1, 0.3*inch))
            
            # Doctor Information Section
            story.append(Paragraph("DOCTOR INFORMATION", heading_style))
            doctor_data = [
                ["Doctor's Name:", self.FurtherInformation.get()],
                ['Registration No:', self.StorageAdvice.get()],
                ['Qualification:', self.DrivingUsingMachine.get()],
            ]
            
            doctor_table = Table(doctor_data, colWidths=[2*inch, 4*inch])
            doctor_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ECF0F1')),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('TOPPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ]))
            story.append(doctor_table)
            story.append(Spacer(1, 0.5*inch))
            
            # Footer
            footer_text = "<i>This is a computer-generated prescription. Please consult your doctor for any queries.</i>"
            story.append(Paragraph(footer_text, styles['Normal']))
            
            # Build PDF
            doc.build(story)
            
            messagebox.showinfo("Success", f"Prescription PDF saved successfully!\n\nLocation: {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {str(e)}")


    def iExit(self):
        iExit=messagebox.askyesno("Hospital menagement system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


root=Tk()
ob=Hospital(root)
root.mainloop()








