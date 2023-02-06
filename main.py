import random
from colorama import Fore, Back, Style 
print(f"{Fore.CYAN}Teksts{Style.RESET_ALL}")

vardi = ["viens", "divi", "tris", "cits"]

while True:
    vards = random.choice(vardi)
    minetaisVards = list("_" for _ in vards)
    dzivibas = 5

    print(vards)

    while dzivibas > 0 and not "".join(minetaisVards) == vards:
        inp = input(f"Ievade ({len(vards)} burti): ")
        if len(inp) != len(vards): continue
        # TODO: garuma pārbaude

        minetaisVards = list("_" for _ in vards)
        for iii in range(0, len(vards)):
            if vards[iii] == inp[iii]:
                print(f"{Back.GREEN}{inp[iii]}{Style.RESET_ALL}", end="")
                minetaisVards[iii] = inp[iii]
            elif inp[iii] in vards:
                print(f"{Back.YELLOW}{inp[iii]}{Style.RESET_ALL}", end="")
            else: 
                print(f"{inp[iii]}", end="")
        print()
        dzivibas -= 1
        print(f"Dzivibas: {dzivibas}")
        print("".join(minetaisVards))

    if dzivibas == 0:
        print("Jūs zaudējāt")
    else:
        print("Jūs uzvarējāt")

    if not input("Vai turpināt? J/N: ")[0].lower() == "j":
        break