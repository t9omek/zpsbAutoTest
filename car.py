class AccelerateError(ValueError):
    """Przyspieszenie samochodu jest zbyt małe."""


class EmptyFuelTankError(ValueError):
    """Bak jest pusty."""


class NoEnaughtFuelError(ValueError):
    """Paliwa jest za mało, aby przejechać zadany odcinek."""


class Samochod:
    def __init__(self, marka, wspolczynnik_spalania_na_100km, przyspieszenie_km_na_sekunde, pojemnosc_baku):
        self.marka = marka
        self.wspolczynnik_spalania_na_100km = wspolczynnik_spalania_na_100km  # litry na 100 km
        self.przyspieszenie_km_na_sekunde = przyspieszenie_km_na_sekunde  # km/s^2
        self.pojemnosc_baku = pojemnosc_baku  # litry
        self.poziom_paliwa = pojemnosc_baku  # litry
        self.predkosc = 0  # km/s

    def przyspiesz(self):
        minimalne_przyspieszenie = 0.1  # minimalne akceptowalne przyspieszenie
        if self.przyspieszenie_km_na_sekunde < minimalne_przyspieszenie:
            raise AccelerateError(f"Przyspieszenie zbyt małe: {self.przyspieszenie_km_na_sekunde} km/s^2")
        self.predkosc += self.przyspieszenie_km_na_sekunde

    def jedz(self, czas_w_sekundach):
        if self.poziom_paliwa == 0:
            raise EmptyFuelTankError("Bak jest pusty")
        dystans = self.predkosc * czas_w_sekundach  # km
        paliwo_potrzebne = (dystans / 100) * self.wspolczynnik_spalania_na_100km
        if paliwo_potrzebne > self.poziom_paliwa:
            raise NoEnaughtFuelError("Za mało paliwa, aby przejechać")
        self.poziom_paliwa -= paliwo_potrzebne
