# innloggingsprogram

users = [{"userName": "admin", "password": "123"}]

def main():
    state = "start"
    while state != "quit":
        if state == "start":
            state = vis_startmeny()
        elif state == "innlogget":
            state = vis_inlogget_meny()

def vis_startmeny():
    print("\n=== STARTMENY ====")
    print("1) Logg inn")
    print("2) Registrer ny bruker")
    print("3) Avslutt")
    valg = input("Hva ønsker du å gjøre? ")
    if valg == "1":
        return login()
    elif valg == "2":
        # her skal vi fylle inn logikk for å registrere ny bruker.
        return registrer()
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
    

def vis_inlogget_meny():
    print("\n=== MENY (innlogget) ===")
    print("1) Fortell en random vits")
    print("2) Logg ut")
    print("3) Avslutt")
    valg = input("Hva ønsker du å gjøre? ")
    if valg == "1":
        #her skal vi fylle inn logikk for p vise en random vits.
        return "innlogget"
    elif valg == "2":
        #her skal vi fylle inn logikk for å logge bruker ut.
        print("Du er logget ut.")
        return "start"
    elif valg == "3":
        return "quit"
    else:
        print("Ugyldig valg, prøv igjen.")
        return "innlogget"


def login():
    print("\n=== Log inn ===")
    b = input("brukernavn: ")
    p = input("passord: ")
    for user in users:
        if b == user["userName"] and  p == user["password"]:
            print("du er nå logget inn")
            return "innlogget"
    
    print("Feil brukernavn eller passord..")
    return "start"

def registrer():
    print("\n=== registrer ny bruker ===")
    b = ""

    while b == "":
        b = input("brukernavn: ")
        for user in users:
            if user["userName"] == b:
                print("brukernavn er opptatt")
                b = ""
    p = ""
    p2 = ""
    while len(p) < 3:
        p = input("passord: ")
        if len(p) < 3:
            print("passord må være minst 3 tegn..")
    
    while p != p2:
        p2 = input("re-type passord: ")
        if p != p2:
            print("passord matcher ikke..")
    
    users.append({"userName": b, "password": p})

    print(f"ny bruker ({b}) registrert")
    return "start"

main()