import mysql.connector

# Connect to MySQL server and the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7224",
    charset="utf8"
)

if mydb.is_connected():
    print("Connection Established")
else:
    print("Connection Errors! Kindly check!!!")
mycursor=mydb.cursor()



def data_base():
    try:
        mycursor.execute("create database emp_manage")
        print("Database Created Successfully")
    except Exception as e:
        print("Database Error!!!,You have given error -- ",e)
        print("Please try again")
        data_base()

#department table
def dept_table():
    try:
        mycursor.execute("use emp_manage")
        mycursor.execute('''create table emp_dept
                        (dept_id varchar(5) primary key,
                        dept_name varchar(20),
                        dept_catgry varchar(20)
                        );
                        ''')
        print("Department table successfully created.")
    except Exception as e:
        print("Database Error",e)
        print("Please try again")
        dept_table()

def dept_data():
    try:
        mycursor.execute("use emp_manage")
        mycursor.execute("insert into emp_dept values ('D001','Admin','Non-teaching');")
        mycursor.execute("insert into emp_dept values ('D002','Medical','Non-teaching');")
        mycursor.execute("insert into emp_dept values ('D003','Social Science','Teaching');")
        mycursor.execute("insert into emp_dept values ('D004','Maths','Teaching');")
        mycursor.execute("insert into emp_dept values ('D005','English','Teaching');")
        mycursor.execute("insert into emp_dept values ('D006','Hindi','Teaching');")
        mycursor.execute("insert into emp_dept values ('D007','Science','Teaching');")
        mydb.commit()

    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
    

#salary table
def sal_table():
    try:
        mycursor.execute("use emp_manage")
        mycursor.execute('''create table salary(Grade varchar(1) primary key,bas_sal int(6));''')
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")


      
def sal_data():
    mycursor.execute("use emp_manage")
    mycursor.execute("insert into salary values ('A',55000);")
    mycursor.execute("insert into salary values ('B',45000);")
    mycursor.execute("insert into salary values ('C',35000);")
    mycursor.execute("insert into salary values ('D',20000);")
    mydb.commit()

    



                
#employee table
def empinfo_table():
    mycursor.execute("use emp_manage")
    mycursor.execute('''create table emp_info(
                        Emp_Id varchar(5) primary key,
                        First_Name varchar(10),
                        Last_Name varchar(10),
                        Father_Spouse_Name varchar(20),
                        Date_of_Birth Date ,
                        GraduateUG_PG varchar(2),
                        dept_id varchar(5),
                        RegularY_N varchar(1),
                        Designation varchar(15),
                        email varchar(30),
                        contact_num BIGINT(10),
                        Joining_Date date,
                        Aadhar_num BIGINT(12),
                        Address varchar(50),
                        Grade varchar(1),
                        foreign key(dept_id) references emp_dept(dept_id),
                        foreign key(Grade) references salary(Grade));''')
    mydb.commit()







def empinfo_data():
    mycursor.execute("use emp_manage")
    mycursor.execute('''insert into emp_info values ("E001"," Aakash"," Gupta", "Ram Charan","1995-04-08", "PG", "D002", "Y", "Manager", "akg.gupta@gmail.com",8657474809, "2020-10-10",234556678976,"Suraincha_Sidhauli_Sitapur","A");''')
    mycursor.execute('''insert into emp_info values ("E002", "Aditya", "Tripathi", "SambhuSaran","1996-05-07", "UG", "D004", "Y", "Engineer","tripathiad2@gmail.com", 2387201735, "2019-01-03", 271917291629, "Rampur_Bareily","B");''')
    mycursor.execute('''insert into emp_info values ("E003", "Abhishek", "Tripathi", " Manoj","1997-05-07", "UG", "D001", "N","Engineer","abtripathi276@gmail.com",7820162052, "2010-01-01", 2816209172017," Reoli_LarRoad_Deoria","C");''')
    mycursor.execute('''insert into emp_info values ("E004", "Vikas", "Dubey", "Akhandanand","1998-04-03", "PG", "D003", "Y" , "Manager","dubeyvikas@gmail.com", 2386472928, "2019-03-19", 282926282528, "Fulera_Baliya","D");''')
    mydb.commit()


