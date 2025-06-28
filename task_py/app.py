from textual.app import App
from textual.containers import Vertical
from task_py.components.addtask import AddTask
from task_py.components.task import TaskWidget

# uso futuro from task_py.components.task import Task


class TodoApp(App):
    CSS_PATH = "styles/app.tcss"
    BINDINGS = [("a", "open_menu", "Open/Close Menu")]  # Added this line

    def compose(self):
        yield AddTask(id="addtask", classes="hidden")
        yield Vertical(
            TaskWidget(),
            TaskWidget(),
            TaskWidget(),
            TaskWidget(),
            id="task-list",
            classes="",
        )

    # TODO descobrir pq nao aparece/ ele ta chegando aq
    def action_open_menu(self):

        tasklist = self.query_one("#task-list")
        tasklist.add_class("hidden")
        menu = self.query_one("#addtask")
        menu.remove_class("hidden")

    # @on(Button.Pressed, "#input-add")
    # def setdone(self):
    #     self.query_one("#task-list")
