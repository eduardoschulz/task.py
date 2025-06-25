from textual.app import App
from textual.containers import Vertical, Middle, Container
from task_py.components.addtask import AddTask
from task_py.components.task import TaskWidget
from textual.widgets import Footer

# uso futuro from task_py.components.task import Task


class TodoApp(App):
    CSS_PATH = "styles/app.tcss"
    BINDINGS = [
        ("o", "open_menu", "Open/Close Menu") # Added this line
    ]
    def compose(self):
        yield AddTask(id="addtask", classes="hidden")
        yield Vertical(
            TaskWidget(), TaskWidget(), TaskWidget(), TaskWidget(),
            id="task-list"
        )

    #TODO descobrir pq nao aparece/ ele ta chegando aq
    def action_open_menu(self): 
        menu = self.query_one("#addtask")
        menu.remove_class("hidden")
        self.bell()

    def on_mount(self) -> None:
        self.query_one(Vertical).focus()

