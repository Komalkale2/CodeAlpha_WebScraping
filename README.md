# CodeAlpha_WebScraping — Multi-Source Job Data Analytics Portal

## Overview

This project was developed as part of the **Data Analytics Internship Task (Task 1: Web Scraping)** for CodeAlpha.

The project collects real-world job data from multiple public job platforms using **Python web scraping**, processes the collected data, performs analysis, and presents jobs in a frontend job portal interface.

The goal of this project is to demonstrate:

* Web scraping using Python
* Data collection from public websites
* Dataset generation and cleaning
* Data analysis and visualization
* Building a frontend interface to display collected insights

---

## Features

### Web Scraping

The project extracts real-time job data from multiple public websites.

### Data Processing

Collected data is cleaned, merged, normalized, and exported into datasets.

### Data Analytics

Generate insights using Python and visualization libraries.

### Job Portal Frontend

A Flask-powered frontend allows users to:

* Search jobs
* Filter by location
* Filter by role/category
* Filter by company
* Filter by salary range
* View benefits and required skills
* Open job application links

---

## Data Sources

The following real public websites were used for scraping:

### 1. RemoteOK

Global remote job listings for developers, engineers, cybersecurity professionals, AI engineers, DevOps, backend, frontend, and more.

Website:
https://remoteok.com/

### 2. Freshers Junction

Fresher jobs, off-campus drives, internships, and graduate hiring opportunities.

Website:
https://freshersjunction.blogspot.com/

### 3. Debug With Shubham Jobs

Technology-focused hiring opportunities and placement updates.

Website:
https://debugwithshubham.com/jobs

---

## Technologies Used

### Programming Language

* Python

### Libraries

* requests
* BeautifulSoup4
* pandas
* matplotlib
* flask
* openpyxl
* lxml

### Frontend

* HTML
* CSS
* Flask Templates (Jinja2)

---

## Project Structure

```txt
CodeAlpha_WebScraping/
│── data/
│   ├── jobs_combined.csv
│   └── jobs_combined.xlsx
│
│── screenshots/
│
│── static/
│   └── style.css
│
│── templates/
│   └── index.html
│
│── web_scraper.py
│── analysis.py
│── app.py
│── requirements.txt
│── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/Komalkale2/CodeAlpha_WebScraping.git
cd CodeAlpha_WebScraping
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1 — Scrape Jobs

Run:

```bash
python web_scraper.py
```

This will:

* Scrape jobs from all websites
* Merge data
* Remove duplicates
* Save CSV and Excel datasets

Generated files:

```txt
data/jobs_combined.csv
data/jobs_combined.xlsx
```

---

### Step 2 — Run Analytics

Run:

```bash
python analysis.py
```

This generates visual insights and screenshots.

Examples:

* Top hiring companies
* Job locations
* Salary trends
* Most demanded skills

---

### Step 3 — Launch Job Portal

Run:

```bash
python app.py
```

Open browser:

```txt
http://127.0.0.1:5000
```

---

## Filters Available

The frontend portal supports:

* Search jobs
* Location filter
* Role filter
* Company filter
* Salary range filter
* Benefits filter
* Skills filtering

---

## Dataset Fields

The project collects:

* Source
* Job Title
* Company
* Location
* Experience
* Qualification
* Role
* Salary
* Skills
* Benefits
* Posted Date
* Apply Link

---

## Screenshots

Add screenshots of:

1. Home page
2. Job cards
3. Filters working
4. Analytics charts

inside the `/screenshots` folder.

---

## Future Improvements

* Database integration (MySQL / MongoDB)
* Live scheduled scraping
* User authentication
* Job recommendation system
* Resume matching
* Advanced analytics dashboard

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Web scraping
* Data preprocessing
* Data analytics
* Data visualization
* Frontend integration with Flask
* Dataset creation from public web pages
* Real-world job market analysis

---

## Author

**komal kale**

CodeAlpha Data Analytics Internship Project
