from __future__ import annotations

import importlib.util
from pathlib import Path


def load_shared_module():
    script_path = (
        Path(__file__).resolve().parents[2]
        / "formatting-journal"
        / "scripts"
        / "generate_manuscript.py"
    )
    spec = importlib.util.spec_from_file_location("shared_manuscript_generator", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load shared generator at {script_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    module = load_shared_module()
    raise SystemExit(module.main(default_style="mdpi", default_journal="Foods"))
