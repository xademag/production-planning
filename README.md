# Production Planning — Starter scaffold

This scaffold provides a minimal Python + WPF UI starter for production planning.

Requirements
- Windows
- Python 3.8+ (64-bit)
- `pythonnet` (install with `pip install -r requirements.txt`)

Run

```powershell
pip install -r requirements.txt
python src\main.py
```

Notes
- The UI uses WPF via `pythonnet`. The app loads XAML files from `src/ui/` and JSON data from `data/`.
- JSON files in `data/` are simple starting samples you can expand.
