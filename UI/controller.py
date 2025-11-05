import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        musei = self._model.get_musei()
        self._view.dropdown_musei.options.clear()
        for id_museo, nome in musei:
            self._view.dropdown_musei.options.append(ft.dropdown.Option(key=id_museo, text=nome))

        self._view.update()




    # CALLBACKS DROPDOWN
    # TODO


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
