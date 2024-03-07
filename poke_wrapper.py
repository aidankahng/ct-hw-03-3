import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

class Pokemon:
    def __init__(self, pokedata):
        self.data = pokedata[0]
        self.id = self.data['id']
        self.name = self.data['name']
        self.height = self.data['height']
        self.weight = self.data['weight']
        self.sprite = self.data['sprites']['front_default']
        self.flavor = 'No description yet'
        for entry in pokedata[1]['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                self.flavor = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')

    def __str__(self):
        ret_str = f"""
Here is some info about {self.name}!
Id: {self.id}
Height: {self.height * 0.1:.1f} meters
Weight: {self.weight * 0.1:.1f} kilograms
Description: {self.flavor}
"""
        return ret_str
    

class PokeAPI:
    base_url = "https://pokeapi.co/api/v2/pokemon"

    def __init__(self):
        pass

    def __get(self, pokemon):
        request_url = f"{self.base_url}/{pokemon}"
        response = requests.get(request_url)
        species_url = f"{self.base_url}-species/{pokemon}"
        response2 = requests.get(species_url)
        if response and response2:
            pokedata = [response.json(), response2.json()]
            return pokedata
        else:
            print(f'Could not retrieve data from {request_url}')
    
    def lookup(self, pokemon_name):
        pokedata = self.__get(pokemon_name)
        if pokedata:
            poke_obj = Pokemon(pokedata)
            return poke_obj
        else:
            print(f"I don't know of any pokemon called {pokemon_name}")