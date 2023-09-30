class Title:
    def __init__(self, x: int, y: int, title: str):
        self.x = x
        self.y = y
        self.title = title
        self.appearance = True

    def hide(self):
        self.appearance = False

    def show(self):
        self.appearance = True

    def print_status(self):
        print(f"Дані про віджет\n{self.title} {self.x} {self.y} {self.appearance}")


main_title = Title(150, 50, "Дізнатись переможця можна прямо зараз!")
rules_title = Title(150, 50, "Переможець може бути тільки один!")
main_title.print_status()
rules_title.print_status()
rules_title.hide()
