# Data Engineer Take-Home Challenge

## Overview

This exercise is designed to test your ability to:
1. Build a Python-based ETL that ingests raw CSV files, applies basic transformations, and loads data into SQLite.
2. Use dbt to model that raw data into a dimensional schema and answer business questions.

You are free to use any AI assistance—but at the end we want to see your code style, your SQL modeling choices, and your test coverage.

---

## Repository Layout

```
.
├── ingest_exercise.py             # Python ETL skeleton
├── requirements.txt               # Python dependencies (if any)
├── sample_data/                   # Raw CSV uploads
│   ├── company_a_employee_uploads.csv
│   ├── company_b_employee_uploads.csv
│   └── company_c_employee_uploads.csv
├── employees.sqlite               # Empty SQLite database (to be populated)
├── dbt_project/                   # dbt project for modeling
│   ├── dbt_project.yml            # dbt project configuration
│   ├── profiles.yml               # dbt connection profiles
│   └── models/                    # dbt models
│       ├── staging/               # Staging models
│       │   ├── stg_employees.sql  # Staging model stub
│       │   └── schema.yml         # Staging schema stub
│       ├── intermediate/          # Intermediate models (optional)
│       │   └── schema.yml         # Intermediate schema stub (no SQL file initially)
│       └── marts/                 # Final models
│           ├── employees.sql      # Employee dimension stub
│           └── schema.yml         # Marts schema stub (no comparison model initially)
└── README.md                      # This file
```

---

## Part 1 – Python ETL

**Goal:** Read the CSVs under `sample_data/`, normalize and enrich them, then write the results into a raw table in `employees.sqlite`.

1. Add any external Python packages you use for the ETL script to `requirements.txt`.
2. Implement the "transform" and "load" sections in `ingest_exercise.py`:
   - Standardize column names (e.g. snake_case).
   - Parse dates into ISO 8601.
   - Cast numeric fields.
   - Create and load into a raw table:
     - `raw_employees` (one row per CSV record)

3. Run and verify:
    ```bash
    # Note: This script ingests all CSV files from the specified directory.
    python ingest_exercise.py \
      --ingest-directory sample_data \
      --db-filename employees.sqlite

    sqlite3 employees.sqlite "SELECT COUNT(*) FROM raw_employees;" | cat
    ```

---

## Part 2 – Data Modeling with dbt

**Goal:** Build a dimensional model using dbt to analyze employee compensation relative to peer groups.

**Business Problem:**
Analyze how individual employee compensation compares to the average compensation within their defined peer group.
A peer group is defined by `company_name`, `employee_job_grp`, and `employee_job_lvl`.
The final model should allow slicing the comparison by various employee attributes (e.g., gender, race, location).

**Understanding dbt for this Exercise:**
dbt (data build tool) helps transform data in your warehouse (in this case, the SQLite database) by writing SQL `SELECT` statements. Here's a quick overview of the key files:
*   **`.sql` files in `models/`:** These define your data models. Each file typically contains one `SELECT` statement. dbt compiles this SQL and runs it against your database to create views or tables. You'll build your staging, intermediate (optional), and final mart models here.
*   **`.yml` files (e.g., `schema.yml`):** These files define metadata, descriptions, and tests for your models and their columns. Defining tests (like `not_null`, `unique`) helps ensure data quality.
*   **`dbt_project.yml`:** Configures your dbt project (like the project name, model paths, and materialization defaults). You generally won't need to modify this file.
*   **`profiles.yml`:** Defines how dbt connects to your database (credentials, database type, file path for SQLite). This file is pre-configured for this exercise.

### Instructions

1. Change directory into the dbt project:
    ```bash
    cd dbt_project
    ```
2. Install dbt:
    ```bash
    pip install dbt-core dbt-sqlite
    ```
3. In `models/staging/`, build the staging model `stg_employees` using `source('employees', 'raw_employees')`. Apply necessary cleaning and casting.
4. In `models/marts/`, build a clean `employees` dimension model by selecting and appropriately renaming/casting columns from `stg_employees`.
5. Build the necessary models (potentially including intermediate models, though the structure is up to you) to create a final mart model that addresses the **Business Problem** defined above. You might name the final model `mart_employee_compensation_comparison` or choose another appropriate name.
6. In your models' `schema.yml` files, define appropriate tests (e.g., not_null, unique, referential integrity, custom tests) and provide clear `description`s for each model and its columns.
7. Run and test your models:
    ```bash
    # You might need to specify profiles dir and target depending on your setup
    # e.g., dbt run --profiles-dir . --target dev
    dbt run
    dbt test
    ```

---

## Submission

- ???
- Include in your README:
  - A short summary of your modeling decisions (e.g., why you chose certain intermediate steps or calculations).
  - Example SQL query/output demonstrating how your final model addresses the compensation comparison problem.
- We will evaluate:
  - Functionality and correctness of the ETL process.
  - Overall code quality and adherence to best practices.
  - Soundness and clarity of the data modeling approach.
  - Appropriateness of data validation and testing.
  - Quality of documentation (e.g., model/column descriptions, README notes).

---

Good luck!
