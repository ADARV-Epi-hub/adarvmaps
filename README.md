# AdarvMap

**Interactive epidemiological spot maps for India — no GIS software, no shapefiles, no setup.**

[![PyPI version](https://img.shields.io/pypi/v/adarvmap.svg)](https://pypi.org/project/adarvmap/)
[![Python versions](https://img.shields.io/pypi/pyversions/adarvmap.svg)](https://pypi.org/project/adarvmap/)
[![License: MIT](https://img.shields.io/pypi/l/adarvmap.svg)](https://github.com/ADARV-Epi-hub/adarvmap/blob/main/LICENSE)

AdarvMap turns a spreadsheet of latitude and longitude from the field into a polished,
interactive HTML map. You can open the map in any browser, make edits, and download it as
a **PNG** image or **PDF**. India's state and district boundaries are already built in, so
you don't have to search for shapefiles.

- 📍 **Spot maps** — show the location of individual people or events
- 🔴 **Dot-density maps** — aggregate nearby points to show clustering of cases
- 🗺️ Built-in **state & district boundaries** — nothing to download
- 🎨 Recolour and resize markers, toggle place-name labels, export to PNG / PDF
- 🤖 **Auto-detects** your latitude / longitude / outcome columns

---

## What will AdarvMap do?

AdarvMap turns your spreadsheet into an interactive map. It automatically places every
row as a **dot** at its location, draws the correct **state and district boundaries**, and
colours the groups (e.g. cases and controls) differently. It then generates a single,
self-contained **HTML** file you can open in any browser to fine-tune your map — and you
can download it as a PNG or PDF, or email it to a colleague. You may also aggregate the
dots to switch from a spot map to a **dot-density** map.

---

## Which guide is for me?

| If this sounds like you… | Go to |
|---|---|
| 🙋 **"I just want a map — I don't write code."** | → [Guide for non-coders](#guide-for-non-coders) |
| 👩‍💻 **"I write Python and want the API / command line."** | → [Guide for developers](#guide-for-developers) |

Everyone should also read [Preparing your data](#preparing-your-data) first.

---

## Preparing your data

Each **row** in your spreadsheet should be **one person or event**, and each row should
carry its **location** (latitude and longitude) in separate columns. You may also include
an extra column that splits the data into groups (e.g. case / control) if you want to show
both on the same map.

---

## Guide for non-coders

This guide is for anyone who wants a map but has never written any code. You don't need to
install anything on your computer. You'll copy and paste two lines of template code, and
then AdarvMap will guide you through the rest with a few plain-English questions.

### Step 1 — Open a free notebook
Go to **[colab.research.google.com](https://colab.research.google.com)** and click
**New notebook**. Google Colab is a free service that runs code in your web browser, so
there's nothing to install. You'll see an empty box called a *cell*.

### Step 2 — Start AdarvMap
Click inside the cell, paste the two lines below, and press the ▶ (play) button:
```python
!pip install adarvmap
import adarvmap; adarvmap.run()
```
The first line installs AdarvMap; the second starts the guided wizard. Depending on your
internet speed, the install may take a little while.

### Step 3 — Answer the questions
AdarvMap asks **five** questions. Each shows its own best guess — press **Enter** to
accept it, or type the number of the correct choice.

1. **Upload your data file**
   - In Colab (or Jupyter / VS Code) an *Upload* button appears — click it and pick your
     spreadsheet (CSV, Excel `.xlsx` / `.xls`, or TSV).
   - AdarvMap prints a quick summary — the number of rows and columns, each column name
     with an example value, and the first few rows — so you can confirm it read your file.
   - **FAQ: Is my data uploaded to a server?** On **Colab**, yes — Colab runs on Google's
     cloud, so your file is processed on Google's servers (see the privacy note below). If
     your data must stay private, **run AdarvMap locally** instead (see Guide for
     developers) — nothing leaves your computer.

2. **Which column has the latitude?**
   - Latitude is the north–south number (for example, `28.61` for Delhi).
   - AdarvMap pre-selects the column it thinks is latitude — press Enter to accept, or, if
     the guess is wrong, check the summary above and type the number of the right column.

3. **Which column has the longitude?**
   - Longitude is the east–west number (for example, `77.20` for Delhi).
   - AdarvMap pre-selects its best guess — accept it or pick another.
   - **Remember:** if the points later look misplaced, the most common cause is that
     latitude and longitude are swapped.

4. **Which column is your grouping variable?**
   - Choose the column that splits your data into two groups — *case* / *control*,
     *affected* / *not affected*, *male* / *female*, *dead* / *alive*, *positive* /
     *negative*, and so on. The map uses the **actual values from your data** as the group
     names automatically — you don't have to type anything.
   - If you don't want any split, choose the first option: *No grouping — show all rows
     the same*.

5. **Which value is the main group?**
   - AdarvMap lists the values found in the column you chose. Tell it which one is the
     **main group** (it's the highlighted / clustered group; for example, if you coded
     `1 = Case, 0 = Control`, choose `1`).
   - Every other value becomes the other group, shown with its own name.

### Step 4 — Get your map
- Your map appears right below the cell and is saved as a file called `adarvmap.html`.
- Download it and open it in any browser, or email it to a colleague — it's a single
  self-contained file (an internet connection is needed to load the background map tiles).
- Using the map's sidebar you can: switch between **Spot Map** and **Dot Density**, show one
  group or both, change colours and resize the dots, toggle **place-name labels**, and save
  the map as a **PNG** or **PDF**.

---

## Guide for developers

### Install
```bash
pip install adarvmap
```
Python 3.9+.

### Usage
```python
from adarvmap import AdarvMap

# `data` accepts a CSV path or a pandas DataFrame
AdarvMap("my_data.csv").build().save("map.html")
```

Or from the command line:
```bash
adarvmap my_data.csv -o map.html
```

### Common options
`AdarvMap(data, ...)` — all options below are keyword arguments:

| Option | Default | Description |
|---|---|---|
| `lat_col`, `long_col`, `outcome_col` | auto | Override column auto-detection |
| `case_value` | auto | Value in `outcome_col` that means "case" |
| `case_label`, `control_label` | "Case" / "Control" | Names for the two groups, e.g. "Male" / "Female" |
| `all_cases` | `False` | Treat every row as a case (no controls) |
| `case_color`, `control_color`, `cluster_color` | ADARV palette | Marker colours (hex) |
| `state_shp`, `district_shp` | bundled | Use your own boundary files |

**Full API and CLI reference →** [DOCUMENTATION.md](https://github.com/ADARV-Epi-hub/adarvmap/blob/main/DOCUMENTATION.md)

> 🔒 **Privacy:** running AdarvMap locally keeps your data on your machine — nothing is
> uploaded. Google Colab is convenient but runs on Google's cloud, so use it only for
> de-identified or demo data.

---

## Preparing your data (details)

AdarvMap reads a CSV and **auto-detects** the columns — you don't have to rename anything.
At a minimum it needs **location** and, optionally, an **outcome**:

| What AdarvMap needs | Possible column names | How to provide it |
|---|---|---|
| **Coordinates** | `lat`, `lon` (or `latitude`, `longitude`) | Separate `lat` / `lon` columns **or** one combined `"lat,lon"` column |
| **Outcome** (optional) | `outcome`, `status`, `case_control`, `case` | A column with values like `case` / `control` |

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
anyone switch between **Dot Density** and **Spot Pins**, show one group or both, recolour
and resize markers, toggle **place-name labels**, and export to **PNG / PDF**.

---

## ADARV Team

AdarvMap is developed by the **ADARV** team: **Muniraj Mallesan** (maintainer),
**Dr. Sharan Murali** (team lead), Manikandan K, Shanmuga Sundharam, Yogita Chaudhary,
Barath U, Balaji S, and Deepana R.

## License

MIT © ADARV
