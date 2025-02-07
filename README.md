Here's a basic `README.md` template for performing CRUD operations using Django API requests:

---

# **Django API CRUD Operations**

This project demonstrates how to perform **Create**, **Read**, **Update**, and **Delete** (CRUD) operations using **MongoDB**. The API allows for easy management of book records, including adding new books, fetching book details, updating existing entries, and deleting books.

---

## **Table of Contents**

- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
  - [Create (POST)](#1-create-post)
  - [Read (GET)](#2-read-get)
  - [Update (POST)](#3-update-post)
  - [Delete (POST)](#4-delete-post)
- [Testing Using Postman](#testing-using-postman)
- [License](#license)

---

## **Technologies Used**

- **Python 3.x**
- **Django 4.x**
- **MongoDB** (Using `pymongo` for database operations)
- **Postman** (For API testing)

---

## **Setup Instructions**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/django-crud-api.git
   cd django-crud-api
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB Connection**

   In your `settings.py`, add:

   ```python
   from pymongo import MongoClient
   client = MongoClient("mongodb://localhost:27017/")
   db = client["YourDatabaseName"]
   coll = db["YourCollectionName"]
   ```

5. **Run Migrations (if using Django models)**

   ```bash
   python manage.py migrate
   ```

---

## **Running the Server**

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at **`http://127.0.0.1:8000/`**.

---

## **API Endpoints**

### 1. **Create (POST)**

- **Endpoint:** `/add/`
- **Method:** `POST`
- **Description:** Adds a new book record to the database.

**Sample Request Body:**

```json
{
  "title": "Percy Jackson: The Last Olympian",
  "author": "Rick Riordan",
  "pages": 300,
  "rating": 8,
  "geners": ["fantasy", "magic", "Greek mythology"]
}
```

---

### 2. **Read (GET)**

- **Endpoint:** `/display/`
- **Method:** `GET`
- **Description:** Fetches all book records from the database.

---

### 3. **Update (POST)**

- **Endpoint:** `/change/`
- **Method:** `POST`
- **Description:** Updates the author and genres of an existing book.

**Sample Request Body:**

```json
{
  "title": "Percy Jackson: The Last Olympian",
  "author": "Rick Riordan Updated",
  "geners": ["adventure", "mythology"]
}
```

---

### 4. **Delete (POST)**

- **Endpoint:** `/remove/`
- **Method:** `POST`
- **Description:** Deletes a book record by title.

**Sample Request Body:**

```json
{
  "title": "Percy Jackson: The Last Olympian"
}
```

---

## **Testing Using Postman**

1. **Open Postman** and set the request type (`POST`, `GET`, etc.) depending on the operation.
2. **Set the request URL** to `http://127.0.0.1:8000/{endpoint}/`.
3. For `POST` requests:
   - Go to the **Body** tab.
   - Select **raw** and choose **JSON** format.
   - Input your JSON data.
4. **Send the request** and check the response.

---

## **License**

This project is licensed under the [MIT License](LICENSE).

---

Let me know if you'd like to customize this further! 🚀
