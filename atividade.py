import flet as ft

class Contador(ft.Column):  
    def __init__(self):
        super().__init__(alignment=ft.MainAxisAlignment.CENTER)
  
        self.entrada = ft.TextField(label="Digite algo", width=200) 
        self.botao_acao = ft.ElevatedButton("Mostrar Texto", on_click=self.mostrar_texto, bgcolor=ft.colors.WHITE, color=ft.colors.WHITE)
        self.resultado = ft.Text("", size=16, color=ft.colors.BLACK)
        
        self.controls = [
            self.entrada,
            self.botao_acao,
            self.resultado
         ]

    def mostrar_texto(self, e):
        self.resultado.value = (f"Você digitou: {self.entrada.value}")
        self.update()


def main(page: ft.Page):
    page.title = "Contador e Entrada de Texto"  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(Contador())  
    page.update()

ft.app(main)