# emp_info_deleted table.   
def emp_info_deleted():
    mycursor.execute("use emp_manage")
    mycursor.execute('''create table emp_infodeleted(
                        Emp_Id varchar(5) primary key,
                        First_Name varchar(10),
                        Last_Name varchar(10),
                        Father_Spouse_Name varchar(20),
                        Date_of_Birth Date ,
                        GraduateUG_PG varchar(2),
                        dept_id varchar(5),

                        RegularY_N varchar(1),
                        Designation varchar(15),
                        email varchar(30),
                        contact_num BIGINT(10),
                        Joining_Date date,
                        Aadhar_num BIGINT(12),
                        Address varchar(50),
                        Grade varchar(1),
                        foreign key(dept_id) references emp_dept(dept_id),
                        foreign key(Grade) references salary(Grade));''')
    mydb.commit()



#1.)	Main employment management Programming. 
#Adding of New Employee
def ADD_EMP():
    b=1
    while b==1:
        print("{:>60}".format("-->> Add Employee Record <<--"))
        mycursor.execute("use emp_manage")
        mycursor.execute("SELECT * FROM emp_info;")
        data = mycursor.fetchall()
        count = mycursor.rowcount
        mycursor.execute("SELECT * FROM emp_infodeleted;")
        r = mycursor.fetchall()
        count1 = mycursor.rowcount
        Emp_id = "E00"+str(count+count1+1)

        first_name = input("Enter the fist name of new employee ")
        last_name = input("Enter the last name of new employee ")
        Father_Spouse_Name = input("Enter name of father or spouse  new employee ")

        Date_of_Birth = input("Enter Date of Birth of new employee(YYYY-MM-DD) ")
        GradauteUG_PG = input("Enter either UG or PG  new employee ")
        Department = input("Enter Employee's department name( like Medical, Admin ,Social Science, Maths ) ")
        mycursor.execute("SELECT * from emp_dept where dept_name = '{}'". format(Department))     
        data1 = mycursor.fetchone()
        if data1 is None:
            print("Error: Department '{}' not found in the 'emp_dept' table.".format(Department))
            return  # Exit the function or handle the error accordingly
        else:
            dept_id = data1[0]
        contact_num = int(input("Enter Employee's 10 digit contact number "))
        Joining_Date = input("Enter Employee's joining date(YYYY-MM-DD) ")
        Aadhar_num = int(input("Enter Employee's aadhar number "))
        Address = input("Enter Employee's address ")
        designation = input("Enter Employee's designation ")
        def emailValid():
            import re
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            email = input("Enter Employee's email ")
            if re.fullmatch(regex, email):
                return email
            else:
                print("You have entered a wrong format")
                print("Please try again")
                return emailValid()
        email = emailValid()
        regular = input("Is employee regular? (Y/N) ")
        grade = input("Enter Employee's grade ")


        # Define the SQL query and the values to be inserted
        query = '''INSERT INTO emp_info 
                   (Emp_id, first_name, last_name, Father_Spouse_Name, Date_of_Birth, 
                   GradauteUG_PG, dept_id, regular, designation, email, contact_num, 
                   Joining_Date, Aadhar_num, Address, grade)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        values = (Emp_id, first_name, last_name, Father_Spouse_Name, Date_of_Birth, 
                  GradauteUG_PG, dept_id, regular, designation, email, contact_num, 
                  Joining_Date, Aadhar_num, Address, grade)
        
        # Execute the query
        mycursor.execute(query, values)
        mydb.commit()
        choice = input("Do you want to add more employee (y/n)")  
        if choice in "Yy":
            b=1
        else:
            b=2
    press = input("Press Any key To Continue..")   
    maindata()

 #Display All Employee Records
def DIS_EMP():
    try:
        print("{:>60}".format("-->> Display Employee Record <<--"))
        mycursor.execute("use emp_manage")
        mycursor.execute("SELECT * FROM emp_info;")
        r = mycursor.fetchall()

        count = mycursor.rowcount
        print()
        print("\t\t\t\t\t","Total Records fetched",count)
        z=1
    

        for i in r:
            print("RECORD NO.",z)
            print("\n")
            print("Employee Id: ", i[0])
            print("Employee First Name: ", i[1])
            print("Employee Last Name: ", i[2])
            print("Employee  Father_Spouse_Name: ", i[3])
            print("Employee Date_of_Birth : ", i[4])
            print("Employee GraduateUG_PG : ", i[5])
            print("Employee dept_id : ", i[6])
            print("Employee RegularY_N: ", i[7])
            print("Employee Designation: ", i[8])
            print("Employee email: ", i[9])
            print("Employee contact_num: ", i[10])
            print("Employee Joining_Date: ", i[11])
            print("Employee Aadhar_num: ", i[12])
            print("Employee Address: ", i[13])
            print("Employee Grade: ", i[14])
            print("\n")
            z+=1
        press = input("Press Any key To Continue..")   

        maindata()   
      
    except Exception as e:
        print("Database Eroor",e)
        print("Please try again")
        DIS_EMP()

    maindata()

# Search and Display by Designation

def SEA_DESIG():
    try:
        print("{:>60}".format("-->> Display Employee Record <<--"))
        mycursor.execute("use emp_manage")
        desig = input("Enter designation by whom you want to search ")
        mycursor.execute("SELECT * FROM emp_info WHERE designation = '{}'". format(desig))
        s=mycursor.fetchall()
        count=mycursor.rowcount
        if count == 0:
             print("NO RECORD FOUND....")
             print("Please try again")
             maindata()
             
        else:
            ac=1

            for i in s:
                print("RECORD NO.",ac)
                print()
                print("Employee Id: ", i[0])
                print("Employee First Name: ", i[1])
                print("Employee Last Name: ", i[2])
                print("Employee  Father_Spouse_Name: ", i[3])

                print("Employee Date_of_Birth : ", i[4])
                print("Employee GraduateUG_PG : ", i[5])
                print("Employee dept_id : ", i[6])
                print("Employee RegularY_N: ", i[7])
                print("Employee Designation: ", i[8])
                print("Employee email: ", i[9])
                print("Employee contact_num: ", i[10])
                print("Employee Joining_Date: ", i[11])
                print("Employee Aadhar_num: ", i[12])
                print("Employee Address: ", i[13])
                print("Employee Grade: ", i[14])
                print("\n")
                ac+=1
                
             
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        SEA_DESIG()
        
    press = input("Press Any key To Continue..")
    maindata()
# Search and Display by Employee First Name
def SEA_NAME():
    try:
        print("{:>60}".format("-->> Display Employee Record <<--"))
        mycursor.execute("use emp_manage")

        name = input("Enter First name of employee  by whom you want to search ")
        mycursor.execute("SELECT * FROM emp_info WHERE First_name = '{}'". format(name))
        t=mycursor.fetchall()
        count=mycursor.rowcount
        if count == 0:
             print("NO RECORD FOUND....")
             print("Please try again")
             maindata()
        else:
            ab=1
            for i in t:
                print("RECORD NO.",ab)
                print("\n")
                print("Employee Id: ", i[0])
                print("Employee First Name: ", i[1])
                print("Employee Last Name: ", i[2])
                print("Employee  Father_Spouse_Name: ", i[3])
                print("Employee Date_of_Birth : ", i[4])

                print("Employee GraduateUG_PG : ", i[5])
                print("Employee dept_id : ", i[6])
                print("Employee RegularY_N: ", i[7])
                print("Employee Designation: ", i[8])
                print("Employee email: ", i[9])
                print("Employee contact_num: ", i[10])
                print("Employee Joining_Date: ", i[11])
                print("Employee Aadhar_num: ", i[12])

                print("Employee Address: ", i[13])
                print("Employee Grade: ", i[14])
                print("\n")
                ab+=1
                 
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        SEA_NAME()
    press = input("Press Any key To Continue..")
    maindata()

# Search and Display by Employee ID
def SEA_EMPID():
    try:
        print("{:>60}".format("-->> Display Employee Record <<--"))
        mycursor.execute("use emp_manage")
        emp_id = input("Enter emp_id of employee by whom you want to search ")

        mycursor.execute("SELECT * FROM emp_info WHERE Emp_id = '{}'". format(emp_id))
        u=mycursor.fetchall()
        count=mycursor.rowcount
        if count == 0:
             print("NO RECORD FOUND....")
             maindata()
        else:
             for i in u:
                 
                print("Employee Id: ", i[0])
                print("Employee First Name: ", i[1])
                print("Employee Last Name: ", i[2])
                print("Employee  Father_Spouse_Name: ", i[3])
                print("Employee Date_of_Birth : ", i[4])
                print("Employee GraduateUG_PG : ", i[5])
                print("Employee dept_id : ", i[6])
                print("Employee RegularY_N: ", i[7])
                print("Employee Designation: ", i[8])
                print("Employee email: ", i[9])
                print("Employee contact_num: ", i[10])
                print("Employee Joining_Date: ", i[11])
                print("Employee Aadhar_num: ", i[12])
                print("Employee Address: ", i[13])
                print("Employee Grade: ", i[14])
                print("\n")
                maindata()
                
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        SEA_EMPID()
    press = input("Press Any key To Continue..")
    maindata()
        



# Delete  Employee Record
def DEL_EMP():
    try:
        mycursor.execute("use emp_manage")
        emp_id = input("Enter emp_id of employee which you want to delete ")
        mycursor.execute("SELECT * FROM emp_info WHERE Emp_id = '{}'". format(emp_id))
        data=mycursor.fetchall()
        A=data[0]
        a=A[0]
        b=A[1]
        c=A[2]
        d=A[3]
        e=A[4]
        f=A[5]
        g=A[6]
        h=A[7]

        i=A[8]
        j=A[9]
        k=A[10]
        l=A[11]
        m=A[12]
        n=A[13]
        o=A[14]
        mycursor.execute('''insert into emp_infodeleted values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}')'''. 
                        format(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o))
        mydb.commit()

        mycursor.execute("DELETE FROM emp_info WHERE Emp_id ='{}'". format(emp_id))
        mydb.commit()
        print("DELETION SUCCESSFUL!!!")
        press = input("Press Any key To Continue..")
        maindata()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        DEL_EMP()
    press = input("Press Any key To Continue..")
    maindata()



