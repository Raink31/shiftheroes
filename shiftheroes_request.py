import requests

headers = {
    'Authorization': 'Bearer 577e9aec2586096664daebb486df09f9',
}

# Lister les plannings
response = requests.get('https://shiftheroes.fr/api/v1/plannings', headers=headers)

# Lister les creneaux
response = requests.get('https://shiftheroes.fr/api/v1/plannings/rwf10y/shifts', headers=headers)

# Reserver un creneau
response = requests.post('https://shiftheroes.fr/api/v1/plannings/rwf10y/shifts/D6FKomo/reservations', headers=headers)