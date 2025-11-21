import json
import os
import streamlit as st
from imdb import Cinemagoer, IMDbError

# IMDb Cache File for Streamlit caching
CACHE_FILE = "data/cached_movies.json"

@st.cache_data
def load_cache(filepath=CACHE_FILE):
    """Load the cache file."""
    if os.path.exists(filepath):
        try:
            # Open the file with UTF-8 encoding to support international characters
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            st.warning("Cache file is corrupted. Creating a new empty cache.")
            return {}
    return {}

def save_cache(cache, filepath=CACHE_FILE):
    """Save the cache file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=4, ensure_ascii=False)  # Keep UTF-8 characters

def fetch_movie(movie_id, cache):
    """
    Fetch movie information (year, director, genres) from IMDb or use cache.

    Args:
        movie_id: IMDb movie ID (tt1234567 or numeric)
        cache: dictionary for cached movie data

    Returns:
        dict: movie information with keys 'title', 'year', 'director', 'genres'
    """
    
    # Convert movie_id to string and remove 'tt' prefix if present
    str_movie_id = str(movie_id).replace("tt", "") 
    
    if str_movie_id in cache:
        return cache[str_movie_id]

    ia = Cinemagoer()
    
    try:
        # Fetch both 'main' and 'full' movie info
        movie = ia.get_movie(str_movie_id, info=['main', 'full']) 
        
        # 1. Get director
        directors = movie.get('director', [])
        director_name = directors[0]['name'] if directors else "Unknown"

        # 2. Get genres
        genres = movie.get('genres', [])

        movie_info = {
            "title": movie.get("title"),
            "year": movie.get("year"),
            "director": director_name,
            "genres": genres
        }
    
    except IMDbError as e:
        st.error(f"IMDb error: {e}")
        movie_info = {"title": "Unknown", "year": None, "director": "Unknown", "genres": []}
    except Exception:
        movie_info = {"title": "Unknown", "year": None, "director": "Unknown", "genres": []}

    # Add to cache
    cache[str_movie_id] = movie_info
    return movie_info
