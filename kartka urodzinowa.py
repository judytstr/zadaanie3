print("Witaj w programie generującym kartki urodzinowe!")
name1=str(input("Wprowadź imię solenizanta: \n")).capitalize()
year=int(input(f"Wprowadź rok urodzenia {name1}: \n"))
msg=str(input(f"Wprowadź spersonalizowaną wiadomość dla {name1}: \n")).capitalize()
name2=str(input("Wprowadź swoje imię \n")).capitalize()
e=2024
f=e-year
print(f"{name1} wszystkiego najlepszego z okazji {f} urodzin!\n{msg}\n{name2}")




