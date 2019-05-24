class Motor:
    def __init__(self, potencia, cilindrada, combustivel):
        self._potencia = potencia
        self._cilindrada = cilindrada
        self._combustivel = combustivel

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia

    def getCilindrada(self):
        return self._cilindrada

    def setCilindrada(self, cilindrada):
        self._cilindrada = cilindrada

    def getCombustivel(self):
        return self._combustivel

    def setCombutivel(self, combustivel):
        self._combustivel = combustivel