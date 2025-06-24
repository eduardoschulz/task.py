def test_app_import():
    from task_py.app import TodoApp
    app = TodoApp()
    assert app is not None
