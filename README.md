# 🏥 Hospital Management System — Week 4 Assessment

## 📌 Project Overview

This project demonstrates practical implementation of **Python programming, PostgreSQL database design, MongoDB CRUD operations, querying, aggregation, and Object-Oriented Programming concepts** through a simple Hospital Management System.

The system manages hospital-related records including departments, doctors, patients, appointments, and billing information.

This assignment was developed as part of **Student Tribe – Week 4 Assessment**.

---

## 🎯 Objectives

* Design a relational database structure
* Establish relationships between entities
* Perform SQL CRUD operations
* Execute SQL joins and aggregations
* Demonstrate MongoDB document operations
* Apply Python OOP concepts
* Build a menu-driven console application

---

# 🛠 Tech Stack

| Layer          | Technology    |
| -------------- | ------------- |
| Language       | Python        |
| Database       | PostgreSQL    |
| NoSQL Database | MongoDB       |
| IDE            | VS Code       |
| Terminal       | psql, mongosh |

---

# 📂 Project Structure

```plaintext
hospital/
│
├── oop.py
├── menu.py
├── README.md
│
├── screenshots/
│   ├── er_diagram.jpg
│   ├── sql_tables.png
│   ├── sql_queries.png
│   ├── mongodb_crud.png
│   ├── mongodb_aggregation.png
│   ├── python_oop_output.png
│   └── menu_output.png
```

---

# 🗂 Database Design

## Entities

### Departments

Stores department details.

Attributes:

* dept_id (PK)
* dept_name
* description

### Doctors

Stores doctor information.

Attributes:

* doctor_id (PK)
* doctor_name
* specialization
* phone
* dept_id (FK)

### Patients

Stores patient information.

Attributes:

* patient_id (PK)
* patient_name
* age
* gender
* phone
* address

### Appointments

Stores appointment records.

Attributes:

* appointment_id (PK)
* appointment_date
* appointment_time
* patient_id (FK)
* doctor_id (FK)

### Bills

Stores payment information.

Attributes:

* bill_id (PK)
* appointment_id (FK)
* bill_date
* amount
* payment_status

---

# 🔗 Relationships

* One Department → Many Doctors
* One Doctor → Many Appointments
* One Patient → Many Appointments
* One Appointment → One Bill

---

# 🧾 SQL Implementation

Implemented:

✅ CREATE TABLE
✅ INSERT
✅ SELECT
✅ UPDATE
✅ DELETE
✅ INNER JOIN
✅ GROUP BY
✅ COUNT
✅ Aggregation Queries

Sample Reports:

* Patient billing details
* Appointment count by doctor
* Doctors per department

---

# 🍃 MongoDB Implementation

Implemented operations:

✅ insertOne()
✅ find()
✅ updateOne()
✅ deleteOne()
✅ aggregate()

Aggregation Example:

```javascript
db.patients.aggregate([
{
$group:{
_id:"$city",
total_patients:{
$sum:1
}
}
}
])
```

---

# 🐍 Python Implementation

## OOP Concepts

Implemented:

* Classes
* Objects
* Constructor
* Inheritance
* Method Overriding

Files:

* oop.py
* menu.py

---

# 📸 Output Screenshots

Screenshots attached inside `/screenshots`

* ER Diagram
* SQL Output
* MongoDB Output
* Python Output
* Menu Program Output

---

# 🚀 How To Run

### PostgreSQL

```bash
psql -U postgres
```

### MongoDB

```bash
mongosh
```

### Python

```bash
python oop.py
python menu.py
```

---

## Status

| Module       | Status     |
| ------------ | ---------- |
| ER Diagram   | ✅ Complete |
| SQL          | ✅ Complete |
| MongoDB      | ✅ Complete |
| Python OOP   | ✅ Complete |
| Menu Program | ✅ Complete |

---

Developed for Student Tribe — Week 4 Assessment
