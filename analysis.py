import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Load dataset
file_path = "data/remoteok_complete_dataset.csv"
df = pd.read_csv(file_path)

print("Dataset Loaded Successfully!")
print("\nDataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nPreview:")
print(df.head())

# -----------------------------------
# 1. Top Hiring Companies
# -----------------------------------
top_companies = df["Company Name"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_companies.plot(kind="bar")
plt.title("Top 10 Hiring Companies")
plt.xlabel("Company Name")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/top_companies.png")
plt.show()

# -----------------------------------
# 2. Top Hiring Locations
# -----------------------------------
top_locations = df["Location"].fillna("Unknown").value_counts().head(10)

plt.figure(figsize=(10, 6))
top_locations.plot(kind="bar")
plt.title("Top Hiring Locations")
plt.xlabel("Location")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/top_locations.png")
plt.show()

# -----------------------------------
# 3. Most Common Skills / Tags
# -----------------------------------
skills_series = df["Tags / Skills"].dropna()

all_skills = []

for skill_set in skills_series:
    skills = [skill.strip() for skill in skill_set.split(",")]
    all_skills.extend(skills)

skill_counts = Counter(all_skills)
top_skills = dict(skill_counts.most_common(10))

plt.figure(figsize=(10, 6))
plt.bar(top_skills.keys(), top_skills.values())
plt.title("Top 10 Most Required Skills")
plt.xlabel("Skills")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/top_skills.png")
plt.show()

# -----------------------------------
# 4. Salary Distribution
# -----------------------------------
salary_df = df[df["Salary Max USD"] > 0]

if len(salary_df) > 0:
    plt.figure(figsize=(10, 6))
    salary_df["Salary Max USD"].plot(kind="hist", bins=20)
    plt.title("Salary Distribution")
    plt.xlabel("Salary (USD)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("screenshots/salary_distribution.png")
    plt.show()

# -----------------------------------
# 5. Top Job Roles
# -----------------------------------
top_roles = df["Role"].fillna("Unknown").value_counts().head(10)

plt.figure(figsize=(10, 6))
top_roles.plot(kind="bar")
plt.title("Top Job Categories / Roles")
plt.xlabel("Role")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("screenshots/top_roles.png")
plt.show()

print("\nAnalysis Completed Successfully!")
print("\nSaved Charts in screenshots/ folder")