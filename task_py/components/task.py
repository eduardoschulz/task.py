from textual import on
from textual.widgets import Button, Label, Static


class TaskWidget(Static):
    def compose(self):
        # with Horizontal():
        yield Button("Done", variant="success", id="btn-done", compact=True)
        yield Label("Tarefa1")

    """i think that's good """

    @on(Button.Pressed, "#btn-done")
    def set_as_done(self):
        self.remove()
