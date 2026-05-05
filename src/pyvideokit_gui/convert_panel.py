from pathlib import Path

from PySide6.QtWidgets import QLabel, QSpinBox, QVBoxLayout

from pyvideokit_gui._base_panel import BasePanel
from pyvideokit_libs import convert_to_ffv1


class ConvertPanel(BasePanel):
    def _build_ui(self, layout: QVBoxLayout):
        self._input = self._input_row(layout, "Input file")

        layout.addWidget(QLabel("FPS"))
        self._fps = QSpinBox()
        self._fps.setRange(1, 240)
        self._fps.setValue(60)
        layout.addWidget(self._fps)

        self._output = self._output_row(layout, "Output MKV (optional)")

    def _run(self):
        path = self._input.text().strip()
        if not path:
            self._status.setText("❌  Select an input file.")
            return
        output = self._output.text().strip() or None
        self._start_worker(convert_to_ffv1, Path(path), fps=self._fps.value(), output=output)
