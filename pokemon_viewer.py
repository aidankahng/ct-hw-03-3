from poke_wrapper import PokeAPI
    
def main():
    print("Welcome to your pokedex!\nI can tell you information about pokemon.\n")
    pokedex = PokeAPI()
    while True:
        running = input("Would you like to see info on a pokemon (y/n)? ").lower()
        if running == 'n':
            break
        elif running == 'y':
            pokemon = input("What pokemon are you interested in? ").lower()
            if pokemon:
                poke = pokedex.lookup(pokemon)
                if poke:
                    print(poke)
main()