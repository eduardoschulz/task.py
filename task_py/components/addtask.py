from textual.widgets import TextArea, Static, Input, Button
from textual import on


class AddTask(Static):
    def compose(self):
        yield Input(placeholder="Nova Tarefa", id="input-add")
        yield Button("Add Task", id="add-task")

    @on(Button.Pressed, '#add-task')
    def set_as_done(self):
        self.add_class("hidden")
        # menu = self.query_one("#addtask")
        # menu.add_class("hidden")
        # tl = self.query_one("#task-list")
        # tl.remove_class("hidden")

