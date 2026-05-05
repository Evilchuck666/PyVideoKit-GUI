# 🎥 PyVideoKit-GUI

![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue)
![License](https://img.shields.io/badge/license-GPLv3-green)

Graphical interface for PyVideoKit — FFmpeg-based video processing. Provides the same operations as [PyVideoKit-CLI](../PyVideoKit-CLI) through a PySide6 desktop application with real-time progress tracking.

---

## ✨ Features

- 📼 **VHS effect** — retro visual noise, color bleed, and audio degradation
- ✂️ **Trim** — cut a segment by start/end time with stream copy (no re-encoding)
- 🔗 **Concatenate** — join multiple videos with drag-and-drop reordering
- 🎬 **Fade** — fade-in and/or fade-out on an FFV1 master
- 🔊 **Extract audio** — dump the audio track to uncompressed WAV (PCM 16-bit)
- 🎞️ **Convert to FFV1** — create a lossless MKV master for editing
- 📺 **Prepare for YouTube** — encode to ProRes 422 HQ MOV, upscaled to 4K

---

## 📦 Requirements

- **Python** ≥ 3.10
- **PySide6** ≥ 6.0
- **FFmpeg** and **FFprobe** available in `PATH`
- **SoX** available in `PATH` (required by VHS effect)
- **PyVideoKit-Libs** — installed automatically as a dependency

---

## 🔧 Installation

### 🏗️ Arch Linux (AUR)

```bash
yay -S python-pyvideokit-gui
```

FFmpeg, FFprobe, SoX, PySide6, and PyVideoKit-Libs are installed automatically as pacman dependencies.

### 🐍 Other systems (pip)

```bash
pip install PyVideoKit-GUI
```

Make sure **FFmpeg**, **FFprobe**, and **SoX** are available in your `PATH`.

---

## 🚀 Usage

```bash
pvk-gui
```

The application opens a tabbed window. Each tab corresponds to one operation:

| Tab | Operation |
|---|---|
| 🎞️ Convert to FFV1 | Convert any video to a lossless FFV1/MKV master |
| ✂️ Trim | Cut a segment by start/end time (no re-encoding) |
| 🔗 Concat | Join multiple videos (drag to reorder) |
| 🎬 Fade | Add fade-in and/or fade-out |
| 📼 VHS Effect | Apply retro VHS visual and audio effect |
| 🔊 Extract Audio | Export audio track to WAV |
| 📺 YouTube | Encode to ProRes 422 HQ MOV for upload |

All operations run in a background thread and display a real-time progress bar.

---

## 🔄 Typical Workflow

```
🎞️ Convert to FFV1  →  ✂️ Trim / 🎬 Fade / 📼 VHS Effect  →  📺 YouTube
```

> Operations that re-encode (Fade, VHS Effect, YouTube) expect an FFV1 `.mkv` as input.

---

## ⚖️ License

This project is licensed under the GPLv3 License — see the [LICENSE](LICENSE) file for details.
