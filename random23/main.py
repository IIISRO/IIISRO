from pymysql import NULL
import pymysql.cursors
hospital = pymysql.connect(host='localhost',
                             port=3309,
                             user='root',
                             password='1234',
                             database='hospital',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
#1
with hospital.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS `Hospital` (
       `Hospital_Id` int(11) NOT NULL AUTO_INCREMENT,
       `Hospital_Name` varchar(255) COLLATE utf8_bin NOT NULL,
       `Bed_Count` int NOT NULL,
        PRIMARY KEY (`Hospital_Id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
        AUTO_INCREMENT=1 ;
       """
        cursor.execute(sql)
hospital.commit()
with hospital.cursor() as cursor:
        sql = """
        CREATE TABLE IF NOT EXISTS `Doctor` (
       `Doctor_Id` int(11) NOT NULL,
       `Doctor_Name` varchar(255) COLLATE utf8_bin NOT NULL,
       `Hospital_Id` int NOT NULL,
       `Joining_Date` date NOT NULL,
       `Specialty` varchar(100) COLLATE utf8_bin NOT NULL,
       `Salary` decimal(10,2) NOT NULL,
       `Experience` int,
        FOREIGN KEY(`Hospital_Id`) REFERENCES `Hospital`(`Hospital_Id`),
        PRIMARY KEY (`Doctor_Id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
        AUTO_INCREMENT=1 ;
       """
        cursor.execute(sql)   
hospital.commit()
def Hospital_info(Hospital_Id, Hospital_Name, Bed_Count):
    with hospital.cursor() as cursor:
        sql = """
        insert into Hospital(Hospital_Id, Hospital_Name, Bed_Count) values (%s, %s, %s)
        """
        cursor.execute(sql, (Hospital_Id, Hospital_Name, Bed_Count))
    hospital.commit()
def Doctor_info(Doctor_Id, Doctor_Name, Hospital_Id,Joining_Date,Specialty,Salary):
    with hospital.cursor() as cursor:
        sql = """
        insert into Doctor(Doctor_Id, Doctor_Name, Hospital_Id,Joining_Date,Specialty,Salary) values (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (Doctor_Id, Doctor_Name, Hospital_Id,Joining_Date,Specialty,Salary))
    hospital.commit()


#2
def Get_Hospital(Hospital_Id):
    with hospital.cursor() as cursor:
        sql="""
        select * from Hospital where Hospital_Id=%s
        """
        cursor.execute(sql,(Hospital_Id))
        records=cursor.fetchone()
        return records
print(Get_Hospital(2))
def Get_Doctor(Doctor_Id):
    with hospital.cursor() as cursor:
        sql="""
        select * from Doctor where Doctor_Id=%s
        """
        cursor.execute(sql,(Doctor_Id))
        records=cursor.fetchone()
        return records

print(Get_Doctor(2))


#3
def Get_Doctor_List(Specialty,Amount):
    with hospital.cursor() as cursor:
        sql="""
        select * from Doctor where Specialty=%s and Salary>%s
        """
        cursor.execute(sql,(Specialty,Amount))
        records=cursor.fetchall()
        return records

print(Get_Doctor_List('Oncologist',10000))


#4
def Get_Doctor_List_by_HospitalId(Hospital_Id):
    with hospital.cursor() as cursor:
        sql="""
        select * from Doctor where Hospital_Id=%s
        """
        cursor.execute(sql,(Hospital_Id))
        records=cursor.fetchall()
        return records

print(Get_Doctor_List_by_HospitalId(1))


#5
def Update(Experience,Doctor_Name):
    with hospital.cursor() as cursor:
        sql="""
        update Doctor set Experience=%s where Doctor_name=%s
        """
        cursor.execute(sql, (Experience,Doctor_Name))
    hospital.commit()
Update(4,'Michael')
