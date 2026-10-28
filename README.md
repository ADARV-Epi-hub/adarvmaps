# AdarvMaps

**Interactive epidemiological spot maps for India — no GIS software, no shapefiles, no setup.**

[![PyPI version](https://img.shields.io/pypi/v/adarvmaps.svg)](https://pypi.org/project/adarvmaps/)
[![Python versions](https://img.shields.io/pypi/pyversions/adarvmaps.svg)](https://pypi.org/project/adarvmaps/)
[![License: MIT](https://img.shields.io/pypi/l/adarvmaps.svg)](https://github.com/ADARV-Epi-hub/adarvmaps/blob/main/LICENSE)

AdarvMaps turns a spreadsheet of latitude and longitude from the field into a polished,
interactive HTML map. You can open this HTML map in any browser, make the necessary edits,
and then download it as a PNG image or a PDF. AdarvMaps already has India's state and
district boundaries built in, so that you don't have to search for shapefiles.

## Preparing data for AdarvMaps

Please ensure that each row in your spreadsheet corresponds to one person or event. Each of
these rows should also have its location (latitude and longitude) in separate columns. You
may also have extra columns in your spreadsheet indicating whether the person is a **case**
or a **control (grouping variable)**, if you intend to show both on the same map.

## What will AdarvMaps do?

AdarvMaps will turn your spreadsheet into an interactive map. AdarvMaps will automatically
place every row as a "dot" at its location on the map, draw the correct **state and district
boundaries** for you, and colour cases and controls differently. AdarvMaps will then generate
an interactive HTML file that you can open in your browser to personalise your map, and you
can download it as a PNG or PDF. You may also aggregate the dots and convert the spot map
into a dot-density map. The result is a single web page (**HTML**) you can open in any browser
or email to a colleague.

With AdarvMaps, you can generate maps with the following features:

- **Spot maps** for showing the location of individuals/events
- **Dot-density** map to show clustering of cases

## Which guide is for me?

| If this sounds like you… | Go to |
|---|---|
| "I just want a map — I don't write code." | [Guide for non-coders](#guide-for-non-coders) |
| "I write Python and want the API / command line." | [Guide for developers](#guide-for-developers) |

## Guide for non-coders

This guide is for anyone who wants to create a map but has never written any code. You don't
need to install anything on your computer, and you don't need to understand any programming.
We will give you the template code, which you can copy and paste. After this, the package
will guide you through the remaining steps with a few simple, plain-English questions.

### Step 1 — Open a free notebook

Go to **[colab.research.google.com](https://colab.research.google.com)** and click
**New notebook**. Google Colab is a free service that runs code in your web browser, so there
is nothing to install on your computer. You'll see an empty box called a *cell*.

### Step 2 — Start AdarvMaps

Click inside the cell, paste the two lines below, and press the ▶ (play) button on the left
of the cell:

```python
!pip install adarvmaps
import adarvmaps; adarvmaps.run()
```

The first line installs AdarvMaps; the second line starts the guided wizard. Based on your
internet speed, this step will take some time.

### Step 3 — Answer the questions

AdarvMaps will now ask five questions. For each one, it shows its **own best guess** — if the
guess is right, just press **Enter** to accept it; otherwise, type the number of the correct
choice.

Here is every question you'll see and what it means:

**1. Upload your data file**

- In Jupyter Notebook, VS Code, or Google Colab, an *Upload* button appears — click it and
  pick your spreadsheet (CSV, Excel .xlsx / .xls, or TSV) from your computer.
- AdarvMaps then prints a quick summary — how many rows and columns it found, each column name
  with an example value, and the first few rows — so you can confirm your file was read
  correctly.
- Please note: If you are running the package on Google Colab, your data will be temporarily
  uploaded to Google's servers (until the Colab session is active). However, if you are
  working in Jupyter Notebook, VS Code, or similar software, the data will remain within your
  system and won't be shared outside.

**2. Which column has the latitude?**

- Latitude is the north–south number (for example, 28.61 for Delhi).
- AdarvMaps will pre-select the column that it thinks is the latitude. If AdarvMaps' guess is
  correct, press Enter to accept.
- If the guess is wrong, check the quick summary generated above, and type the number of the
  right column.

**3. Which column has the longitude?**

- Longitude is the east–west number (for example, 77.20 for Delhi).
- AdarvMaps will pre-select the column that it thinks is the longitude. If AdarvMaps' guess is
  correct, press Enter to accept.
- If the guess is wrong, check the quick summary generated above, and type the number of the
  right column.
- Remember: if the points later look misplaced, the most common mistake is that the latitude
  and longitude may be swapped.

**4. Which column has the grouping variable?**

- If your spreadsheet has a variable that splits the data into "cases" and "controls," or into
  "affected" and "not affected," then you may choose that variable here. Let's call it the
  Grouping Variable.
- Alternatively, if you want to show "males" and "females," "dead" and "alive," "positive" and
  "negative" differently on the map, then you may also use this option.
- If you don't want to show any groups on the map, choose the first option: "My data is all
  cases (no control group)."

**5. Which value marks the outcome?**

- AdarvMaps will now show the values from the spreadsheet for the grouping variable that you
  chose in question 4.
- Please tell AdarvMaps which of the listed values refer to the "case."
- For example, you may have coded your spreadsheet as 1 = Case and 0 = Control, or Yes = Case,
  No = Control. AdarvMaps will now ask for the value you used to represent a case. In this
  case, you can choose 1 or Yes.
- Every other value is treated as a control.

Once you've answered all five, AdarvMaps will build the map as an HTML file.

### Step 4 — Getting the Map!

- Your map appears right below the cell and is also saved as a file (for example,
  `adarvmaps_281026.html`).
- Download it and open it in any browser — it is a single self-contained file (an internet
  connection is needed to load the background map tiles).
- Using the map's sidebar, you can make the following edits:
  - Switch between the Spot Map and the Dot-Density Map
  - Hide "controls"
  - Change the colours of the dots, and resize them
  - Turn place-name labels on or off, and finally
  - Save the map as a PNG image or PDF.

## Guide for developers

### Step 1: Installing the package

```bash
pip install adarvmaps
```

### Step 2: Running the package

```python
from adarvmaps import AdarvMaps

# `data` accepts a CSV path or a pandas DataFrame
AdarvMaps("my_data.csv").build().save("map.html")
```

Or from the command line:

```bash
adarvmaps my_data.csv -o map.html
```

A fuller example (overriding the automatic choices):

```python
AdarvMaps(
    "cases.csv",
    lat_col="Latitude",
    long_col="Longitude",
    outcome_col="vital_status",
    case_value="dead",
    case_label="Deaths",
    control_label="Survivors",
    case_color="#B00020",
    control_color="#0057B7",
).build().save("map.html")
```

### Common options

`AdarvMaps(data, ...)` — all options below are keyword arguments:

| Option | Default | Description |
|---|---|---|
| lat_col, long_col, outcome_col | auto | Override column auto-detection |
| case_value | auto | Value in outcome_col that means "case" |
| case_label, control_label | data values | Names shown for the two groups on the map |
| all_cases | False | Treat every row as a case (no controls) |
| case_color, control_color, cluster_color | ADARV palette | Marker colours (hex) |
| state_shp, district_shp | bundled | Use your own boundary files |

**Full API and CLI reference →** [DOCUMENTATION.md](https://github.com/ADARV-Epi-hub/adarvmaps/blob/main/DOCUMENTATION.md)

## Extra notes

### Preparing your data

AdarvMaps reads a CSV and **auto-detects** the columns. You don't have to rename anything. At
a minimum, it needs the following variables:

| What AdarvMaps needs | Possible column names | How to provide it |
|---|---|---|
| Coordinates | lat, lon (or latitude, longitude) | Separate lat / lon columns, or one combined "lat,lon" column |
| Grouping (optional) | outcome, status, case_control, case | A column with values like case / control |

**Example:**

```csv
latitude, longitude, outcome
28.6, 77.2, case
19.0, 72.8, control
13.0, 80.2, case
```

### What you get

A single, self-contained HTML file you can open in any browser or share. Its sidebar lets
anyone switch between **Dot Density** and **Spot Pins**, show one group or both groups,
recolour markers, resize pins, toggle **place-name labels**, and export to **PNG / PDF**.

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
