import pandas as pd
import os
from enum import Enum
from typing import List


class MovieDataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.extension = os.path.splitext(file_path)[1]
        self.dataframe = None

    def load(self) -> pd.DataFrame:
        self.dataframe = pd.read_csv(
            self.file_path, sep="\t" if self.extension == ".txt" else ","
        )
        return self.dataframe


class DB(Enum):
    CASTINGS = 0
    COUNTRIES = 1
    GENRES = 2
    RATES = 3
    MOVIES = 4
    PEOPLES = 5


def get_dataframes() -> List[pd.DataFrame]:
    base_path = os.path.join(os.getcwd(), "data/kmrd/kmr_dataset/datafile/kmrd-small")
    db_name = [
        "castings.csv",
        "countries.csv",
        "genres.csv",
        "rates.csv",
        "movies.txt",
        "peoples.txt",
    ]
    db_paths = [os.path.join(base_path, name) for name in db_name]
    return [MovieDataLoader(path).load() for path in db_paths]


dataframes = get_dataframes()
castings_df = dataframes[DB.CASTINGS.value]
countries_df = dataframes[DB.COUNTRIES.value]
genres_df = dataframes[DB.GENRES.value]
rates_df = dataframes[DB.RATES.value]
movies_df = dataframes[DB.MOVIES.value]

print("===========================castings_df===========================")
print(castings_df.head())
print("===========================countries_df===========================")
print(countries_df.head())
print("===========================genres_df===========================")
print(genres_df.head())
print("===========================rates_df===========================")
print(rates_df.head())
print("===========================movies_df===========================")
print(movies_df.head())


merged_df = (
    movies_df.merge(castings_df, on="movie", how="left")
    .merge(countries_df, on="movie", how="left")
    .merge(genres_df, on="movie", how="left")
    .merge(rates_df[["movie", "rate", "user"]], on="movie", how="left")
)

# 필요한 컬럼만 선택하여 정리
final_df = merged_df[[
    "movie",
    "title",
    "year",
    "grade",
    "people",
    "leading",
    "country",
    "genre",
    "rate",
    "user",
]]

# print(len(final_df))

# # Merge 예제 (컬럼 기준)
# merged_df = movies_df.merge(castings_df, on="movie", how="left")

# # Join 예제 (인덱스 기준)
# joined_df = movies_df.set_index("movie").join(castings_df.set_index("movie"))

# print(merged_df.head())
# print(joined_df.head())

# cast_per_movie = castings_df.groupby("movie").size()
# print(cast_per_movie.mean())

merged_df = movies_df.merge(genres_df, on="movie", how="left")
print(merged_df.head())
