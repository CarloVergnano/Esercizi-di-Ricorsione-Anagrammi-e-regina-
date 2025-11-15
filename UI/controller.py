import flet as ft

class Controller:
    def __init__(self, view, model, dao):
        self._view = view
        self._model = model
        self._dao = dao

    def calcola_anagrammi(self, e):
        parola = self._view.txt_word.value

        if parola == "":
            self._view.create_alert("Inserisci una parola")
            return

        anagrammi = self._model.calcola_anagrammi(parola)

        # Svuoto la GUI prima di ricaricare i risultati
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()

        for anagramma in anagrammi:
            if self._dao.parola_valida(anagramma):
                self._view.lst_correct.controls.append(ft.Text(anagramma))
            else:
                self._view.lst_wrong.controls.append(ft.Text(anagramma))

        self._view.update_page()

    def reset(self, e):
        self._view.lst_correct.controls.clear()
        self._view.lst_wrong.controls.clear()
        self._view.txt_word.value = ""
        self._view.update_page()
