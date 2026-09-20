"""Command-line interface for adarvmaps."""

import argparse
import sys


_EPILOG = """\
Examples:
  adarvmaps                            launch the guided wizard (easiest)
  adarvmaps data.csv                   build a map from data.csv
  adarvmaps data.csv -o my_map.html    choose where to save the map

In Python or Google Colab:
  from adarvmaps import adarvmaps_run
  adarvmaps_run()
"""


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="adarvmaps",
        description="Generate an interactive epidemiological spot map for India.",
        epilog=_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "csv",
        nargs="?",
        default=None,
        help="Path to your data file (CSV/Excel). Omit it to launch the guided wizard.",
    )
    p.add_argument(
        "-o", "--output",
        default=None,
        help="Output HTML file path (default: a dated file, e.g. adarvmap_200926.html).",
    )
    p.add_argument("--state-shp", default=None, help="Custom state boundary file.")
    p.add_argument("--district-shp", default=None, help="Custom district boundary file.")
    p.add_argument("--lat-col", default=None, help="Latitude column name.")
    p.add_argument("--lon-col", default=None, help="Longitude column name.")
    p.add_argument("--outcome-col", default=None, help="Outcome column name.")
    p.add_argument("--case-value", default=None, help="Value that represents a case.")
    p.add_argument(
        "--count-cutoff",
        type=int,
        default=2,
        help="District count threshold for mode selection (default: 2).",
    )
    p.add_argument(
        "--cluster-color",
        default="#E85252",
        help="Hex colour for dot-density clusters (default: #E85252).",
    )
    p.add_argument(
        "--case-color",
        default="#D55757",
        help="Hex colour for case pins (default: #D55757).",
    )
    p.add_argument(
        "--control-color",
        default="#7676E7",
        help="Hex colour for control pins (default: #7676E7).",
    )
    p.add_argument(
        "--case-label",
        default=None,
        help="Name for the case group on the map, e.g. Male (default: Case).",
    )
    p.add_argument(
        "--control-label",
        default=None,
        help="Name for the control group on the map, e.g. Female (default: Control).",
    )
    return p


def main(argv=None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    # No data file given → launch the friendly step-by-step wizard.
    if args.csv is None:
        from .interactive import adarvmaps_run
        adarvmaps_run(args.output)
        return

    from .map_builder import AdarvMaps
    from .interactive import _default_output

    output = args.output or _default_output()
    try:
        AdarvMaps(
            args.csv,
            state_shp=args.state_shp,
            district_shp=args.district_shp,
            lat_col=args.lat_col,
            long_col=args.lon_col,
            outcome_col=args.outcome_col,
            case_value=args.case_value,
            count_cutoff=args.count_cutoff,
            cluster_color=args.cluster_color,
            case_color=args.case_color,
            control_color=args.control_color,
            case_label=args.case_label,
            control_label=args.control_label,
        ).build().save(output)
        print(f"Map saved to: {output}")
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
