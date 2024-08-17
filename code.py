import requests
from requests.auth import HTTPBasicAuth

# Remplacez ces variables par vos informations
GITHUB_USERNAME = ''
GITHUB_TOKEN = ''
REPO_NAME = 'exam-DIT'

# URL pour créer un dépôt
create_repo_url = f'https://api.github.com/user/repos'
repo_data = {
    "name": REPO_NAME,
    "description": "Un dépôt créé via l'API REST de GitHub",
    "private": False
}

# Créer le dépôt
response = requests.post(create_repo_url, json=repo_data, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
if response.status_code == 201:
    print(f'Dépôt {REPO_NAME} créé avec succès.')
else:
    print(f'Erreur lors de la création du dépôt: {response.json()}')

# URL pour ajouter un ticket
issues_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/issues'
issue_data_1 = {
    "title": "Ticket 1",
    "body": "Ceci est le premier ticket."
}

issue_data_2 = {
    "title": "Ticket 2",
    "body": "Ceci est le deuxième ticket."
}

# Ajouter les tickets
response_1 = requests.post(issues_url, json=issue_data_1, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))
response_2 = requests.post(issues_url, json=issue_data_2, auth=HTTPBasicAuth(GITHUB_USERNAME, GITHUB_TOKEN))

if response_1.status_code == 201 and response_2.status_code == 201:
    print('Tickets ajoutés avec succès.')
else:
    print(f'Erreur lors de l\'ajout des tickets: {response_1.json()}, {response_2.json()}')
