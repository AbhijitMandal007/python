import importlib

db = importlib.import_module("19b")
ui = importlib.import_module("19c")

db.setup()
ui.start()