class OveloadError(Exception):
    pass

class NoItemError(Exception):
    pass

class PositionError(Exception):
    pass

class NoItemEquiptError(Exception):
    pass

class NoItemToEquiptError(Exception):
    pass

class TalkingError(Exception):
    pass


class FantasyCharacter:
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MAX_ITEMS = 10
    MIN_POS = 0
    MAX_POS = 999
    EQUIP_PREFIX = "equip with "
    STANY = {"idle", "moving", "attacking", "talking", "injured",
             "unconscious", "dead", "stunned", "hidden"}

    def __init__(self, name, health=100, inventory=None, position=(0, 0), states=None):
        if inventory is None:
            inventory = []
        if states is None:
            states = ["idle"]

        self.name = self._sprawdz_nazwe(name)
        self.health = self._sprawdz_zdrowie(health)

        if len(inventory) > self.MAX_ITEMS:
            raise OveloadError("max 10 przedmiotow w ekwipunku")
        self.inventory = list(inventory)  # kopia zeby nie zmieniac listy z zewnatrz

        self.position = self._sprawdz_pozycje(position)

        for stan in states:
            self._sprawdz_stan(stan, inventory)
        self.states = list(states)

    def _sprawdz_nazwe(self, name):
        # isalnum - tylko litery i cyfry
        if type(name) != str or not name.isalnum():
            raise ValueError("zla nazwa: " + str(name))
        return name

    def _sprawdz_zdrowie(self, health):
        if type(health) not in (int, float):
            raise TypeError("zdrowie musi byc liczba")
        if health < self.MIN_HEALTH or health > self.MAX_HEALTH:
            raise ValueError("zdrowie musi byc od 0 do 100")
        return health

    def _sprawdz_pozycje(self, position):
        if type(position) not in (tuple, list) or len(position) != 2:
            raise PositionError("pozycja ma byc w postaci (x, y)")
        x = position[0]
        y = position[1]
        if type(x) != int or type(y) != int:
            raise PositionError("x i y musza byc int")
        if x < self.MIN_POS or x > self.MAX_POS or y < self.MIN_POS or y > self.MAX_POS:
            raise PositionError("pozycja poza plansza (0-999)")
        return (x, y)

    def _sprawdz_stan(self, stan, inventory):
        if stan in self.STANY:
            return
        if type(stan) == str and stan.startswith(self.EQUIP_PREFIX):
            przedmiot = stan.replace(self.EQUIP_PREFIX, "", 1)
            if przedmiot not in inventory:
                raise NoItemError("nie ma " + przedmiot + " w ekwipunku")
            return
        raise ValueError("nieznany stan: " + str(stan))

    def _dodaj_stan(self, stan):
        # jak postac cos robi to juz nie jest idle
        if "idle" in self.states:
            self.states.remove("idle")
        if stan not in self.states:
            self.states.append(stan)

    def _zalozone_przedmioty(self):
        wynik = []
        for s in self.states:
            if s.startswith(self.EQUIP_PREFIX):
                wynik.append(s.replace(self.EQUIP_PREFIX, "", 1))
        return wynik

    def take(self, item):
        if len(self.inventory) >= self.MAX_ITEMS:
            raise OveloadError("ekwipunek pelny")
        self.inventory.append(item)

    def drop(self, item=None):
        if len(self.inventory) == 0:
            raise NoItemError("ekwipunek jest pusty")
        if item is None:
            item = self.inventory[-1]  # jak nie podano co wyrzucic to ostatni
        if item not in self.inventory:
            raise NoItemError("nie ma " + str(item) + " w ekwipunku")
        self.inventory.remove(item)

        # jak wyrzucamy zalozony przedmiot to trzeba go tez zdjac
        if item not in self.inventory and self.EQUIP_PREFIX + item in self.states:
            self.states.remove(self.EQUIP_PREFIX + item)
        return item

    def move(self, dx, dy):
        x, y = self.position
        self.position = self._sprawdz_pozycje((x + dx, y + dy))
        self._dodaj_stan("moving")

    def equip(self, item):
        if item not in self.inventory:
            raise NoItemError("nie ma " + str(item) + " w ekwipunku")
        self._dodaj_stan(self.EQUIP_PREFIX + item)

    def unequip(self, item):
        if self.EQUIP_PREFIX + item not in self.states:
            raise NoItemEquiptError(item + " nie jest zalozony")
        self.states.remove(self.EQUIP_PREFIX + item)

    def attack(self):
        if len(self._zalozone_przedmioty()) == 0:
            raise NoItemToEquiptError("nie ma czym atakowac")
        self._dodaj_stan("attacking")

    def hide(self):
        self._dodaj_stan("hidden")

    def talk(self):
        if "hidden" in self.states:
            raise TalkingError("ukryta postac nie moze gadac")
        self._dodaj_stan("talking")

    def show_status(self):
        status = {
            "name": self.name,
            "health": self.health,
            "inventory": list(self.inventory),
            "position": self.position,
            "state": list(self.states),
        }
        for k in status:
            print(k + ":", status[k])
        return status


if __name__ == "__main__":
    bohater = FantasyCharacter("Aragorn", 90, ["miecz", "tarcza"], (10, 20))
    bohater.equip("miecz")
    bohater.move(5, 5)
    bohater.attack()
    bohater.show_status()
