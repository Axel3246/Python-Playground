# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python server to interact with Unity
# Sergio. Julio 2021

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json


# Set the number of agents here:
# EN UNITY WIDTH = X, ¿HEIGHT = Z?


'''# Función para traducir las posicioens a un JSON
def positionsToJSON(ps):
    posDICT = []
    for p in ps:
        pos = {
            "x" : p[0],
            "z" : p[1],
            "y" : p[2]
        }
        json_string = json.dumps(p)
        # posDICT.append(pos)
        print(json_string)
   # return json.dumps(posDICT)


pos = [1, 2, 3]
positionsToJSON(pos)
'''
                                 #  x  y  z
my_dict_car = {"1": { "positions": [1, 0, 3]},
               "2": { "positions": [2, 0, 3]},
               "3": { "positions": [3, 0, 3]}
               }

a = {
"dict1": {"letter": "a", "code": "y", "position": 1},
"dict2": {"letter": "p", "code": "y", "position": 2},
"dict3": {"letter": "a", "code": "y", "position": 1}
}


print(my_dict_car)
