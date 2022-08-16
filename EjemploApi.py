# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:21:11 2021

@author: Asus
"""
from pprint import pprint
from urllib import response
import pandas as pd
import requests
import json
from tabulate import tabulate as tb

'''

if __name__=='__main__':
    url="https://pokeapi.co/api/v2/pokemon-form/"
    response= requests.get(url)
    if response.status_code==200:
        payload=response.json()
        results= payload.get("results",[])

        if results:
            for pokemon in results:
                name=pokemon['name']
data=requests.get(url).json()
results_list = [results_json for results_json in data['results']]
results_df = pd.DataFrame(results,columns=['name'])

'''

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:21:11 2021

@author: Asus
"""

'''
url="https://pokeapi.co/api/v2/pokemon/" 
params=params={'name':''}

response = requests.get(url, params=params)
dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
print(dictionary)

data=requests.get(url, params=params).json()
results_list = [results_json for results_json in data['results']]
results_df = pd.DataFrame(results_list,columns=['name'])
'''

url="https://pokeapi.co/api/v2/pokemon/" 
def pokemon(urlP=''):
    pokeData={
        'name':'',
        'height':'',
        'abilities':'',
        'types':'',
        'weight':''
    }
    response= requests.get(urlP).json()
    pokeData['name']=response['name']
    pokeData['height']=response['height']
    pokeData['abilities']=response['abilities']
    pokeData['types']=response['types']
    pokeData['weight']=response['weight']

    return pokeData

def main():
    pokemoName='butterfree' #butterfree , pikachu , charmander, El único pokémon que se puede obtener con el 
    #diccionario llamado lista3 es el butterfree
    pokeUrl=url+pokemoName
    data= pokemon(pokeUrl)
    print("\n")
    print("Nombre del pokemon:",pokemoName,"\n\n")
    pprint(data)
    print("\n\n\n")
    dataF=requests.get(pokeUrl,data=data).json()
    for data in dataF:
        #lista1={'Nombre':[dataF["name"]],'Altura':[dataF["height"]], 'Peso':[dataF["weight"]]}
        #lista2={'Nombre':[dataF["name"]],'Altura':[dataF["height"]], 'Peso':[dataF["weight"]], 'Habilidades':[dataF["abilities"]], 'Tipos':[dataF["types"]]}
        lista3={'Nombre':[dataF["name"]],'Altura':[dataF["height"]], 'Peso':[dataF["weight"]],
        'Habilidad 1':[dataF["abilities"][0]['ability']['name']],
        'Habilidad 2':[dataF["abilities"][1]['ability']['name']], 'Tipo':[dataF["types"][1]['type']['name']]}
    results_df = pd.DataFrame(lista3)
    print(tb(results_df, headers="keys",showindex="always", tablefmt="fancy_grid", stralign="center"))
    #print(results_df) #print para imprimir toda la lista 2 de cualquier pokémon




if __name__=='__main__':
    main()



                