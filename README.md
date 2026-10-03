# AdarvMaps

**Interactive epidemiological spot maps for India — no GIS software, no shapefiles, no setup.**

[![PyPI version](https://img.shields.io/pypi/v/adarvmaps.svg)](https://pypi.org/project/adarvmaps/)
[![Python versions](https://img.shields.io/pypi/pyversions/adarvmaps.svg)](https://pypi.org/project/adarvmaps/)
[![License: MIT](https://img.shields.io/pypi/l/adarvmaps.svg)](https://github.com/ADARV-Epi-hub/adarvmaps/blob/main/LICENSE)

AdarvMaps turns a spreadsheet of latitude and longitude from the field into a polished,
interactive HTML map. You can open the map in any browser, personalise it, and download
it as a **PNG** image or a **PDF**. AdarvMaps already has India's state and district
boundaries built in, so you don't have to search for shapefiles.

---

## Preparing your data

Please ensure each **row** in your spreadsheet is **one person or event**, and that each
row carries its **location** (latitude and longitude) in separate columns. You may also
include an extra column that splits the data into **case** and **control** (a *grouping
variable*), if you want to show both on the same map.

---

## What will AdarvMaps do?

AdarvMaps turns your spreadsheet into an interactive map. It automatically places every row
as a **dot** at its location, draws the correct **state and district boundaries** for you,
and colours the two groups differently. It then generates a single, self-contained **HTML**
file you can open in any browser to personalise your map, download as a PNG or PDF, or email
to a colleague. You can also aggregate the dots to switch from a spot map to a **dot-density**
map.

With AdarvMaps you can make:

- 📍 **Spot maps** — show the location of individual people or events
- 🔴 **Dot-density maps** — show the clustering of cases

---

## Which guide is for me?

| If this sounds like you… | Go to |
|---|---|
| 🙋 **"I just want a map — I don't write code."** | → [Guide for non-coders](#guide-for-non-coders) |
| 👩‍💻 **"I write Python and want the API / command line."** | → [Guide for developers](#guide-for-developers) |

---

## Guide for non-coders

This guide is for anyone who wants to create a map but has never written any code. You
don't need to install anything on your computer, and you don't need to understand any
programming. We'll give you the template code to copy and paste, and then AdarvMaps guides
you through the rest with a few simple, plain-English questions.

### Step 1 — Open a free notebook
Go to **[colab.research.google.com](https://colab.research.google.com)** and click
**New notebook**. Google Colab is a free service that runs code in your web browser, so
there's nothing to install. You'll see an empty box called a *cell*.

### Step 2 — Start AdarvMaps
Click inside the cell, paste the two lines below, and press the ▶ (play) button on the left:
```python
!pip install adarvmaps
import adarvmaps; adarvmaps.run()
```
The first line installs AdarvMaps; the second starts the guided wizard. Depending on your
internet speed, this may take a little while.

### Step 3 — Answer the questions
AdarvMaps asks **five** questions. For each one it shows its own best guess — if the guess is
right, just press **Enter** to accept it; otherwise, type the number of the correct choice.

**1. Upload your data file**
- In Jupyter Notebook, VS Code, or Google Colab, an *Upload* button appears — click it and
  pick your spreadsheet (CSV, Excel `.xlsx` / `.xls`, or TSV) from your computer.
- AdarvMaps then prints a quick summary — how many rows and columns it found, each column
  name with an example value, and the first few rows — so you can confirm the file was read
  correctly.
- **Please note:** on **Google Colab**, your data is temporarily uploaded to Google's
  servers. In **Jupyter Notebook, VS Code**, or similar software on your own computer, the
  data stays on your system and is not shared anywhere.

**2. Which column has the latitude?**
- Latitude is the north–south number (for example, `28.61` for Delhi).
- AdarvMaps pre-selects the column it thinks is the latitude. If the guess is correct, press
  Enter to accept; otherwise, check the summary above and type the number of the right column.

**3. Which column has the longitude?**
- Longitude is the east–west number (for example, `77.20` for Delhi).
- AdarvMaps pre-selects the column it thinks is the longitude. If the guess is correct, press
  Enter to accept; otherwise, check the summary above and type the number of the right column.
- **Remember:** if the points later look misplaced, the most common mistake is that latitude
  and longitude are swapped.

**4. Which column is your grouping variable?**
- If your spreadsheet has a variable that splits the data into *cases* and *controls*, or
  *affected* and *not affected*, choose it here — we call this the **grouping variable**.
- You can equally use this to show *males* and *females*, *dead* and *alive*, or *positive*
  and *negative* differently on the map.
- If you don't want any split, choose the first option: *My data is all cases (no control
  group)*.

**5. Which value is the main group?**
- AdarvMaps lists the values found in the grouping variable you chose in question 4.
- Tell it which value is the **main group** (the highlighted / clustered group). For example,
  if you coded `1 = Case, 0 = Control` or `Yes = Case, No = Control`, choose `1` or `Yes`.
- Every other value becomes the other group, shown with its own name from your data.

Once you've answered all five, AdarvMaps builds the map as an HTML file.

### Step 4 — Get your map
- Your map appears right below the cell and is also saved as a file (e.g. `adarvmaps_200926.html`).
- Download it and open it in any browser, or email it to a colleague — it's a single
  self-contained file (an internet connection is needed to load the background map tiles).
- Using the map's sidebar you can:
  - Switch between the **Spot Map** and the **Dot-Density Map**
  - Show one group or both
  - Change the colours of the dots and resize them
  - Turn place-name labels on or off
  - Save the map as a **PNG** image or **PDF**

---

## Guide for developers

### Step 1 — Install
```bash
pip install adarvmaps
```
Python 3.9+.

### Step 2 — Use it
```python
from adarvmaps import AdarvMaps

# `data` accepts a CSV path or a pandas DataFrame
AdarvMaps("my_data.csv").build().save("map.html")
```

Or from the command line (run `adarvmaps` with no arguments for the guided wizard):
```bash
adarvmaps my_data.csv -o map.html
```

### Python API reference
```python
AdarvMaps(
    data,                      # required: a CSV path or a pandas DataFrame
    state_shp=None,            # custom state boundary (shapefile / GeoPackage)
    district_shp=None,         # custom district boundary
    lat_col=None,              # override column auto-detection
    long_col=None,
    outcome_col=None,          # the grouping column
    case_value=None,           # which value in outcome_col is the main group
    case_label=None,           # name for the main group (default: the data's own value)
    control_label=None,        # name for the other group (default: the data's own value)
    all_cases=False,           # treat every row as a case (no second group)
    count_cutoff=2,            # districts ≤ cutoff → district-level zoom
    margin_deg=1.0,            # boundary crop padding
    cluster_color="#E85252",   # dot-density bubble colour
    case_color="#D55757",      # main-group pin colour
    control_color="#7676E7",   # other-group pin colour
)
```

### Common options
`AdarvMaps(data, ...)` — all options below are keyword arguments:

| Option | Default | Description |
|---|---|---|
| `lat_col`, `long_col`, `outcome_col` | auto | Override column auto-detection |
| `case_value` | auto | Value in `outcome_col` that is the main group |
| `case_label`, `control_label` | data values | Names shown for the two groups on the map |
| `all_cases` | `False` | Treat every row as a case (no second group) |
| `case_color`, `control_color`, `cluster_color` | ADARV palette | Marker colours (hex) |
| `state_shp`, `district_shp` | bundled | Use your own boundary files |

**Full API and CLI reference →** [DOCUMENTATION.md](https://github.com/ADARV-Epi-hub/adarvmaps/blob/main/DOCUMENTATION.md)

---

## Extra notes

### Preparing your data (details)
AdarvMaps reads a CSV and **auto-detects** the columns — you don't have to rename anything.
At a minimum it needs **location**, and optionally a **grouping** column:

| What AdarvMaps needs | Possible column names | How to provide it |
|---|---|---|
| **Coordinates** | `lat`, `lon` (or `latitude`, `longitude`) | Separate `lat` / `lon` columns, **or** one combined `"lat,lon"` column |
| **Grouping** (optional) | `outcome`, `status`, `case_control`, `case` | A column with two values, e.g. `case` / `control` |

**Example:**
```csv
latitude,longitude,outcome
28.6,77.2,case
19.0,72.8,control
13.0,80.2,case
```

### What you get
A single, self-contained HTML file you can open in any browser or share. Its sidebar lets
anyone switch between **Dot Density** and **Spot Pins**, show one group or both, recolour
and resize markers, toggle **place-name labels**, and export to **PNG / PDF**.

---

## ADARV Team

AdarvMaps is developed by the **ADARV** team:

1. **Muniraj Mallesan** (Maintainer)
2. **Dr. Sharan Murali** (Team Lead)
3. Manikandan K
4. Shanmuga Sundharam
5. Yogita Chaudhary
6. Barath U
7. Balaji S
8. Deepana R

## License

MIT © ADARV
