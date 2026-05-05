# 🎬 PyVideoKit-GUI

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

## 🖥️ Desktop Integration

Arch Linux users get the launcher entry and icon automatically via the AUR package. For all other systems, create them manually:

**1. Save the icon:**

```bash
mkdir -p ~/.local/share/icons/hicolor/scalable/apps
cat > ~/.local/share/icons/hicolor/scalable/apps/pvk-gui.svg << 'EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
  <rect x="4" y="14" width="40" height="30" rx="3" fill="#2d3561"/>
  <rect x="10" y="19" width="28" height="20" rx="2" fill="#1a2038"/>
  <polygon points="18,21 18,37 33,29" fill="#ff6b6b"/>
  <rect x="4" y="6" width="40" height="8" rx="2" fill="#ff6b6b"/>
  <rect x="11" y="6" width="6" height="8" fill="#ffffff"/>
  <rect x="23" y="6" width="6" height="8" fill="#ffffff"/>
  <rect x="35" y="6" width="5" height="8" fill="#ffffff"/>
</svg>
EOF
```

**2. Create the `.desktop` entry:**

```bash
mkdir -p ~/.local/share/applications
cat > ~/.local/share/applications/pvk-gui.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=PyVideoKit
GenericName=Video Processing Tool
Comment=FFmpeg-based video processing GUI
Exec=pvk-gui
Icon=pvk-gui
Categories=AudioVideo;Video;AudioVideoEditing;
Terminal=false
Keywords=video;ffmpeg;trim;fade;vhs;youtube;convert;
EOF
```

**3. Refresh the icon cache** *(may be required on some desktop environments)*:

```bash
gtk-update-icon-cache ~/.local/share/icons/hicolor/
```

PyVideoKit will now appear in your application launcher.

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
