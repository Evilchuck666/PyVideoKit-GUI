from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pyvideokit_gui._worker import Worker

_VIDEO_FILTER = "Video files (*.mkv *.mp4 *.mov *.avi *.webm);;All files (*)"


class BasePanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._worker = None
        root = QVBoxLayout(self)
        root.setAlignment(Qt.AlignTop)
        root.setSpacing(10)
        root.setContentsMargins(20, 20, 20, 20)
        self._build_ui(root)
        root.addStretch()
        self._build_run_section(root)

    def _build_ui(self, layout: QVBoxLayout):
        raise NotImplementedError

    def _run(self):
        raise NotImplementedError

    # ── file picker helpers ───────────────────────────────────────────────

    def _input_row(self, layout, label="Input file", filter=_VIDEO_FILTER) -> QLineEdit:
        layout.addWidget(QLabel(label))
        row = QHBoxLayout()
        le = QLineEdit()
        le.setPlaceholderText("Select a file…")
        btn = QPushButton("Browse…")
        row.addWidget(le)
        row.addWidget(btn)
        layout.addLayout(row)
        btn.clicked.connect(lambda: self._browse_open(le, label, filter))
        return le

    def _output_row(self, layout, label="Output (optional)") -> QLineEdit:
        layout.addWidget(QLabel(label))
        row = QHBoxLayout()
        le = QLineEdit()
        le.setPlaceholderText("Leave empty for default…")
        btn = QPushButton("Browse…")
        row.addWidget(le)
        row.addWidget(btn)
        layout.addLayout(row)
        btn.clicked.connect(lambda: self._browse_save(le, label))
        return le

    def _browse_open(self, le: QLineEdit, title: str, filter: str):
        path, _ = QFileDialog.getOpenFileName(self, title, "", filter)
        if path:
            le.setText(path)

    def _browse_save(self, le: QLineEdit, title: str):
        path, _ = QFileDialog.getSaveFileName(self, title, "")
        if path:
            le.setText(path)

    # ── worker ────────────────────────────────────────────────────────────

    def _start_worker(self, fn, *args, **kwargs):
        self._progress.setValue(0)
        self._status.setText("Running…")
        self._run_btn.setEnabled(False)
        self._worker = Worker(fn, args, kwargs)
        self._worker.progress.connect(lambda pct: self._progress.setValue(int(pct)))
        self._worker.finished.connect(self._on_finished)
        self._worker.error.connect(self._on_error)
        self._worker.start()

    # ── run section ───────────────────────────────────────────────────────

    def _build_run_section(self, layout):
        self._run_btn = QPushButton("▶  Run")
        self._run_btn.setFixedHeight(36)
        self._run_btn.clicked.connect(self._run)
        self._progress = QProgressBar()
        self._progress.setRange(0, 100)
        self._progress.setValue(0)
        self._status = QLabel("")
        layout.addWidget(self._run_btn)
        layout.addWidget(self._progress)
        layout.addWidget(self._status)

    def _on_finished(self, result):
        self._progress.setValue(100)
        self._status.setText(f"✅  Done → {Path(str(result)).name}")
        self._run_btn.setEnabled(True)

    def _on_error(self, msg):
        self._progress.setValue(0)
        self._status.setText(f"❌  {msg}")
        self._run_btn.setEnabled(True)
