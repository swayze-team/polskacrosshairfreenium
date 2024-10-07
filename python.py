import sys
import requests
import pyautogui

def center_crosshair():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, screen_height // 2)

def update_config(crosshair_id):
    response = requests.get(f'http://localhost:8000/crosshair/{crosshair_id}')
    if response.status_code == 200:
        config = response.json()
        print(f"Configuration mise à jour: {config}")
        # Ici, vous pouvez utiliser la configuration pour mettre à jour l'affichage du crosshair
    else:
        print("Erreur lors de la récupération de la configuration")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crosshair.py [center|update] [crosshair_id]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "center":
        center_crosshair()
    elif command == "update":
        if len(sys.argv) < 3:
            print("Veuillez fournir l'ID du crosshair pour la mise à jour")
            sys.exit(1)
        update_config(sys.argv[2])
    else:
        print("Commande non reconnue")
