# Django Excel Dataset Creation

This project is a Django REST API that allows users to upload Excel/CSV files, extract columns, apply configurable operations (filter, group, aggregate), and download the processed output.
---

## Features

- Upload Excel / CSV files
- Store uploaded files in media folder
- Fetch column names from dataset
- Apply filter, group by, and aggregation
- Generate processed Excel output
- Download result file
- API testing using Postman

---

## Tech Stack

- Backend: Django, Django REST Framework
- Data Processing: Pandas
- Database: SQLite
- Testing: Postman

---

## Installation

### 1. Clone Repository

clone this repo
```bash
cd weather_system
```

### 2. Create Virtual Environment

```bash
python -m venv environment
environment\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django djangorestframework pandas openpyxl
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```bash
python manage.py runserver
```

Server will start at:

```text
http://127.0.0.1:8000/
```

---

## API Usage (Postman)

### 1️⃣ Upload File

#### Endpoint

```http
POST /upload/
```

#### Body (form-data)

| Key  | Type | Value |
|------|------|-------|
| file | File | Select Excel/CSV file |

#### Response Example

```json
{
  "message": "File uploaded",
  "file_id": 6,
  "saved_path": "D:\\...\\media\\uploads\\file.xlsx"
}
```

---

### 2️⃣ Get Columns

#### Endpoint

```http
GET /columns/<file_id>/
```

#### Example

```http
GET /columns/6/
```

#### Response Example

```json
{
  "columns": [
    "Order Date",
    "Product Name",
    "Category",
    "Region",
    "Quantity",
    "Sales",
    "Profit"
  ]
}
```

---

### 3️⃣ Process File

#### Endpoint

```http
POST /process/
```

#### Body (raw JSON)

```json
{
  "file_id": 6,
  "config": {
    "filter": {
      "Region": "West"
    },
    "group_by": "Category",
    "aggregate": {
      "Sales": "sum",
      "Profit": "mean"
    }
  }
}
```

#### Response

```text
Downloads: result.xlsx
```

---

## Configuration Format

### Example

```json
{
  "filter": {
    "Region": "West"
  },
  "group_by": "Category",
  "aggregate": {
    "Sales": "sum"
  }
}
```

---

## Output

Processed files are saved in:

media/output_<file_id>.xlsx
