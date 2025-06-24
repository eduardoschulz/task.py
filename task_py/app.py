from textual.app import App
from textual.containers import Vertical
from task_py.components.task import TaskWidget

# uso futuro from task_py.components.task import Task


class TodoApp(App):
    CSS_PATH = "styles/app.tcss"

    def compose(self):
        with Vertical():
            yield TaskWidget()
            yield TaskWidget()
            yield TaskWidget()
            yield TaskWidget()
