# Warehouse
warehouse = {}
# Transaction history
actions = []
# Initialize balance
balance = 0

# Main loop
while True:
    print("\nDostępne komendy: saldo, sprzedaż, zakup, konto, lista, magazyn, przegląd, koniec")
    command = input("Podaj komendę: ").lower()

    # Command execution
    if command == 'saldo':
        amount = float(input("Podaj kwotę do dodania lub odjęcia z konta: "))
        balance += amount
        actions.append(('saldo', amount))
    elif command == 'sprzedaż':
        name = input("Podaj nazwę produktu: ")
        if name not in warehouse:
            print("Produkt nie istnieje w magazynie!")
            continue

        price = float(input("Podaj cenę produktu: "))
        quantity = int(input("Podaj liczbę sztuk: "))
        product = warehouse[name]
        if product['quantity'] < quantity:
            print("Brak wystarczającej liczby sztuk w magazynie!")
            continue

        total_price = price * quantity
        product['quantity'] -= quantity
        balance += total_price
        actions.append(('sprzedaż', name, price, quantity))
    elif command == 'zakup':
        name = input("Podaj nazwę produktu: ")
        price = float(input("Podaj cenę produktu: "))
        if price < 0:
            print("Nie można wykonać operacji")
            continue
        quantity = int(input("Podaj liczbę sztuk: "))

        if price * quantity > balance:
            print("Brak wystarczających środków na koncie!")
            continue

        if name in warehouse:
            warehouse[name]['quantity'] += quantity
        else:
            warehouse[name] = {'price': price, 'quantity': quantity}

        total_price = price * quantity
        balance -= total_price
        actions.append(('zakup', name, price, quantity))
    elif command == 'konto':
        print("Stan konta: ", balance)
    elif command == 'lista':
        print("Stan magazynu:")
        for product, details in warehouse.items():
            print(f"Produkt: {product}, Cena: {details['price']}, Ilość: {details['quantity']}")
    elif command == 'magazyn':
        name = input("Podaj nazwę produktu: ")
        product = warehouse.get(name)
        if product:
            print(f"Stan magazynu dla produktu {name}: Cena: {product['price']}, Ilość: {product['quantity']}")
        else:
            print("Produkt nie istnieje w magazynie!")
    elif command == 'przegląd':
        start = input("Podaj indeks początkowy (od 0) lub zostaw puste dla początku: ")
        end = input(f"Podaj indeks końcowy (max {len(actions)-1}) lub zostaw puste dla końca: ")

        try:
            if start == '':
                start = 0
            else:
                start = int(start)
            if end == '':
                end = len(actions) - 1
            else:
                end = int(end)

            if start < 0 or end >= len(actions):
                print(f"Podano nieprawidłowy zakres, dostępne indeksy od 0 do {len(actions)-1}")
                continue

            print("Historia operacji:")
            for i in range(start, end + 1):
                print(actions[i])
        except ValueError:
            print("Podano nieprawidłowy zakres!")
    elif command == 'koniec':
        print("Koniec działania programu.")
        break
    else:
        print("Nieprawidłowa komenda!")
