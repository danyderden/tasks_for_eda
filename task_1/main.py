import json
import random


class RandomCity:

    def __init__(self, route):
        self.route: str = route
        self.cities: dict = self._load_cities()

    def _load_cities(self) -> [dict]:
        with open(self.route, 'r') as file:
            cities = json.load(file)
        return cities

    def get_random_city(self) -> str:
        total_population = sum(c['population'] for c in self.cities)
        random_probability = random.random()
        for city in self.cities:
            if city['population'] / total_population >= random_probability:
                return city['name']
        return self.get_random_city()
