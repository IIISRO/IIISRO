import main

hospital_info=[[1, "Mayo Clinic", 200],[2, "Cleveland Clinic", 400],[3, "Johns Hopkins", 1000],[4, "UCLA Medical Center", 1500]]
for i in range(4):
    Hospital_Id=hospital_info[i][0]
    Hospital_Name=hospital_info[i][1]
    Bed_Count=hospital_info[i][2]
    main.Hospital_info(Hospital_Id,Hospital_Name,Bed_Count)

doctor_info=[[101, "David", 1,'2005-02-10',"Pediatric",40000],[102, "Michael", 1,'2018-07-23',"Oncologist",20000],[103, "Susan", 2,'2016-05-19',"Garnacologist",25000],[104, "Robert", 2,'2017-12-28',"Pediatric",28000],[105, "Linda", 3,'2004-06-04',"Garnacologist",42000],[106, "William", 3,'2012-09-11',"Dermatologist",30000],[107, "Richard", 4,'2014-08-21',"Garnacologist",32000],[108, "Karen", 4,'2011-10-17',"Radiologist",30000]]
for i in range(8):
    Doctor_Id=doctor_info[i][0]
    Doctor_Name=doctor_info[i][1]
    Hospital_Id=doctor_info[i][2]
    Joining_Date=doctor_info[i][3]
    Specialty=doctor_info[i][4]
    Salary=doctor_info[i][5]
    main.Doctor_info(Doctor_Id,Doctor_Name,Hospital_Id,Joining_Date,Specialty,Salary)