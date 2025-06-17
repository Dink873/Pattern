import csv
from faker import Faker
import random
from pathlib import Path

fake = Faker('en_US')
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def generate_test_data():
    with open(DATA_DIR / "users.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email"])
        for i in range(1, 201):
            writer.writerow([i, fake.name(), fake.email()])

    with open(DATA_DIR / "genres.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
        genres = ["Action", "RPG", "Indie", "Strategy", "Simulation"]
        for i, genre in enumerate(genres, 1):
            writer.writerow([i, genre])

    with open(DATA_DIR / "games.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "title", "description", "year", "genre_id"])
        for i in range(1, 301):
            writer.writerow([
                i,
                fake.sentence(nb_words=2),
                fake.text(max_nb_chars=100),
                random.randint(2000, 2024),
                random.randint(1, 5)
            ])

    with open(DATA_DIR / "playsessions.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "user_id", "game_id"])
        for i in range(1, 1001):
            writer.writerow([
                i,
                random.randint(1, 200),
                random.randint(1, 300)
            ])

    with open(DATA_DIR / "reviews.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "score", "comment", "user_id", "game_id"])
        for i in range(1, 801):
            writer.writerow([
                i,
                random.randint(1, 10),
                random.choice(["Great game", "Fun", "Mid", "Bad experience"]),
                random.randint(1, 200),
                random.randint(1, 300)
            ])

if __name__ == "__main__":
    generate_test_data()
    print("Test data generated in data/")
