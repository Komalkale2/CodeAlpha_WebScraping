from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

CSV_PATH = "data/remoteok_complete_dataset.csv"


@app.route("/")
def home():

    # Load CSV
    df = pd.read_csv(CSV_PATH, encoding="utf-8")

    # Fill missing values
    df = df.fillna("")

    # Query params
    search = request.args.get("search", "").strip()
    location = request.args.get("location", "").strip()
    role = request.args.get("role", "").strip()
    benefit = request.args.get("benefit", "").strip()
    salary_range = request.args.get("salary_range", "").strip()

    # -------------------------
    # SEARCH
    # -------------------------
    if search:
        search_lower = search.lower()

        mask = (
            df["Job Position"].str.lower().str.contains(search_lower, na=False)
            | df["Company Name"].str.lower().str.contains(search_lower, na=False)
            | df["Tags / Skills"].str.lower().str.contains(search_lower, na=False)
            | df["Role"].str.lower().str.contains(search_lower, na=False)
        )

        df = df[mask]

    # -------------------------
    # LOCATION FILTER
    # -------------------------
    if location:
        df = df[
            df["Location"]
            .str.strip()
            .eq(location)
        ]

    # -------------------------
    # ROLE FILTER
    # -------------------------
    if role:
        df = df[
            df["Role"]
            .str.strip()
            .eq(role)
        ]

    # -------------------------
    # BENEFIT FILTER
    # -------------------------
    if benefit:
        df = df[
            df["Benefits"]
            .str.contains(benefit, case=False, na=False)
        ]

    # -------------------------
    # SALARY FILTER
    # -------------------------
    df["Salary Max USD"] = pd.to_numeric(
        df["Salary Max USD"],
        errors="coerce"
    ).fillna(0)

    if salary_range == "0-50000":
        df = df[df["Salary Max USD"] <= 50000]

    elif salary_range == "50000-100000":
        df = df[
            (df["Salary Max USD"] > 50000)
            & (df["Salary Max USD"] <= 100000)
        ]

    elif salary_range == "100000-150000":
        df = df[
            (df["Salary Max USD"] > 100000)
            & (df["Salary Max USD"] <= 150000)
        ]

    elif salary_range == "150000+":
        df = df[df["Salary Max USD"] > 150000]

    # -------------------------
    # DYNAMIC DROPDOWN VALUES
    # -------------------------

    locations = sorted(
        df["Location"]
        .replace("", pd.NA)
        .dropna()
        .unique()
    )

    roles = sorted(
        df["Role"]
        .replace("", pd.NA)
        .dropna()
        .unique()
    )

    # extract benefits list
    benefit_set = set()

    for item in df["Benefits"]:
        if item:
            values = str(item).split(",")

            for value in values:
                cleaned = value.strip()

                if cleaned:
                    benefit_set.add(cleaned)

    benefits = sorted(list(benefit_set))

    jobs = df.to_dict(orient="records")

    return render_template(
        "index.html",
        jobs=jobs,
        search=search,
        locations=locations,
        roles=roles,
        benefits=benefits,
        location=location,
        role=role,
        benefit=benefit,
        salary_range=salary_range
    )


if __name__ == "__main__":
    app.run(debug=True)