"""Regression tests guarding behaviour that has previously broken.

Each test here maps to a real bug that shipped, so they should not be relaxed
without understanding what they protect.
"""

import re
import subprocess
import sys

import pandas as pd
import pytest

pytest.importorskip("geopandas")
pytest.importorskip("folium")

from adarvmaps import AdarvMaps  # noqa: E402
from adarvmaps.interactive import (  # noqa: E402
    _LAT_NAMES,
    _LONG_NAMES,
    _default_output,
    _guess,
)
from adarvmaps.loader import detect_lat_lon  # noqa: E402


# --------------------------------------------------------------------------
# Column auto-detection: the "x"/"y" substring bug
# --------------------------------------------------------------------------

def test_guess_prefers_exact_match_over_y_substring():
    """A column named 'lat' must beat an earlier column containing "y".

    Previously the single-letter alias "y" matched any column whose name
    merely contained that letter (e.g. 'survey_year'), so the wizard
    pre-selected the wrong column.
    """
    cols = ["id", "survey_year", "study_day", "sex", "lat", "long"]
    assert cols[_guess(cols, _LAT_NAMES)] == "lat"
    assert cols[_guess(cols, _LONG_NAMES)] == "long"


def test_detect_lat_lon_ignores_y_substring_columns():
    """The same bug in the non-interactive API path."""
    cols = ["id", "survey_year", "study_day", "lat", "long"]
    df = pd.DataFrame(
        {c: ([11.02] if c == "lat" else [76.97] if c == "long" else [1]) for c in cols}
    )
    assert detect_lat_lon(df) == ("lat", "long")


def test_single_letter_aliases_still_match_exactly():
    """Fixing the substring bug must not break genuine 'x'/'y' columns."""
    cols = ["y", "x"]
    assert cols[_guess(cols, _LAT_NAMES)] == "y"
    assert cols[_guess(cols, _LONG_NAMES)] == "x"


# --------------------------------------------------------------------------
# Group labels come from the data
# --------------------------------------------------------------------------

def _grouped_df():
    return pd.DataFrame({
        "lat": [11.0, 11.1, 28.6, 19.0],
        "lon": [76.9, 77.0, 77.2, 72.8],
        "status": ["Dead", "Alive", "Dead", "Alive"],
    })


def test_group_labels_default_to_the_data_values():
    html = (
        AdarvMaps(_grouped_df(), outcome_col="status", case_value="Dead")
        .build().map.get_root().render()
    )
    assert ">Dead<" in html and ">Alive<" in html
    assert "Only Dead" in html
    # the old hard-coded wording must be gone
    assert ">Case<" not in html and ">Control<" not in html


def test_explicit_labels_override_the_data_values():
    html = (
        AdarvMaps(
            _grouped_df(), outcome_col="status", case_value="Dead",
            case_label="Deceased", control_label="Survived",
        ).build().map.get_root().render()
    )
    assert ">Deceased<" in html and ">Survived<" in html


# --------------------------------------------------------------------------
# Output filename / embedded assets
# --------------------------------------------------------------------------

def test_default_output_filename_is_dated_ddmmyy():
    assert re.fullmatch(r"adarvmap_\d{6}\.html", _default_output())


def test_screenshoter_cdn_script_is_version_pinned():
    """An unversioned CDN URL would let an upstream release silently break
    PNG export in every map already generated."""
    df = pd.DataFrame({"lat": [11.0], "lon": [76.9], "case_control": ["case"]})
    html = AdarvMaps(df).build().map.get_root().render()
    assert "leaflet-simple-map-screenshoter@" in html


# --------------------------------------------------------------------------
# Importing the package must not pollute stdout
# --------------------------------------------------------------------------

def test_import_does_not_write_to_stdout():
    """The welcome banner must go to stderr, never stdout.

    Printing on import corrupts any script that emits CSV/JSON on stdout.
    """
    proc = subprocess.run(
        [sys.executable, "-c", "import adarvmaps; print('SENTINEL')"],
        capture_output=True, text=True, check=True,
    )
    assert proc.stdout.strip() == "SENTINEL"
