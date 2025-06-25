from textual.app import App
from textual.containers import Vertical, Middle, Container
from task_py.components.add_task import AddTask
from task_py.components.task import TaskWidget
from textual.widgets import Footer

# uso futuro from task_py.components.task import Task


class TodoApp(App):
    CSS_PATH = "styles/app.tcss"
    BINDINGS = [
        ("b", "ring_bell", "ring"),
        ("o", "openmenu", "Open/Close Menu") # Added this line
    ]
     
    
    def action_ring_bell(self):
        self.bell()


    

    def compose(self):
        yield AddTask(id="addtask", classes="hidden")
        yield Vertical(
            TaskWidget(), TaskWidget(), TaskWidget(), TaskWidget(),
            id="task-list"
        )

    def action_openmenu(self):
        menu = self.query_one("#addtask")
        menu.toggle_class("hidden")

    def on_mount(self) -> None:
        self.query_one(Vertical).focus()

