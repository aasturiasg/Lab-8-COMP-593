from requests import get

def retrieve_pokemon_data(pokemon_name):

    print('Getting Pokemon data from PokeAPI...')

    #make sure the input is valid
    pokemon_name = pokemon_name.strip().lower()
    if pokemon_name == '':
        return None

    #establish a connection and get all the iformation for a pokemon
    request_response = get('https://pokeapi.co/api/v2/pokemon/' + str(pokemon_name))

    #verify the request status
    if request_response.status_code == 200:
        print('Request successful, data for ' + pokemon_name + ' gathered.')
        return request_response.json()
    elif request_response.status_code == 404:
        print('Unable to establish connection: ' + str(request_response.status_code) + "\nMake sure to input a valid pokemon name/number.")
        return None
    else:
        print('Unable to establish connection: ' + str(request_response.status_code) + ".")
        return None