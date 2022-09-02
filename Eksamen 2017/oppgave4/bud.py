class Bud:
    def __init__(self,navn,budstorrelse):
        if budstorrelse < 0:
            self._budStr = 1
        self._budgiver = navn
        self._budStr = budstorrelse

    def __str__(self):
        streng = "Budgiver: " + self._budgiver + ", " + "Budstorrelse: " + str(self._budStr)
        return streng

    def hentBudgiver(self):
        return self._budgiver

    def hentBudStr(self):
        return self._budStr
