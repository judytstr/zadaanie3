num_of_packages = int(input("Ilość paczek do wysłania: "))

sent_packages = 0
sent_weight = 0
empty_weight = 0
max_empty_weight = 0
max_empty_package = 0

i = 0
while i < num_of_packages:
    weight = int(input(f"Podaj wagę paczki {i + 1} (od 1 do 10 kg): "))
    if weight >= 1 and weight <= 10:
        while sent_weight + weight > 20:
            sent_packages += 1
            empty_weight += 20 - sent_weight
            if 20 - sent_weight > max_empty_weight:
                max_empty_weight = 20 - sent_weight
                max_empty_package = sent_packages
            sent_weight = 0
        sent_weight += weight
        i += 1

sent_packages += 1
empty_weight += 20 - sent_weight

print("\nPodsumowanie:")
print(f"Wysłano {sent_packages} paczek")
print(f"Wysłano {sent_weight} kg")
print(f"Suma pustych kilogramów: {empty_weight} kg")
print(f"Najwięcej pustych kilogramów ma paczka {max_empty_package} ({max_empty_weight} kg)")
