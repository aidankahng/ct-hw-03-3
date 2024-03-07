from poke_wrapper import PokeAPI
import pyttsx3
    
def main():

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
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
                    engine.say(str(poke))
                    engine.runAndWait()
                    print(poke)
main()