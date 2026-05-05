from pathlib import Path

from PySide6.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QSpinBox, QVBoxLayout

from pyvideokit_gui._base_panel import BasePanel
from pyvideokit_libs import convert_to_ffv1


class ConvertPanel(BasePanel):
    def _build_ui(self, layout: QVBoxLayout):
        self._input = self._input_row(layout, "Input file")

        fps_row = QHBoxLayout()
        self._fps_override = QCheckBox("Override FPS")
        self._fps = QSpinBox()
        self._fps.setRange(1, 240)
        self._fps.setValue(60)
        self._fps.setEnabled(False)
        self._fps_override.toggled.connect(self._fps.setEnabled)
        fps_row.addWidget(self._fps_override)
        fps_row.addWidget(self._fps)
        fps_row.addStretch()
        layout.addLayout(fps_row)

        self._output = self._output_row(layout, "Output MKV (optional)")

    def _run(self):
        path = self._input.text().strip()
        if not path:
            self._status.setText("❌  Select an input file.")
            return
        output = self._output.text().strip() or None
        fps = self._fps.value() if self._fps_override.isChecked() else None
        self._start_worker(convert_to_ffv1, Path(path), fps=fps, output=output)
