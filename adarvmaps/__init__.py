"""adarvmaps — Interactive epidemiological spot maps for India."""

from .exceptions import ColumnNotFoundError, NoCasePointsError, AdarvMapsError
from .interactive import run_interactive, adarvmaps_run
from .map_builder import AdarvMaps

# Short, friendly alias so non-coders can simply do:  import adarvmaps; adarvmaps.run()
run = adarvmaps_run

__version__ = "0.1.42"
__all__ = [
    "AdarvMaps",
    "run",  # friendly alias for adarvmaps_run
    "adarvmaps_run",
    "run_interactive",  # deprecated alias, kept for backward compat
    "AdarvMapsError",
    "ColumnNotFoundError",
    "NoCasePointsError",
]

_BANNER = (
    "\n"
    "Interactive AdarvMaps for India - created by ADARV\n"
    "\n"
    "No code required! To build your map, just run:\n"
    "\n"
    "adarvmaps.run()\n"
    "\n"
    "You'll be asked to choose your data file, then your map appears.\n"
)


def _in_interactive_session() -> bool:
    """True for a REPL, Jupyter/Colab notebook, or an interactive terminal."""
    import sys

    if "ipykernel" in sys.modules or "google.colab" in sys.modules:
        return True
    if hasattr(sys, "ps1"):  # plain Python REPL
        return True
    try:
        return bool(sys.stdout.isatty())
    except Exception:  # noqa: BLE001 — detached/!closed streams
        return False


def _show_banner() -> None:
    """Show the first-run hint for non-coders.

    Written to **stderr**, and only in an interactive session, so that
    importing adarvmaps never pollutes piped or redirected stdout (which
    would corrupt scripts that emit CSV/JSON).  This mirrors R's
    ``packageStartupMessage`` behaviour in the sibling adarvmapsr package.
    """
    import sys

    if _in_interactive_session():
        print(_BANNER, file=sys.stderr)


_show_banner()
