from models.movie_model import Movie

def test_to_dict():
   
    movie = Movie("Inception", "Action", 8.8, 2010, "En tjuv som stjäl idéer genom drömmar.")

   
    expected = {
        "title": "Inception",
        "genre": "Action",
        "rating": 8.8,
        "year": 2010,
        "plot": "En tjuv som stjäl idéer genom drömmar."
    }

    
    assert movie.to_dict() == expected
    