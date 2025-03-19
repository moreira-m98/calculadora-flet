import flet as ft
from Styles.styles import style_clear, style_numbers, style_operators, style_equal

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor =  "#2d2d2d"
    page.window.width = 350
    page.window.height = 460

    all_values = ""

    result_text = ft.Text(value="0", size=28, color="white")

    def enter_values(e):
        nonlocal all_values
        all_values += str(e.control.text)
        result_text.value = all_values
        page.update()

    def clear_display(e):
        nonlocal all_values
        all_values = ""
        result_text.value = "0"
        page.update()

    def backspace(e):
        nonlocal all_values
        all_values = all_values[:-1]
        result_text.value = all_values if all_values else '0'
        page.update()

    def calculate(e):
        nonlocal all_values
        try:
            result_text.value=str(eval(all_values))
            all_values = result_text.value
        except:
            result_text.value = "Error"
            all_values = ""
        page.update()


    display = ft.Container(
        content = result_text,
        bgcolor="#37474f",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right
    )


    grid_buttons = [
        [
            ("C", style_clear, clear_display),
            ("%", style_operators, enter_values),
            ("/", style_operators, enter_values),
            ("*", style_operators, enter_values),
        ],
        [
            ("7", style_numbers, enter_values),
            ("8", style_numbers, enter_values),
            ("9", style_numbers, enter_values),
            ("-", style_operators, enter_values),
        ],
        [
            ("4", style_numbers, enter_values),
            ("5", style_numbers, enter_values),
            ("6", style_numbers, enter_values),
            ("+", style_operators, enter_values),
        ],
        [
            ("1", style_numbers, enter_values),
            ("2", style_numbers, enter_values),
            ("3", style_numbers, enter_values),
            ("=", style_equal, calculate),
        ],
        [
            ("0", {**style_numbers, "expand":2}, enter_values),
            (".", style_numbers, enter_values),
            ("⌫", style_operators, backspace)
        ],
    ]

    buttons = []

    for row in grid_buttons:
        row_buttons = []
        for text, style, handler in row:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0
                )
            )
            row_buttons.append(btn)
        buttons.append(ft.Row(row_buttons, spacing=5))

    page.add(
        ft.Column(
            [
                display,
                ft.Column(buttons, spacing=5)
            ]
        )
    )

ft.app(target=main)