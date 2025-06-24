from textual.widgets import Button, Label, Static


class TaskWidget(Static):
    def compose(self):
        yield Button("Done", variant="success")
        yield Label("Tarefa1")
