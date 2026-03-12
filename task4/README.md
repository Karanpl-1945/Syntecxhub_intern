# Task 4 – Movie Recommendation System API

## Overview

This project implements a **Content-Based Movie Recommendation System** and exposes it through a **FastAPI-based REST API**.

The system recommends movies similar to a given movie based on **movie metadata such as genres and tags**. Similarity between movies is computed using **TF-IDF vectorization and cosine similarity**.

Users can send a movie title to the API and receive a list of recommended movies.

---

# Features

* Content-based movie recommendation system
* Uses **MovieLens dataset**
* Genre encoding using **One-Hot Encoding**
* Tag processing using **TF-IDF**
* Similarity computation using **Cosine Similarity**
* API built with **FastAPI**
* Input and output validation using **Pydantic**
* Clean modular project structure

---

# Dataset

This project uses the **MovieLens dataset** provided by GroupLens.

Download the dataset from:

https://grouplens.org/datasets/movielens/

Recommended dataset:

**MovieLens 32M Dataset**

After downloading and extracting, the dataset contains files such as:

* `movies.csv`
* `ratings.csv`
* `tags.csv`
* `links.csv`

---

# Data Setup

After downloading the dataset, place the required files inside:

```
task4/data/
```

Example structure:

```
task4/data/
    movies.csv
    ratings.csv
    tags.csv
```

---

# Large Files Not Included in Repository

The following files are **not included in the repository** because they exceed GitHub’s file size limits.

```
similarity.pkl
movies_data.pkl
```

Approximate sizes:

| File            | Size    |
| --------------- | ------- |
| similarity.pkl  | ~2–3 GB |
| movies_data.pkl | large   |

GitHub has a **100MB maximum file size limit**, so these files cannot be uploaded to the repository.

Instead, they must be **generated locally**.

---

# How to Generate Required Model Files

The repository contains a notebook named:

```
model.ipynb
```

This notebook performs the complete **data preprocessing and model generation pipeline**.

---

## Step 1 – Download Dataset

Download MovieLens dataset from:

https://grouplens.org/datasets/movielens/

Place files in:

```
task4/data/
```

---

## Step 2 – Run the Notebook

Open and run:

```
task4/model.ipynb
```

Run all cells sequentially.

---

## Step 3 – Processing Pipeline

The notebook performs the following operations:

1. Load MovieLens datasets
2. Merge movie metadata
3. Clean and preprocess text fields
4. Encode movie genres using **One-Hot Encoding**
5. Convert movie tags to numerical features using **TF-IDF**
6. Combine genre and tag features
7. Compute **cosine similarity** between movies
8. Save model artifacts

---

## Step 4 – Generated Files

After running the notebook, the following files will be created:

```
task4/model/
    similarity.pkl
    movies_data.pkl
```

These files are required for running the API.

---

# Running the API

Start the FastAPI server:

```
uvicorn app:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

### Recommend Movies

**POST**

```
/recommend
```

Request body example:

```json
{
  "movie": "Toy Story (1995)",
  "no_recommendation": 5
}
```

Example response:

```json
{
  "query_movie": "toy story (1995)",
  "recommendations": [
    {
      "movieId": 3114,
      "title": "Toy Story 2",
      "average_rating": 4.2,
      "rating_count": 3500
    }
  ]
}
```

---

# Project Structure

```
task4/
│
├── app.py
├── recommend.py
├── model.ipynb
│
├── schema/
│   ├── input.py
│   └── response.py
│
├── model/
│   └── (generated locally)
│
├── data/
│   └── (MovieLens dataset)
│
└── README.md
```

---

# Technologies Used

* Python
* FastAPI
* Scikit-learn
* Pandas
* NumPy
* Pydantic
* Uvicorn

---

# Notes

* Large datasets and model artifacts are intentionally excluded from the repository.
* Users must download the dataset and generate the model files locally before running the API.

---


