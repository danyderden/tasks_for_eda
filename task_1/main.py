import json
import random


class RandomCity:

    def __init__(self, file_path) -> None:
        self.file_path: str = file_path
        self.cities: [dict] = self._load_cities()
        self.total_population = sum(c['population'] for c in self.cities)


    def _load_cities(self) -> [dict]:
        with open(self.file_path, 'r') as file:
            cities = json.load(file)
        return cities

    def get_random_city(self) -> str:
        random_probability = random.random()
        for city in self.cities:
            if city['population'] / self.total_population >= random_probability:
                return city['name']
        return self.get_random_city()
