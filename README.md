# 🚀 X Trends Scraper

A full-stack project that scrapes the **top 5 trending topics from X (Twitter)** and displays them on a simple React dashboard.

---

## 📖 Project Overview

**Xplore Trends** helps users stay updated with the latest trending topics on **X (formerly Twitter)**.  
The project automatically:

- Scrapes trending topics using Selenium.  
- Stores them in a **PostgreSQL** database.  
- Serves data through a **Django REST API**.  
- Displays them on a **React dashboard**.  

### Goals
- Learn and demonstrate **full-stack development** using Django + React.  
- Work with **web scraping** (Selenium) to fetch real-time data.  
- Build a **RESTful API** to serve frontend data dynamically.  
- Store and manage data reliably in **PostgreSQL**.  

---

## Visit the website:
- URL = https://final-x-trends-scraper.vercel.app/

## 🛠️ Tech Stack

- **Frontend:** React (Vite)  
- **Backend:** Django + Django REST Framework  
- **Scraper:** Selenium  
- **Database:** PostgreSQL (NeonDB) 

---

## 📂 Project Structure

```
Xplore_Trends/
├── frontend/           # React frontend (Vite)
├── X_scraper/          # Django backend
│   ├── X_scraper/      # Django project settings
│   ├── trends_scraper/ # Django app + scraper scripts
│   └── manage.py
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashish7078/Final_X_Trends_Scraper.git
cd Final_X_Trends_Scraper
```

---

### 2️⃣ Backend Setup (Django)

```bash
cd X_scraper

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Edit .env to include: SECRET_KEY, NEON_DB_URL, X_EMAIL, X_USERNAME, X_PASSWORD

# Apply migrations
python manage.py migrate

# Run the backend server
python manage.py runserver
```

The backend runs at: **http://127.0.0.1:8000**

---

### 3️⃣ Frontend Setup (React)

```bash
cd frontend

# Install dependencies
npm install

# Start the dev server
npm run dev
```

The frontend runs at: **http://localhost:5173**

---

## 🔗 API Endpoints

| Method | Endpoint          | Description                           |
|--------|------------------|---------------------------------------|
| GET    | `/api/trends/`   | Fetches the list of top trending topics |
| GET    | `/api/trends/<id>` | Fetches details of a single trend     |

---

## 🗄️ Database

- **PostgreSQL (NeonDB)** is used to store all scraped trends.  
- Each record includes:
  - Top 5 trends from a scrape  
  - Timestamp of the run  
  - Source IP address  

---

## 🖥️ Frontend Features

- Displays the **latest trends** in a clean, responsive dashboard.  
- Fetches updated trends dynamically from the backend API.  
- Shows topic, category, and post count for each trend (if available).  

---

## ⚡ Future Improvements

- ⏳ **Automate Scraping:** Use Django management commands + cron jobs.  
- 📜 **Pagination:** Browse historical trends.  
- 🎨 **UI/UX Enhancements:** Categories, search, filtering.  
- 🔐 **User Authentication:** Users can register, log in, and favorite trends.  

---

## 🤝 Contributing

Contributions are welcome!  

1. Fork the Project  
2. Create your Feature Branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your Changes  
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push to the Branch  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request  

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.  
Please be mindful of **X.com's Terms of Service** when using this scraper.
