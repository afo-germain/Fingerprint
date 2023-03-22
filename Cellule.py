class Cellule():

    def __init__(self, tpr) -> None:
        self.tpr = tpr

    def somme(self) -> int:
        return abs(sum(self.tpr))