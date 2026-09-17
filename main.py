from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculadoraApp(App):

  def build(self):
    self.title = "Calculadora"
    layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

    self.pantalla = TextInput(
        font_size=40, readonly=True, halign="right", multiline=False
    )
    layout.add_widget(self.pantalla)

    botones = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"],
    ]

    for fila in botones:
      h_layout = BoxLayout(spacing=10)
      for label in fila:
        boton = Button(text=label, font_size=32)
        boton.bind(on_press=self.on_button_press)
        h_layout.add_widget(boton)
      layout.add_widget(h_layout)

    return layout

  def on_button_press(self, instance):
    texto_actual = self.pantalla.text
    texto_boton = instance.text

    if texto_boton == "C":
      self.pantalla.text = ""
    elif texto_boton == "=":
      try:
        resultado = str(eval(texto_actual))
        self.pantalla.text = resultado
      except Exception:
        self.pantalla.text = "Error"
    else:
      self.pantalla.text = texto_actual + texto_boton


if __name__ == "__main__":
  CalculadoraApp().run()