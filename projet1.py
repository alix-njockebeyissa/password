MIN_LENGTH = 8
REQUIRE_DIGIT = True
REQUIRE_UPPER = True
REQUIRE_LOWER = True
while True:
    password = input("Choisissez un mot de passe : ")

    errors = []
    if len(password) < MIN_LENGTH:
        errors.append("Le mot de passe doit contenir au moins {} caractères.".format(MIN_LENGTH))
    if REQUIRE_DIGIT and not any(char.isdigit() for char in password):
        errors.append("Le mot de passe doit contenir au moins un chiffre.")
    if REQUIRE_UPPER and not any(char.isupper() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if REQUIRE_LOWER and not any(char.islower() for char in password):
        errors.append("Le mot de passe doit contenir au moins une lettre minuscule.")

    if not errors:
        print("Le mot de passe est sécurisé.")
        break

    else:
        print("Le mot de passe ne répond pas aux exigences de sécurité suivantes :")
        for error in errors:
            print("-", error)
        print("Veuillez choisir un nouveau mot de passe.")