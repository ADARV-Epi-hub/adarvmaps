"""adarvmaps — Interactive epidemiological spot maps for India."""

from .exceptions import ColumnNotFoundError, NoCasePointsError, AdarvMapsError
from .interactive import run_interactive, adarvmaps_run
from .map_builder import AdarvMaps

# Short, friendly alias so non-coders can simply do:  import adarvmaps; adarvmaps.run()
run = adarvmaps_run

__version__ = "0.1.39"
__all__ = [
    "AdarvMaps",
    "run",  # friendly alias for adarvmaps_run
    "adarvmaps_run",
    "run_interactive",  # deprecated alias, kept for backward compat
    "AdarvMapsError",
    "ColumnNotFoundError",
    "NoCasePointsError",
]

# Friendly welcome shown when the package is imported, to help first-time
# (non-coder) users know how to launch the tool.  At this point `import adarvmaps`
# has already run, so we only need to tell them the one next line.
print(
    f"\n"
    f"Interactive AdarvMaps for India - created by ADARV\n"
    f"\n"
    f"No code required! To build your map, just run:\n"
    f"\n"
    f"adarvmaps.run()\n"
    f"\n"
    f"You'll be asked to choose your data file, then your map appears.\n"
)
