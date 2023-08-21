from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def get_valid_movie(movie: dict):
        rate = movie.get("rating_kinopoisk")
        num_of_countries = movie.get("country", "").count(",") + 1
        if (num_of_countries >= 2) and (rate != "0" and rate != ""):
            return movie

    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        valid_movies = list(filter(MapExercise.get_valid_movie, list_of_movies))
        ratings = list(map(lambda movie: float(movie["rating_kinopoisk"]), valid_movies))
        total_rate = sum(ratings)
        total_amount = len(ratings)
        average_rate = total_rate / total_amount
        return average_rate

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def count_char_in_name(movie: dict):
            movie_rate = movie["rating_kinopoisk"]
            if movie_rate != "" and float(movie_rate) >= rating:
                return movie["name"].count("и")

        filtered_movies = filter(None, map(count_char_in_name, list_of_movies))
        return sum(filtered_movies)
