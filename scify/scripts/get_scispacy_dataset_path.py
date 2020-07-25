import os
from pathlib import Path
CACHE_ROOT = Path(os.getenv("SCISPACY_CACHE", str(Path.home() / ".scispacy")))
DATASET_CACHE = str(CACHE_ROOT / "datasets")
print(DATASET_CACHE)

