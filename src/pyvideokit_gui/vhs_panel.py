from pathlib import Path

from PySide6.QtWidgets import QVBoxLayout

from pyvideokit_gui._base_panel import BasePanel
from pyvideokit_libs import apply_vhs_effect


class VhsPanel(BasePanel):
    def _build_ui(self, layout: QVBoxLayout):
        self._inputs = self._batch_input_list(layout, "Input files (must have audio)")

    def _run(self):
        paths = [Path(self._inputs.item(i).text()) for i in range(self._inputs.count())]
        if not paths:
            self._status.setText("❌  Add at least one file.")
            return
        self._start_batch(apply_vhs_effect, paths, lambda p: {"output": None})
