# innloggingsprogram

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
        #her skal vi fylle inn logikk for å logge inn.
        print("du er nå logget inn")
        return "innlogget"
    elif valg == "2":
        # her skal vi fylle inn logikk for å registrere ny bruker.
        print("Ny bruker registrert")
        return "start"
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
    

main()