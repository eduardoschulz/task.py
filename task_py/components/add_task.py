from textual.widgets import TextArea, Static, Input, Button


class AddTask(Static):
    def compose(self):
        yield Input(placeholder="Nova Tarefa", id="input-add")
        yield Button("Add Task", id="add-task")