# Modify Different details of Employee

def first_name():
    try:
        
        x = input("Enter the updated first name of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set First_Name = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")

            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        first_name()
    maindata()

   
def last_name():
    try:
        x = input("Enter the updated last name of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE  emp_info set last_name = '{}' where emp_id = '{}'". format(x,y))

        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            last_name()
            
    except Exception as e:

        print("Database Error:",e)
        print("Please try again")
        last_name()
    maindata()

def Father_Spouse_Name():
    try:
        x = input("Enter the updated father or spouse name of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set Father_Spouse_Name = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")

            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        Father_Spouse_Name()
    maindata()

def Date_of_Birth():
    try:

        x = input("Enter the updated date of birth of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE  emp_info set Date_of_Birth = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            Date_of_Birth()
    except Exception as e:

        print("Database Error:",e)
        print("Please try again")
        Date_of_Birth()
    maindata()

def GraduateUG_PG():
    try:
        x = input("Enter the updated Graduated UG or PG of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set GraduateUG_PG = '{}' where emp_id = '{}' ". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:

            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            GraduateUG_PG()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        GraduateUG_PG()
    maindata()


def regular():
    try:
        x = input("Enter the updated Regularity Y/N of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE  emp_info set RegularY_N = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")

            regular()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        regular()
    maindata()

   
   
def designation():
    try:
        x = input("Enter the updated designation of employee :")

        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set designation = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            designation()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")

        designation()
    maindata()


def email():
    try:
        def emailValid():
            import re
            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            x = input("Enter the updated email of employee :")
            if re.fullmatch(regex, x):

                return x
            else:
                print("You have entered a wrong format")
                print("Please try again")
                emailValid()
        x = emailValid()
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set email = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")

            print("Please try again")
            email()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        email()
    maindata()


def contact_num():

    try:
        x = input("Enter the updated contact number of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set contact_num = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            contact_num()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")

        contact_num()
    maindata()


def Joining_Date():
    try:
        x = input("Enter the updated joining date of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set Joining_Date = '{}' where emp_id = '{}'". format(x,y))

        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            Joining_Date()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        Joining_Date()
    maindata()
        
   


def Aadhar_num():
    try:
        x = input("Enter the updated aadhar number of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set Aadhar_num = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:

            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")
            print("Please try again")
            Aadhar_num
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        Aadhar_num()
    maindata()
   
   
def Address():
    try:
        x = input("Enter the updated address of employee :")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE emp_info set Address = '{}' where emp_id = '{}'". format(x,y))

        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            press = input("Press Any key To Continue..")
        else:
            print("Such Employee",y,"does not exist...")

            print("Please try again")
            Address()
    except Exception as e:
        print("Database Error:",e)
        print("Please try again")
        Address()
    maindata()
   

def MOD_EMP():
    try:
        mycursor.execute("use emp_manage")
        emp_id = input("Enter emp_id of employee which you want to modify ")
        print()
        print("1.first_name","2.last_name","3.Father_Spouse_Name","4.Date_of_Birth","5.GradauteUG_PG",
                      "6.regular","7.designation","8.email","9.contact_num","10.Joining_Date","11.Aadhar_num", "12.Address",sep="\n")
        x=int(input("Choose the number which you to modify "))
        
    except Exception as e:
        print("Database Error:",e)
        MOD_EMP()
        
    global y
    y = emp_id
    

    if x == 1:
        first_name()
    if x == 2:
        last_name()
    if x == 3:
        Father_Spouse_Name()
    if x == 4:
        Date_of_Birth()
    if x == 5:
        GraduateUG_PG()
    if x == 6:
        regular()
    if x == 7:
        designation()
    if x == 8:
        email()
    if x == 9:
        contact_num()
    if x == 10:

        Joining_Date()
    if x == 11:
        Aadhar_num()
    if x == 12:
        Address()
    else:

        print("Please enter a valid choice")
        MOD_EMP()
    maindata()

# Promote an Employee
def Promote_Emp():
    print("{:>60}".format("-->> Promote Employee Record <<--\n"))
    try:
        y =input("Enter emp_id of employee which you want to modify ")
        x = input("Enter the updated grade of employee : ")
        mycursor.execute("use emp_manage")
        mycursor.execute("UPDATE  emp_info set Grade = '{}' where emp_id = '{}'". format(x,y))
        mydb.commit()
        count=mycursor.rowcount
        if count ==1:
            print("Record Updated Successfully")
            print("Employee Promoted")
            press = input("Press Any key To Continue..")
        else:
            print("Such an employee doess't exist.Please try again.")

            Promote_Emp()

        maindata()
    except Exception as e:
        print("Database Error:",e)

        print("Please try again")
        Promote_Emp()

    maindata()
    
        
  # Generate Salary Slip of an Employee 
def SAL_SLIP():
    try:
        mycursor.execute("use emp_manage")
        emp_id = input("Enter emp_id of employee whom salary slip you want to display ")
        mycursor.execute("SELECT * FROM emp_info where emp_id = '{}'". format(emp_id))
        data = mycursor.fetchone()
        count = mycursor.rowcount
        grade=data[14]
        count = mycursor.rowcount
        if count == 0:
             print("NO RECORD FOUND....")
        mycursor.execute("SELECT bas_sal FROM salary where grade='{}' ". format(grade))
        data1 = mycursor.fetchone()
        l=float(data1[0])

        count1 = mycursor.rowcount
        if count1 == -1:
             print("NO RECORD FOUND....")
        month=input("Please enter the month's name ")

        HRA=int(input("Please enter the House Rent Allowance % on basic salary "))
        HRA=float(HRA/100)
        CA=int(input("Please enter the Conveyance Allowance % on basic salary "))
        CA=float(CA/100)
        print("==="*52)
        print("*"*50, "RAMAYAN ENTERPRISES","*"*50)
        print()
        print("\t\t\t\t\t\t","JAN KALYAN BANK")
        print("\t\t\t\t\t", "Payslip for the month of " + month + " 2022")
        print("==="*52)
        print()
        print("==="*52)
        print("Emp_Id       :  ",data[0],"\t\t",  "|  First_Name  :  ",data[1],"\t\t",           "      |  Last_Name           :  ",data[2] )
        print("DOB          :  ", data[4],"\t",   "|  Grade       :  ", data[14],"\t\t\t",       "      |  Father_Spouse_Name  :  ",data[3])
        print("Graduation   :  ", data[5],"\t\t", "|  Dept_Id     :  ", data[6],"\t\t",          "      |  Regular             :  ",data[7])
        print("Designation  :  ", data[8],"\t\t",   "|  Contact_num :  ",data[10], "\t\t",              "      |  Email       :  ", data[9])
        
        print("==="*52)
        print()
        print("==="*52)

        print(" "*5, "EARNINGS", "\t\t\t", "Monthly Rate","\t\t\t","DEDUCTIONS","\t\t\t","Total")
        print(" "*5, "Basic",    " \t\t\t",l,"\t\t\t",      "Profession Tax ","\t\t",l*0.01)


        print(" "*5,"Conveyance Allowance"," \t",round(l*CA,2),"\t\t\t","Income Tax     ","\t\t",round(l*0.01,2))
        print(" "*5,"House Rent Allowance"," \t",round(l*HRA,2),"\t\t\t","Provident Fund ","\t\t",round(l*0.12,2))
        print(" "*5,"Fixed Allowance     "," \t",float(3750))
        print(" "*5,"Medical","\t\t\t",float(1250))
        print("\n")
        ge=l+l*CA+l*HRA+3750+1250
        ded=l*0.01+l*0.01+l*0.12
        print("\t\t\t","Gross Earnings : ",round(ge,2))       
        print("\t\t\t","Deductions     : ", round(ded,2))
        print("\n")
        print("\t\t\t","Net Salary Payable : ",round(ge-ded,2))


        print("\n")
        print("\n")
        print("\n")
        print("\n")
        press = input("Press Any key To Continue..")
        maindata()

    except Exception as e:
        print("Database Error:",e)
        print("Please try again")

        SAL_SLIP()
    

#Display All Employee Records
def DELETED_EMP():
    try:
        print("{:>60}".format("-->> Display  DELETED Employee Record <<--"))
        mycursor.execute("use emp_manage")
        mycursor.execute("SELECT * FROM emp_infodeleted;")
        r = mycursor.fetchall()
        count = mycursor.rowcount
        print()
        print("\t\t\t\t\t","Total Records fetched",count)
        z=1
    
        for i in r:
            print("RECORD NO.",z)
            print("\n")
            print("Employee Id: ", i[0])
            print("Employee First Name: ", i[1])
            print("Employee Last Name: ", i[2])
            print("Employee  Father_Spouse_Name: ", i[3])
            print("Employee Date_of_Birth : ", i[4])
            print("Employee GraduateUG_PG : ", i[5])
            print("Employee dept_id : ", i[6])
            print("Employee RegularY_N: ", i[7])
            print("Employee Designation: ", i[8])
            print("Employee email: ", i[9])

            print("Employee contact_num: ", i[10])

            print("Employee Joining_Date: ", i[11])
            print("Employee Aadhar_num: ", i[12])
            print("Employee Address: ", i[13])
            print("Employee Grade: ", i[14])
            print("\n")
            z+=1
        press = input("Press Any key To Continue..")   
        maindata()   
      
    except Exception as e:
        print("Database Eroor",e)
        print("Please try again")
        DELETED_EMP()
    maindata()
 
# Main calling function
 
def maindata():
    while True:
        print("\t\t\t\t\t\t\t " ,"*"*40 )
        print("\t\t\t\t\t\t\t\t EMPLOYEE MANAGEMENT SYSTEM")
        print("\t\t\t\t\t\t\t " ,"*"*40 )
        print("=======================================================================================================")
        print("Please choose the desired option")
        print()


        print("\t\t1.ADDING OF NEW EMPLOYEE")
        print("\t\t2.DISPLAY ALL EMPLOYEE")
        print("\t\t3.SEARCH AND DISPLAY BY DESIGNATION")
        print("\t\t4.SEARCH AND DISPLAY BY NAME")
        print("\t\t5.SEARCH AND DISPLAY BY EMPLOYEE ID")
        print("\t\t6.DELETE EMPLOYEE")
        print("\t\t7.MODIFY DETAILS OF EMPLOYEE")
        print("\t\t8.GENERATE SALARY SLIP")
        print("\t\t9.PROMOTE AN EMPLOYEE")
        print("\t\t10.EXIT")

        print("=====================================================================================================")
        ch=int(input("Enter your choice(1 to 10):"))
        print("=====================================================================================================")
        if (ch==1):
            ADD_EMP()
            
        if (ch==2):
            DIS_EMP()
            
        if (ch==3):
            SEA_DESIG()
            
        if (ch==4):

            SEA_NAME()
            
        if (ch==5):
            SEA_EMPID()
            
        if (ch==6):
            DEL_EMP()
            
        if (ch==7):
            MOD_EMP()
            

        if (ch==8):
            SAL_SLIP()
           
        if (ch==9):
           Promote_Emp()
           
        if (ch==10):
            exit()
            



maindata()
