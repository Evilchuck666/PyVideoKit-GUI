from PySide6.QtCore import QThread, Signal


class Worker(QThread):
    progress = Signal(float)
    finished = Signal(object)
    error = Signal(str)

    def __init__(self, fn, args=(), kwargs=None):
        super().__init__()
        self._fn = fn
        self._args = args
        self._kwargs = dict(kwargs or {})
        self._kwargs["on_progress"] = self.progress.emit

    def run(self):
        try:
            result = self._fn(*self._args, **self._kwargs)
            self.finished.emit(result)
        except Exception as e:
            self.error.emit(str(e))
