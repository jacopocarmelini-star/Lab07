import flet as ft

from UI.alert import AlertManager
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
    def popola_dropdown_musei(self):
        musei = self._model.get_musei()
        self._view.dropdown_musei.options.clear()
        self._view.dropdown_musei.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))
        for museo in musei:
            self._view.dropdown_musei.options.append(ft.dropdown.Option(key=museo.id, text=museo.nome))

        self._view.update()

    def popola_dropdown_epoche(self):
        epoche = self._model.get_epoche()
        self._view.dropdown_epoche.options.clear()
        self._view.dropdown_epoche.options.append(ft.dropdown.Option(key="", text="Nessun filtro"))

        for epoca in epoche:
            self._view.dropdown_epoche.options.append(ft.dropdown.Option(key=epoca, text=epoca))

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def on_museo_selected(self, e):
        self.museo_selezionato = e.control.value

    def on_epoca_selected(self, e):
        self.epoca_selezionata = e.control.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self, e):
        museo = self.museo_selezionato
        epoca = self.epoca_selezionata

        if museo == "Nessun filtro":
            museo = None
        if epoca == "Nessun filtro":
            epoca = None

        artefatti = self._model.get_artefatti_filtrati(museo, epoca)
        self._view.mostra_lista_artefatti.controls.clear()

        if not self.museo_selezionato or not self.epoca_selezionata:
            self._view.show_alert("Seleziona entrambi i filtri.")
            return
        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato.")
        else:
            for artefatto in artefatti:
                self._view.mostra_lista_artefatti.controls.append(
                    ft.Text(f"{artefatto.id} | {artefatto.nome} | {artefatto.tipologia} | {artefatto.epoca}"))

        self._view.update()
