# 📚 **Library Manager**  

## 📖 **Overview**  
**Library Manager** is a **Streamlit-based** application designed to help users efficiently manage their book collections. It allows users to **add, remove, search, and track** reading progress of books, with data stored in an **SQLite database**.  

## 🚀 **Features**  
- ✅ **Add a Book** – Enter book details including **Title, Author, Genre, Year, and Read Status**.  
- ❌ **Remove a Book** – Delete books from the collection.  
- 🔍 **Search for a Book** – Search by **Title or Author**.  
- 📋 **Display All Books** – View the complete list of books.  
- 📊 **Statistics** – View **Total Books** and **Percentage of Books Read**.  
- 🗄️ **Database Storage** – All book records are stored in an **SQLite database (`library.db`)** for efficient data management.  

## 🎯 **Why Use SQLite for This Project?**  
- ✅ **Data Persistence** – Unlike CSV files, **SQLite** ensures that book records remain stored even after restarting the app.  
- ⚡ **Better Performance** – Faster **search, retrieval, and storage** of book records compared to file-based storage.  
- 📈 **Scalability** – Supports **thousands of book records** efficiently without performance issues.  
- 🔐 **Data Integrity** – Prevents **duplicate book entries** with constraints like `UNIQUE` on titles.  
- 🔎 **Structured Queries** – Allows **advanced filtering and searching** using SQL queries.  

## 📂 **Project Structure**  
📁 Library-Manager
│── 📁 backround_img.jpg # Background image
│── 📜 manager.py # Main application file
│── 📜 library.db # SQLite database file
│── 📜 README.md # Project documentation

## 🤝 **Contributing**  
Feel free to submit **issues** or **pull requests** to improve this project!  

## 🛠 **Developed by Rafiha Siddiqui** 🚀  
