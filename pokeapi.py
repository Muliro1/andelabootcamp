import requests
#this code snippet makes a simple get request to pokeapi and returns the status code
def get_status_code(): 
    response = requests.get(http://beta.pokeapi.co/docsv2/pokeapi.co/api/v2//)
    return response.status_code
    
