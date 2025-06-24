from textual.app import App
from textual.containers import Vertical
# uso futuro from task_py.components.task import Task

class TodoApp(App):
    CSS_PATH = "task_py/styles/app.tcss"

    def compose(self):
        yield Vertical()

