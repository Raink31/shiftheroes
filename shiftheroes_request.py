import requests
import time

headers = {
    'Authorization': 'Bearer 577e9aec2586096664daebb486df09f9',
}


# Lister les plannings
liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()


# Détecter quand un nouveau planning est dispobible
while liste_initiale == nouvelle_liste:
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers).json()
    time.sleep(1)

print("Nouveau planning disponible!")


# Lister les creneaux avec la variable précédente
all_creneaux = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{nouvelle_liste[0]["id"]}/shifts', headers=headers).json()


# Reserver tous les creneaux
for item in all_creneaux :
    requests.post(f'https://shiftheroes.fr/api/v1/plannings/{nouvelle_liste[0]["id"]}/shifts/{item["id"]}/reservations', headers=headers)
