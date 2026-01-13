# BookWise | Digital Book Directory & Review System

A lightweight, Flask-powered web application for managing a personal library and tracking reader reviews. This system allows you to catalog books, calculate average ratings dynamically, and view a ranked leaderboard of the highest-rated titles.

---

# BookWise | Digital Book Directory & Review System
<p align="center">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel Badge" />
  <br />
  <a href="https://book-store-beige-nu.vercel.app/" target="_blank">
    <img src="https://img.shields.io/badge/live_demo-online-brightgreen?style=flat-square" alt="Live Demo" />
  </a>
</p>

---

## Features

* **Book Management:** Add new books with title, publication year, and author details.
* **Smart Rating System:** Automatically calculates and updates the average rating as new reviews are added.
* **Reader Feedback:** Tracks multiple reader comments and ratings per book.
* **Dynamic Leaderboard:** View books ranked from highest to lowest based on user satisfaction.
* **Clean UI:** A responsive, modern interface built with **Tailwind CSS**.

---

## Technical Stack

* **Backend:** Python 3.x, Flask
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
* **Data Structure:** Custom Object-Oriented logic using in-memory Python classes (`Book`, `Reader`, `BookDirectory`).

---

##  Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/amirsakib16/Book-Review-and-Users-Activity.git](https://github.com/amirsakib16/Book-Review-and-Users-Activity.git)
    
    ```

2.  **Install Dependencies:**
    Make sure you have Python installed, then install Flask:
    ```bash
    pip install flask
    ```

3.  **Project Structure:**
    Ensure your folders are organized as follows:
    ```text
    /your-project-folder
    ├── app.py              # The Python/Flask code
    └── templates/
        └── index.html      # The UI/Frontend code
    ```

4.  **Run the Application:**
    ```bash
    python app.py
    ```

5.  **Access the Web Interface:**
    Open your browser and navigate to:
    `http://127.0.0.1:5000`

---
**Virtual Environment Activation**
```text
python -m venv env
env/Scripts/activate
```
---
##  How It Works

1.  **Adding a Book:** Go to the "Add Book" section. The system checks for duplicates based on Title, Year, and Author before saving.
2.  **Submitting a Review:** Select a book from the dropdown, enter your name, a rating (1-5), and your comment.
3.  **The Leaderboard:** The backend parses stored review strings, calculates the mean score, and sorts the display list in descending order.

---

##  License
This project is open-source and available under the MIT License.
