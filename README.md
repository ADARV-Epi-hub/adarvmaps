# SpotMap

**Interactive epidemiological spot maps for India — no GIS software, no shapefiles, no setup.**

[![PyPI version](https://img.shields.io/pypi/v/spotmap.svg)](https://pypi.org/project/spotmap/)
[![Python versions](https://img.shields.io/pypi/pyversions/spotmap.svg)](https://pypi.org/project/spotmap/)
[![License: MIT](https://img.shields.io/pypi/l/spotmap.svg)](https://github.com/ADARV-Epi-hub/spotmap/blob/main/LICENSE)

SpotMap turns a spreadsheet of case/control coordinates into a polished, interactive
HTML map you can open in any browser or drop straight into a report. India's state and
district boundaries are built in — you don't download or configure anything.

- 📍 **Spot pins** for individual cases and controls, in colours you choose
- 🔴 **Dot-density** clustering to spot hotspots at a glance
- 🗺️ Built-in **state & district boundaries** — nothing to download
- 🏷️ Toggle place-name labels, resize pins, and switch modes live
- 💾 Export the finished map to **PNG** or **PDF**
- 🤖 **Auto-detects** your latitude / longitude / outcome columns

---

## Which guide is for me?

| If this sounds like you… | Go to |
|---|---|
| 🙋 **"I just want a map — I don't write code."** | → [Guide for non-coders](#guide-for-non-coders) |
| 👩‍💻 **"I write Python and want the API / command line."** | → [Guide for developers](#guide-for-developers) |

---

## Guide for non-coders

**You don't need to install anything on your computer.** The easiest way is
**Google Colab** — a free notebook that runs in your web browser.

**Step 1** — Open **[colab.research.google.com](https://colab.research.google.com)** and click **New notebook**.

**Step 2** — Paste these two lines into the cell and press ▶:
```python
!pip install spotmap
import spotmap; spotmap.run()
```

**Step 3** — Follow the simple prompts:
1. Click the button to **upload your data file**.
2. Confirm the **latitude**, **longitude**, and **case/control** columns SpotMap detected.
3. Choose which value means a **"case"** (e.g. `case`, `positive`, `1`).

Your map appears right below the cell and is saved as `spotmap.html` to download and share.

> 💡 See [Preparing your data](#preparing-your-data) — any spreadsheet with location and case/control columns works.

---

## Guide for developers

### Install
```bash
pip install spotmap
```
Python 3.9+.

### Usage
```python
from spotmap import SpotMap

# `data` accepts a CSV path or a pandas DataFrame
SpotMap("my_data.csv").build().save("map.html")
```

Or from the command line:
```bash
spotmap my_data.csv -o map.html
```

### Common options
`SpotMap(data, ...)` — all options below are keyword arguments:

| Option | Default | Description |
|---|---|---|
| `lat_col`, `long_col`, `outcome_col` | auto | Override column auto-detection |
| `case_value` | auto | Value in `outcome_col` that means "case" |
| `all_cases` | `False` | Treat every row as a case (no controls) |
| `case_color`, `control_color`, `cluster_color` | ADARV palette | Marker colours (hex) |
| `state_shp`, `district_shp` | bundled | Use your own boundary files |

**Full API and CLI reference →** [DOCUMENTATION.md](https://github.com/ADARV-Epi-hub/spotmap/blob/main/DOCUMENTATION.md)

---

## Preparing your data

SpotMap reads a CSV and **auto-detects** the columns — you don't have to rename anything.
At a minimum it needs **location** and **outcome**:

| What SpotMap needs | How to provide it |
|---|---|
| **Coordinates** | Separate `lat` / `lon` columns **or** one combined `"lat,lon"` column |
| **Outcome** | A column (e.g. `outcome`, `status`, `case_control`) with values like `case` / `control` |

**Example:**
```csv
latitude,longitude,outcome
28.6,77.2,case
19.0,72.8,control
13.0,80.2,case
```

---

## What you get

A single, self-contained HTML file you can open in any browser or share. Its sidebar lets
anyone switch between **Dot Density** and **Spot Pins**, show **Cases Only** or
**Cases & Controls**, recolour markers, resize pins, toggle **place-name labels**, and
export to **PNG / PDF**.

---

## Team

SpotMap is developed by the **ADARV** team: **Muniraj Mallesan** (maintainer),
**Dr. Sharan Murali** (team lead), Manikandan K, Shanmuga Sundharam, Yogita Chaudhary,
Barath U, Balaji S, and Deepana R.

## License

MIT © ADARV
