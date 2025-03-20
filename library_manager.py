import sqlite3
import pandas as pd
import streamlit as st
import os
import base64

# Set page configuration
st.set_page_config(
    page_title="Books Library Manager",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Function to encode image to base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Background image path
background_image_path = "backround_img.jpg"

# Encode image in base64
if os.path.exists(background_image_path):
    encoded_image = get_base64_of_image(background_image_path)
    background_css = f"""
    <style>
       .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_image}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
            animation: zoomEffect 10s infinite ease-in-out;
        }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)
else:
    st.warning("Background image not found! Make sure 'backround_img.jpg' is in the same folder.")

# 📌 Create or connect to the SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 📌 Create books table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE NOT NULL,
    author TEXT NOT NULL,
    genre TEXT,
    year INTEGER,
    read_status INTEGER
)
""")
conn.commit()
conn.close()

# 📌 Function to load books from database
def load_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, genre, year, read_status FROM books")
    books = cursor.fetchall()
    conn.close()
    
    return pd.DataFrame(books, columns=["Title", "Author", "Genre", "Year", "Read Status"])

# 📌 Function to save book into database
def save_books(title, author, genre, year, read_status):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO books (title, author, genre, year, read_status) VALUES (?, ?, ?, ?, ?)", 
                       (title, author, genre, year, read_status))
        conn.commit()
    except sqlite3.IntegrityError:
        st.warning("This book already exists in the library!")
    conn.close()

# 📌 Function to delete book from database
def delete_book(title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    conn.commit()
    conn.close()

# 📌 Streamlit UI
st.title("📚 Books Library Manager")

# 📌 Load books data
books_df = load_books()

# 📌 Ensure "Read Status" column exists
if "Read Status" not in books_df.columns:
    books_df["Read Status"] = False

# 📌 Add New Book
st.subheader("➕ Add a New Book")
title = st.text_input("Book Title")
author = st.text_input("Author")
genre = st.text_input("Genre")
year = st.number_input("Publication Year", min_value=1000, max_value=2025, step=1)
read_status = st.checkbox("Mark as Read")

if st.button("Add Book"):
    if title and author:
        save_books(title, author, genre, year, read_status)
        st.success(f"✅ '{title}' added successfully!")
        st.rerun()
    else:
        st.warning("⚠️ Please enter at least Title and Author!")

# 📌 Display Books
st.subheader("📖 Book List")
st.dataframe(books_df)

# 📌 Search Books
st.subheader("🔍 Search Books")
search_query = st.text_input("Enter title or author")
if search_query:
    filtered_books = books_df[
        books_df["Title"].str.contains(search_query, case=False, na=False) |
        books_df["Author"].str.contains(search_query, case=False, na=False)
    ]
    st.dataframe(filtered_books)

# 📌 Delete a Book
st.subheader("❌ Delete a Book")
if not books_df.empty:
    book_to_delete = st.selectbox("Select a book to delete", books_df["Title"].tolist())
    if st.button("Delete Book"):
        delete_book(book_to_delete)
        st.success(f"❌ '{book_to_delete}' deleted successfully!")
        st.rerun()

# 📌 Library Statistics
st.subheader("📊 Library Statistics")
total_books = books_df.shape[0]
total_read = books_df[books_df["Read Status"] == True].shape[0] if "Read Status" in books_df.columns else 0
read_percentage = (total_read / total_books * 100) if total_books > 0 else 0

st.write(f"📚 Total Books: {total_books}")
st.write(f"✅ Books Read: {total_read} out of {total_books} ({read_percentage:.2f}%)")
