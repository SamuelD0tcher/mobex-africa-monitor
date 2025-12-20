# S(uper)Scraper 🕷️

**S(uper)Scraper** is a Python-based reconnaissance and data extraction tool designed for educational purposes and security auditing. It automates the process of mapping a website's infrastructure, identifying its tech stack, and extracting sensitive information into structured, readable reports.

## ⚖️ Legal Disclaimer

This tool is for **educational and ethical security testing purposes only**. Unauthorized scraping or scanning of websites without explicit permission may violate Terms of Service or local laws. Use this tool responsibly.

---

## ✨ Features

The scraper performs a deep dive into target URLs to extract:

* **Infrastructure Audit:** IP addresses, Whois data, and server Operating Systems.
* **Tech Stack Discovery:** Identification of frameworks and libraries (e.g., React, GSAP, Tailwind).
* **Data Extraction:**
* **Personnel:** Names and roles discovered on the site.
* **Contact Info:** Email addresses and social media profiles.
* **Security Assets:** Sitemap.xml, robots.txt, and active Cookies.


* **Page Analysis:**
* Full link mapping (Internal & External).
* Form field identification (Action targets and input types).
* Metadata and Page Titles.



---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* pip (Python package manager)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SamuelD0tcher/web-scraper.git
cd web-scraper

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```



### Usage

Run the main script and provide the **Home Page URL** of your target:

```bash
python main.py

```

---

## 📂 Output & Logging

The tool automatically generates structured reports in the `/logs` directory. Each session creates a Markdown (`.md`) file containing:

| Section | Description |
| --- | --- |
| **Files** | Status of robots.txt and sitemap.xml. |
| **Target Info** | Network-level data (IP, OS). |
| **Pages** | Breakdown of every discovered sub-page. |
| **Interactions** | List of all forms and cookie data. |

---

## 🛠️ Built With

* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - For parsing HTML.
* [Requests](https://requests.readthedocs.io/) - For handling HTTP protocols.
* [Python](https://www.python.org/) - Core logic and data processing.

---

Would you like me to help you write a `requirements.txt` file to match this README, or perhaps a `LICENSE` file for the repository?
