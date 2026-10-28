# AdarvMaps — Reference

This is the full reference for developers using **adarvmaps** in Python or from
the command line. If you just want to make a map without writing code, start
with the [README](README.md) instead.

- [Install](#install)
- [Three ways to use it](#three-ways-to-use-it)
- [Python: all the options](#python-all-the-options)
- [Command line](#command-line)
- [Your data](#your-data)
- [Naming the two groups](#naming-the-two-groups)
- [Using your own boundaries](#using-your-own-boundaries)
- [Errors you might see](#errors-you-might-see)
- [How it works (in plain English)](#how-it-works-in-plain-english)
- [For contributors](#for-contributors)

---

## Install

```bash
pip install adarvmaps
```
Needs Python 3.9 or newer. Everything else (the India boundaries, all the map
tools) comes with it — nothing else to download.

---

## Three ways to use it

All three do the same thing under the hood:

| You want to… | Use this |
|---|---|
| Write Python | `adarvmaps("data.csv").build().save("map.html")` |
| Use the command line | `adarvmaps data.csv -o map.html` |
| Be guided step by step | `adarvmaps` (no arguments) — or `adarvmaps.run()` in Python |

---

## Python: all the options

The one thing to know: call `adarvmaps(...)`, then `.build()`, then `.save()`.
(`adarvmaps` is a lowercase alias of the `AdarvMaps` class — either name works.)

```python
from adarvmaps import adarvmaps

adarvmaps("my_data.csv").build().save("map.html")
```

`data` can be a file path (CSV, Excel, or TSV) **or** a pandas DataFrame.
Everything else is optional — AdarvMaps figures it out from your data. Pass an
option only when you want to override what it guessed:

| Option | What it does | Default |
|---|---|---|
| `lat_col` | Name of your latitude column | auto-detected |
| `long_col` | Name of your longitude column | auto-detected |
| `outcome_col` | The column that splits your data into groups | auto-detected |
| `case_value` | Which value in that column is the main group | auto-detected |
| `case_label` | What to call the main group on the map | the value from your data (e.g. `"Dead"`) |
| `control_label` | What to call the other group | the other value (e.g. `"Alive"`) |
| `all_cases` | Treat every row as a case (no second group) | `False` |
| `case_color` | Colour of the main-group pins | ADARV red |
| `control_color` | Colour of the other-group pins | ADARV blue |
| `cluster_color` | Colour of the dot-density bubbles | ADARV red |
| `state_shp` / `district_shp` | Use your own boundary files | the built-in India ones |

**A fuller example:**
```python
from adarvmaps import adarvmaps

adarvmaps(
    "cases.csv",
    outcome_col="sex",       # split the map by this column
    case_value="male",       # males are the highlighted group
    case_color="#D55757",
    control_color="#7676E7",
).build().save("map.html")
```

**Getting the map object** (if you want to customise it further with Folium):
```python
m = adarvmaps("data.csv").build()
m.save("map.html")
folium_map = m.map          # the underlying folium.Map
```
`.save()` will complain if you call it before `.build()`.

---

## Command line

```bash
adarvmaps data.csv -o map.html
```
Run `adarvmaps` with **no arguments** to get the guided step-by-step wizard.

| Flag | Meaning |
|---|---|
| `-o`, `--output` | Where to save the HTML (default: a dated name like `adarvmaps_200926.html`) |
| `--lat-col` / `--lon-col` | Latitude / longitude column names |
| `--outcome-col` / `--case-value` | Grouping column and its main value |
| `--case-color` / `--control-color` / `--cluster-color` | Marker colours (hex) |
| `--state-shp` / `--district-shp` | Your own boundary files |

---

## Your data

Each **row** is one person or event. At a minimum you need **location**, and
usually a **grouping** column:

| Need | How to provide it |
|---|---|
| Coordinates | Separate `lat` and `lon` columns, **or** one `"lat,lon"` column |
| Grouping (optional) | A column like `outcome`, `status`, or `case_control` with two values |

AdarvMaps recognises common column names automatically (`lat`, `latitude`;
`lon`, `long`, `longitude`; `outcome`, `status`, `case_control`, …). If a point
looks misplaced, the usual cause is latitude and longitude being swapped —
AdarvMaps warns you when most points fall outside India.

**Example:**
```csv
latitude,longitude,outcome
28.6,77.2,case
19.0,72.8,control
```

---

## Naming the two groups

Your grouping column can be anything with two values — `case`/`control`,
`male`/`female`, `dead`/`alive`, `positive`/`negative`. The map automatically
uses **your data's own words** in the legend, pop-ups, and menu. You only need
`case_label` / `control_label` if you want to display different names than the
values in your file.

---

## Using your own boundaries

The India state and district boundaries are built in. To use your own instead:
```python
adarvmaps(
    "cases.csv",
    state_shp="path/to/states.shp",
    district_shp="path/to/districts.shp",
).build().save("map.html")
```
Shapefiles and GeoPackages both work; AdarvMaps finds the name column for you.

---

## Errors you might see

| Error | What it means | What to do |
|---|---|---|
| `ColumnNotFoundError` | It couldn't find your latitude, longitude, or grouping column | Pass the column name explicitly (e.g. `lat_col="Latitude"`) |
| `NoCasePointsError` | No rows matched the value you chose as the main group | Check `case_value` matches a value in your column |
| `ValueError: empty` | The file had no rows (or all rows had bad coordinates) | Check the file loaded correctly |

---

## How it works (in plain English)

When you call `.build()`, AdarvMaps:

1. **Reads your file** and finds the latitude, longitude, and grouping columns
   (dropping any rows with bad coordinates).
2. **Places each row on the map of India** and works out which state and
   district it falls in.
3. **Splits the rows into two groups** based on your grouping column.
4. **Zooms to the right level** — one district, a few states, or all of India —
   depending on how spread out your data is.
5. **Draws everything**: the boundaries, the coloured pins (or clustered
   "dot-density" bubbles), and the sidebar of controls.

The result is one self-contained HTML file. All the buttons on it (switching
modes, changing colours, saving a PNG) run in the viewer's browser — there's no
server involved. (It does need internet to load the grey background map.)

---

## For contributors

The package is organised into small, single-job files:

| File | Job |
|---|---|
| `map_builder.py` | The `AdarvMaps` class — runs the whole process |
| `loader.py` | Reads files, auto-detects columns |
| `spatial.py` | Boundaries, matching points to districts, zoom level |
| `layers.py` | Draws the pins and clusters |
| `sidebar.py` | Builds the map's control panel (HTML/CSS/JS) |
| `interactive.py` | The step-by-step wizard |
| `cli.py` | The `adarvmaps` command |
| `data/` | The built-in India boundary files |

**Tests** live in `tests/` — run them with `pytest`. They also run automatically
on every push via GitHub Actions (see `.github/workflows/`). If you change how
maps are generated, please add a test.

---

MIT © ADARV
