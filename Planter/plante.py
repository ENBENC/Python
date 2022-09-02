class  Plante:
    def __init__(self,vannbeholder,maksgrenseVann):
        self._vannbeholder = vannbeholder
        self._maksgrenseVann = maksgrenseVann
        self._status = True #True betyr planten er levende, False betyr planten er doed.

    def vannPlante(self,vannCl):
        self._vannbeholder += vannCl
        if self._vannbeholder > self._maksgrenseVann:
            self._status = False

    def nyDag(self):
        self._vannbeholder -= 20
        if self._vannbeholder < 0:
            self._status = False

    def levende(self):
        return self._status
