## Movie-Recommendation
This project is a Movie Recommendation System built using Machine Learning, Natural Language Processing (NLP), and Streamlit to provide an interactive and user-friendly web interface.

# About the Project
The system recommends movies based on content similarity, allowing users to select their favorite movie and instantly get five personalized recommendations along with posters. It uses textual metadata such as cast, crew, keywords, genres, and overview to compute similarity scores between movies.

# Key Features

1. Content-Based Filtering using NLP techniques
2. TF-IDF and Cosine Similarity for movie comparison
3. Movie metadata preprocessing (combining cast, genre, keywords, etc.)
4. Poster Fetching via TMDB API for a visually rich UI
5. Deployed via Streamlit for an interactive web experience

# Tech Stack

Python
Scikit-learn (Vectorization and Similarity computation)
Pandas & NumPy (Data processing)
NLTK / Regex (Text cleaning, optional)
TMDB API (Fetching movie posters)
Streamlit (Web app interface)

# How It Works

A user selects a movie from the dropdown menu.
The app processes the movie’s metadata using NLP.
It computes similarity scores and retrieves the top 5 closest matches.
Posters are fetched from TMDB and displayed alongside the titles.

# Steps to run

1. Run the requirements.txt file
   pip install -r requirements.txt
2. Run the movierecommender.py file
   python movierecommender.py
3. This will give you two pickle files as output - similarity.pkl and movie.pkl
4. Run the app.py file using streamlit
   streamlit run app.py

# Screenshots of the UI

Landing page
<img width="500" alt="image" src="https://github.com/user-attachments/assets/b3efaa3d-41bf-40c7-a32a-33f8f31e9a72" />


Recommedation after typing a movie
<img width="500" alt="image" src="https://github.com/user-attachments/assets/5a42f688-732e-4fab-b140-a786269755e8" />
