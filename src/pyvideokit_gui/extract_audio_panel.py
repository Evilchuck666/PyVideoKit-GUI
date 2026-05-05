from pathlib import Path

from PySide6.QtWidgets import QVBoxLayout

from pyvideokit_gui._base_panel import BasePanel
from pyvideokit_libs import extract_audio


class ExtractAudioPanel(BasePanel):
    def _build_ui(self, layout: QVBoxLayout):
        self._input = self._input_row(layout, "Input file")
        self._output = self._output_row(layout, "Output WAV (optional)")

    def _run(self):
        path = self._input.text().strip()
        if not path:
            self._status.setText("❌  Select an input file.")
            return
        output = self._output.text().strip() or None
        self._start_worker(extract_audio, Path(path), output=output)
