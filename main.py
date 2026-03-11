#!/usr/bin/env python3
import subprocess
import yaml

# === Cargar perfiles desde YAML ===
import os

def load_profiles():
    for path in ["profiles.yaml", "profile.yaml"]:
        if os.path.exists(path):
            with open(path, "r") as f:
                return yaml.safe_load(f)["profiles"]
    raise FileNotFoundError("No profiles.yaml or profile.yaml found")


# === Ejecutar comando externo ===
def run_command(command):
    print(f"\n[+] Ejecutando: {command}\n")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Error:", result.stderr)
    except Exception as e:
        print("Excepción:", e)

############################################## PERFILES DE CONFIG

###############################################
print("""
      ⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤
⣿⡿⢯⡉⠱⢾⣇⣶⠋⣀⠾⢁⡰⠞⠁⢰⠋⠉⠀⣀⠾⠉⢀⡰⠞⠁
⣿⢧⡈⢱⣶⡎⠉⣿⠶⠿⢶⣸⡇⠀⢀⡼⠄⠀⣀⠿⠀⢰⡎⠁⠀⠀
⣿⠚⢳⡎⠉⢱⣶⠉⠀⠀⣴⠛⠓⢲⣾⡇⡄⠀⣿⠀⠀⢸⡇⠀⠀⠀
⣿⣀⣸⣇⡰⠎⠉⠶⣀⣶⠉⢀⡰⠎⠉⠉⠉⣶⣿⣀⣀⣸⡇⠀⠀⠀
⣿⠉⢉⣹⡇⠀⣀⠶⠿⠿⣀⢸⡇⠀⠀⢀⠶⠉⠉⠉⣹⠿⠷⠆⠀⠀  Brafuzz by Bravo Agustin
⣿⠒⠚⠙⢳⣶⡃⠀⠀⠀⣼⣾⡇⠀⠀⢸⠀⠀⠀⣤⠓⠀⠀⠀- For CTFs and ethics audits only -
⣿⢠⣤⣤⣤⣼⡅⠀⣤⠛⠀⠀⠘⢣⡄⢸⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⣿⠓⠀⠀⠀⠘⢻⣿⠀⠀⠀⣰⠤⠤⠼⠿⣀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⣿⡰⠶⠶⠶⠶⣏⣿⠀⣀⠶⠁⠀⠀⠀⠀⠉⠶⣀⣿⠀⠀⠀⠀⠀ [1] Simple Web Scann
⣿⠉⠀⠀⠀⠀⠈⠿⣶⠉⠀⠀⠀⠀⢀⣠⣤⣀⣍⣿⣀⠀⠀⠀⠀⠀[2] Fuzzing with wordlists Personalized
⣿⠀⢀⣀⣀⣀⡀⠀⠿⣀⠀⢀⡸⠿⠟⠀⠀⠀⠀⠀⠸⠄⠀⠀⠀⠀[3] Advanced Fuzzing Techniques
⣿⡰⠾⠉⠉⠉⠳⠶⣀⣿⣀⡎⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀[4] Custom Payloads
⣿⠉⠀⠀⠀⠀⠀⠀⠉⠉⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ [5] Info
⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
      """)
print("--------------------------------------------------------------")
print("Select an option >>> ")

profiles = load_profiles()
op = input()

if op in ["1","2","3","4"]:
    selected_profile = profiles[int(op)-1]
    print(f"\n--- {selected_profile['name']} ---")
    for idx, option in enumerate(selected_profile["options"], start=1):
        print(f"[{idx}] {option['description']}")
    subchoice = input("Selecciona un tipo de fuzzing >>> ").strip()

    if subchoice.isdigit() and 1 <= int(subchoice) <= len(selected_profile["options"]):
        target = input("Ingresa la URL objetivo >>> ").strip()
        chosen = selected_profile["options"][int(subchoice)-1]
        command = chosen["command"].replace("{target}", target)
        run_command(command)
    else:
        print("Subopción inválida")

elif op == "5":
    print("Script Created by Bravo Alberto Agustin | @Bravxo")
    print("GitHub: https://github.com/Bravxo")
    print("Contribuye con el proyecto ampliando las wordlists o nuevos directorios 🙌")
