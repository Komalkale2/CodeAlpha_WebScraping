import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

all_jobs = []


# ============================================
# Helper Function
# ============================================

def safe_text(value):
    if value is None:
        return "N/A"

    value = str(value).strip()

    return value if value else "N/A"


# ============================================
# SOURCE 1 — REMOTE OK
# ============================================

def scrape_remoteok():

    print("\n[1/3] Scraping RemoteOK...")

    url = "https://remoteok.com/api"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        data = response.json()

        jobs = data[1:]

        print(f"Found {len(jobs)} jobs")

        for job in jobs:

            all_jobs.append({

                "Source":
                "RemoteOK",

                "Job Title":
                safe_text(
                    job.get("position")
                ),

                "Company":
                safe_text(
                    job.get("company")
                ),

                "Location":
                safe_text(
                    job.get("location")
                ),

                "Experience":
                safe_text(
                    job.get("experience")
                ),

                "Qualification":
                "N/A",

                "Role":
                safe_text(
                    job.get("role")
                ),

                "Salary":
                f"{job.get('salary_min', 'N/A')} - "
                f"{job.get('salary_max', 'N/A')}",

                "Skills":
                ", ".join(
                    job.get("tags", [])
                ),

                "Benefits":
                ", ".join(
                    job.get("benefits", [])
                ),

                "Posted Date":
                safe_text(
                    job.get("date")
                ),

                "Apply Link":
                safe_text(
                    job.get("url")
                )
            })

    except Exception as e:
        print("RemoteOK Error:", e)


# ============================================
# SOURCE 2 — FRESHERS JUNCTION
# ============================================

def scrape_freshersjunction():

    print("\n[2/3] Scraping Freshers Junction...")

    base_url = (
        "https://freshersjunction.blogspot.com/"
    )

    try:

        response = requests.get(
            base_url,
            headers=HEADERS
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        post_links = []

        for a in soup.find_all(
            "a",
            href=True
        ):

            href = a["href"]

            if (
                "freshersjunction.blogspot.com"
                in href
                and href.endswith(".html")
            ):
                post_links.append(href)

        post_links = list(
            set(post_links)
        )

        print(
            f"Found {len(post_links)} posts"
        )

        def extract(text, field):

            for line in text.split("\n"):

                if (
                    field.lower()
                    in line.lower()
                ):

                    if ":" in line:
                        return (
                            line
                            .split(":")[-1]
                            .strip()
                        )

            return "N/A"

        for i, link in enumerate(
            post_links
        ):

            try:

                print(
                    f"Post "
                    f"{i+1}/{len(post_links)}"
                )

                r = requests.get(
                    link,
                    headers=HEADERS
                )

                page = BeautifulSoup(
                    r.text,
                    "html.parser"
                )

                page_text = page.get_text(
                    "\n",
                    strip=True
                )

                title = (
                    page.title.text.strip()
                    if page.title
                    else "N/A"
                )

                all_jobs.append({

                    "Source":
                    "Freshers Junction",

                    "Job Title":
                    safe_text(title),

                    "Company":
                    safe_text(
                        extract(
                            page_text,
                            "Company Name"
                        )
                    ),

                    "Location":
                    safe_text(
                        extract(
                            page_text,
                            "Location"
                        )
                    ),

                    "Experience":
                    safe_text(
                        extract(
                            page_text,
                            "Experience"
                        )
                    ),

                    "Qualification":
                    safe_text(
                        extract(
                            page_text,
                            "Qualification"
                        )
                    ),

                    "Role":
                    safe_text(
                        extract(
                            page_text,
                            "Job Role"
                        )
                    ),

                    "Salary":
                    safe_text(
                        extract(
                            page_text,
                            "Salary"
                        )
                    ),

                    "Skills":
                    safe_text(
                        extract(
                            page_text,
                            "Skills"
                        )
                    ),

                    "Benefits":
                    "N/A",

                    "Posted Date":
                    "N/A",

                    "Apply Link":
                    link
                })

                time.sleep(0.8)

            except Exception as e:
                print(
                    "Post error:",
                    e
                )

    except Exception as e:
        print(
            "Freshers Junction Error:",
            e
        )


# ============================================
# SOURCE 3 — DEBUG WITH SHUBHAM
# ============================================

def scrape_debugwithshubham():

    print(
        "\n[3/3] Scraping "
        "DebugWithShubham..."
    )

    url = (
        "https://debugwithshubham.com/jobs"
    )

    try:

        response = requests.get(
            url,
            headers=HEADERS
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        cards = soup.find_all(
            ["article", "div"]
        )

        count = 0

        for card in cards:

            text = card.get_text(
                " ",
                strip=True
            )

            if (
                "apply"
                in text.lower()
                and len(text) > 40
            ):

                title = "N/A"

                heading = card.find(
                    ["h1", "h2", "h3", "h4"]
                )

                if heading:
                    title = heading.get_text(
                        strip=True
                    )

                apply_link = "N/A"

                for a in card.find_all(
                    "a",
                    href=True
                ):

                    if (
                        "apply"
                        in a.get_text()
                        .lower()
                    ):
                        apply_link = (
                            a["href"]
                        )
                        break

                all_jobs.append({

                    "Source":
                    "DebugWithShubham",

                    "Job Title":
                    safe_text(title),

                    "Company":
                    "N/A",

                    "Location":
                    "India",

                    "Experience":
                    "Fresher",

                    "Qualification":
                    "N/A",

                    "Role":
                    "Tech",

                    "Salary":
                    "N/A",

                    "Skills":
                    "N/A",

                    "Benefits":
                    "N/A",

                    "Posted Date":
                    "N/A",

                    "Apply Link":
                    safe_text(
                        apply_link
                    )
                })

                count += 1

        print(
            f"Found {count} jobs"
        )

    except Exception as e:
        print(
            "DebugWithShubham Error:",
            e
        )


# ============================================
# RUN ALL SCRAPERS
# ============================================

scrape_remoteok()
scrape_freshersjunction()
scrape_debugwithshubham()

# ============================================
# SAVE DATASET
# ============================================

print("\nSaving dataset...")

df = pd.DataFrame(all_jobs)

df.drop_duplicates(
    inplace=True
)

os.makedirs(
    "data",
    exist_ok=True
)

csv_path = (
    "data/jobs_combined.csv"
)

excel_path = (
    "data/jobs_combined.xlsx"
)

df.to_csv(
    csv_path,
    index=False,
    encoding="utf-8-sig"
)

df.to_excel(
    excel_path,
    index=False
)

print("\nDONE!")
print(
    f"Total Jobs: {len(df)}"
)
print(
    f"CSV: {csv_path}"
)
print(
    f"Excel: {excel_path}"
)

print("\nPreview:")
print(df.head())