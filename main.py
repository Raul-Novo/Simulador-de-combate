import random
import time


class Personaje:
    """
    Clase base que representa un personaje en el combate.

    Atributos:
        nombre (str): Nombre del personaje.
        vida (int): Puntos de vida del personaje.
        ataque (int): Puntos de ataque base.
        defensa (int): Puntos de defensa base.
    """

    def __init__(self, nombre: str, vida: int, ataque: int, defensa: int) -> None:
        self.nombre: str = nombre
        self.vida: int = vida
        self.ataque: int = ataque
        self.defensa: int = defensa

    def atacar(self, enemigo: "Personaje") -> None:
        """
        Realiza un ataque a otro personaje, calculando el daño final.

        Args:
            enemigo (Personaje): El objetivo del ataque.
        """
        daño: int = random.randint(self.ataque - 2, self.ataque + 2)
        daño_final: int = max(0, daño - enemigo.defensa)
        enemigo.vida -= daño_final
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {daño_final} de daño.")

    def esta_vivo(self) -> bool:
        """Indica si el personaje sigue con vida."""
        return self.vida > 0


class Guerrero(Personaje):
    """Clase que representa un Guerrero, enfocado en resistencia."""

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre, vida=50, ataque=10, defensa=5)


class Mago(Personaje):
    """Clase que representa un Mago, enfocado en ataque y curación."""

    def __init__(self, nombre: str) -> None:
        super().__init__(nombre, vida=40, ataque=12, defensa=3)

    def curar(self) -> None:
        """Cura una cantidad aleatoria de vida."""
        cura: int = random.randint(5, 10)
        self.vida += cura
        print(f"{self.nombre} se cura {cura} puntos de vida.")


def combate(jugador1: Personaje, jugador2: Personaje) -> None:
    """
    Simula un combate entre dos personajes por turnos.

    Args:
        jugador1 (Personaje): Primer combatiente.
        jugador2 (Personaje): Segundo combatiente.
    """
    print("¡Comienza el combate!\n")
    time.sleep(1)

    while jugador1.esta_vivo() and jugador2.esta_vivo():
        jugador1.atacar(jugador2)
        if not jugador2.esta_vivo():
            break

        # El mago tiene un 30% de probabilidad de curarse antes de atacar
        if isinstance(jugador2, Mago) and random.random() < 0.3:
            jugador2.curar()
        else:
            jugador2.atacar(jugador1)

        print(f"{jugador1.nombre}: {jugador1.vida} de vida | {jugador2.nombre}: {jugador2.vida} de vida\n")
        time.sleep(1)

    ganador: Personaje = jugador1 if jugador1.esta_vivo() else jugador2
    print(f"¡{ganador.nombre} gana el combate!")


if __name__ == "__main__":
    jugador1: Guerrero = Guerrero("Thorin")
    jugador2: Mago = Mago("Gandalf")
    combate(jugador1, jugador2)
