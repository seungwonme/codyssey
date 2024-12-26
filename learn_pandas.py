import pandas as pd

file_path = "./prob-0101/prob-0101.csv"
movies = pd.read_csv(file_path)


# Display the first few rows of the dataframe in a more readable format
actors = []
movies["출연진"].apply(lambda x: actors.extend(x.split(", ")))
for actor in actors:
    print(actor)
print(len(actors))
set_actors = set(actors)
print(len(set_actors))
