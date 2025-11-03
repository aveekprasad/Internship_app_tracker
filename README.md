# 🎯 Internship Application Tracker

A simple **Python-based console application** to help students manage and track their internship applications efficiently.

---

## 📘 Overview

This program allows users to:
- Add new internship applications  
- View all stored applications  
- Count applications by status (e.g., applied, offer, rejected)  
- Check the next upcoming application deadline  

It’s designed as a minimal, beginner-friendly project focusing on Python lists, dictionaries, and basic logic implementation.

---

## 🧑‍💻 Author
**Aveek Kumar**  
Enrollment No: 2502140127  
Mini Project Code: E-30  

---

## ⚙️ Features

| Function | Description |
|-----------|--------------|
| **Add** | Add a new internship application (company, role, status, deadline) |
| **Show** | Display all applications in a clean format |
| **Count** | Show count of applications grouped by their current status |
| **Next Due** | Display the next approaching deadline among all ‘applied’ internships |
| **Exit** | Safely terminate the program |

---

## 🧠 How It Works

1. The program maintains all internship entries inside a list named `appli`.
2. Each application is stored as a dictionary with the following keys:
   - `company`
   - `role`
   - `status`
   - `deadline`
3. Menu options are displayed continuously until the user chooses to exit.

---

## ▶️ Usage

### **Run the Script**
Make sure Python 3 is installed on your system.  
Then execute:

```bash
python Internship_app_tracker.py
```

### **Sample Interaction**
```
=+=+=+= Welcome to Internship Tracker =+=+=+=
1. Add  2. Show  3. Count  4. Next Due  5. Exit
Enter your choice: 1
Company: Google
Role: Data Analyst Intern
Status (applied/offer/rejected): applied
Deadline (YYYY-MM-DD): 2025-11-10
✅ Application added!

Enter your choice: 2
-----All Applications-----
Google | Data Analyst Intern | applied | 2025-11-10
```

---

## 🧩 Example Output

```
Count by status: {'applied': 3, 'offer': 1, 'rejected': 2}

Next due: 2025-11-10 @ Google
```

---

## 🗂️ File Structure
```
Internship_app_tracker.py   # Main program file
README.md                   # Project documentation
```

---

## 💡 Future Enhancements
- Save data to a file (JSON or CSV) for persistence  
- Add search or update functionality  
- Implement GUI using Tkinter or web interface using Flask  

---

## 🧾 License
This project is created for educational purposes and is free to use and modify.
