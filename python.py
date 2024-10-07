import sys
import requests
import pyautogui
import time

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

def main(crosshair_id):
    print(f"Utilisation du crosshair ID: {crosshair_id}")
    while True:
        print("\n[1] - Centrer Le Crosshair")
        print("[2] - Mettre À Jour La Configuration")
        print("[3] - Déconnecter")
        choice = input("Entrez Le Numéro d'Option : ")

        if choice == "1":
            center_crosshair()
        elif choice == "2":
            update_config(crosshair_id)
        elif choice == "3":
            print("Déconnexion...")
            break
        else:
            print("Option invalide. Veuillez réessayer.")
        
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crosshair.py [crosshair_id]")
        sys.exit(1)

    crosshair_id = sys.argv[1]
    main(crosshair_id)
