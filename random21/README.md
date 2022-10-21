# SQL :open_file_folder:

We require you to solve the following tasks. Remember to read the requirements first.

#### Topics you need to know and use to solve tasks

* Adding Records to a Table
* Selecting Data from Table
* Selecting Record Based on Condition
* Working with Range and Membership Conditions
* Ordering the Result Set
* Updating Table Data
* Deleting Data from Tables
* Removing Database



**Final Notes**: *Remember to solve and send assignments on time* :hourglass_flowing_sand:

# Assignments' list 

## Assignment 1  :star:  :star:  :star:  :star:

### Description


The following is a table where you can apply sql queries

![table image](https://i.ibb.co/7phv1MK/screenshot-docs-google-com-2020-09-04-13-50-18.png)


**Code to create a schedule**

```
CREATE TABLE `Employee` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `age` INT,
    `salary` INT NOT NULL,
    `number` INT NOT NULL UNIQUE,
    `nationality` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);
```

Write sql queries that meet the requirements of the following terms

* Add the ten employees in the picture to the table

![table of data](https://i.ibb.co/jv1mxrT/screenshot-docs-google-com-2020-09-04-13-52-59.png)

* Select **all** employees in the table
* Select employees whose number is **equal to 6291**
* Choose employees with a salary of **more than 2,500**
* Select employees whose names **begin with the letter ‘A’**
* Choose employees from any of the **‘China, Japan, Russia, Korea’** countries
* Choose employees **between the ages of 30 and 50**
* Choose employees whose **name is Wad**e and whose **nationality is Japan**
* Choose employees **over the age of 30**, **number 7560 or 1853**
* **Double** the salaries of employees whose **names end in 'a'**
* **Delete** the employee **number 4014** from the table
* **Delete** the **Employee** table


**Powered by [TechAcademy](https://www.tech.edu.az/)**

