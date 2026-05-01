import pandas as pd
import numpy as np
import os

def generate_data(n=500):
    np.random.seed(42)

    df = pd.DataFrame({
        "prior_gpa": np.round(np.random.uniform(2.0, 4.0, n), 2),
        "attendance_pct": np.random.randint(50, 100, n),
        "quiz_avg": np.random.randint(40, 100, n),
        "assign_avg": np.random.randint(40, 100, n),
        "midterm": np.random.randint(40, 100, n),
        "study_hours_wk": np.random.randint(1, 10, n),
        "on_time_submit_pct": np.random.randint(50, 100, n),
        "lms_logins_wk": np.random.randint(0, 10, n),
        "forum_posts": np.random.randint(0, 5, n),
        "commute_min": np.random.randint(5, 60, n),
        "gender": np.random.choice(["M", "F"], n),
        "school_type": np.random.choice(["Private", "Govt"], n),
        "parent_edu": np.random.choice(["UG", "PG", "School"], n),
    })

    score = (
        df["prior_gpa"] * 10 +
        df["attendance_pct"] * 0.3 +
        df["quiz_avg"] * 0.2 +
        df["assign_avg"] * 0.2 +
        df["midterm"] * 0.3
    )

    df["passed"] = (score > 65).astype(int)

    os.makedirs("data", exist_ok=True)
    df.to_csv("data/students.csv", index=False)

    print("✅ Data generated")