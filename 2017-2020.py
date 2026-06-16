#!/usr/bin/env python3
# VERSION: GitHub outputs/figures layout — 2026-06-16
"""Create the 2017–2020 Metaverse Research Landscape video.

Expected repository layout (default):

    project-root/
    ├── 2017-2020.py
    ├── outputs/
    │   ├── figures/
    │   │   ├── metaverse_landscape_2017.jpeg
    │   │   ├── metaverse_landscape_2018.jpeg
    │   │   └── ...
    │   └── videos/

The script discovers one image for every year from 2017 through 2020,
adds a year label, creates opening and closing cards, and encodes an MP4.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

START_YEAR = 2017
END_YEAR = 2020
DEFAULT_SIZE = 768
DEFAULT_FPS = 30
DEFAULT_OPENING_SECONDS = 2.5
DEFAULT_IMAGE_SECONDS = 2.0
DEFAULT_ENDING_SECONDS = 3.0
OUTPUT_NAME = "Metaverse_Landscape_2017_2020.mp4"

TITLE = "Metaverse Research Landscape\n2017–2020"
OPENING_SUBTITLE = (
    "Blockchain, IoT, smart contracts, security, digital twins, and AI"
)
ENDING_TITLE = "2017–2020"
ENDING_SUBTITLE = (
    "The research landscape shifted toward connected infrastructures: blockchain, "
    "IoT, smart contracts, security, digital twins, machine learning, and AI."
)

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}
YEAR_PATTERN = re.compile(r"(?<!\d)(20\d{2})(?!\d)")


def parse_args() -> argparse.Namespace:
    script_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=script_dir / "outputs" / "figures",
        help="Directory containing yearly source images.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=script_dir / "outputs" / "videos" / OUTPUT_NAME,
        help="Destination MP4 path.",
    )
    parser.add_argument("--size", type=int, default=DEFAULT_SIZE, help="Square video size in pixels.")
    parser.add_argument("--fps", type=int, default=DEFAULT_FPS, help="Output frame rate.")
    parser.add_argument(
        "--keep-slides",
        action="store_true",
        help="Keep generated slide PNG files beside the output video.",
    )
    return parser.parse_args()


def require_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg is None:
        raise RuntimeError(
            "FFmpeg was not found. Install FFmpeg and ensure 'ffmpeg' is available on PATH."
        )
    return ffmpeg


def discover_year_images(input_dir: Path) -> list[tuple[int, Path]]:
    if not input_dir.is_dir():
        raise FileNotFoundError(f"Input directory does not exist: {input_dir}")

    by_year: dict[int, list[Path]] = {}
    for path in sorted(input_dir.iterdir()):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        match = YEAR_PATTERN.search(path.stem)
        if match:
            year = int(match.group(1))
            if START_YEAR <= year <= END_YEAR:
                by_year.setdefault(year, []).append(path)

    missing = [year for year in range(START_YEAR, END_YEAR + 1) if year not in by_year]
    duplicates = {year: files for year, files in by_year.items() if len(files) > 1}

    if missing:
        raise ValueError("Missing source image(s) for year(s): " + ", ".join(map(str, missing)))
    if duplicates:
        details = "; ".join(
            f"{year}: {', '.join(path.name for path in files)}"
            for year, files in sorted(duplicates.items())
        )
        raise ValueError(f"More than one source image was found for a year: {details}")

    return [(year, by_year[year][0]) for year in range(START_YEAR, END_YEAR + 1)]


def find_font(bold: bool, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = (
        [
            "C:/Windows/Fonts/arialbd.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        ]
        if bold
        else [
            "C:/Windows/Fonts/arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
            "/System/Library/Fonts/Supplemental/Arial.ttf",
        ]
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def fit_image(path: Path, size: int) -> Image.Image:
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
    return ImageOps.pad(
        image,
        (size, size),
        method=Image.Resampling.LANCZOS,
        color="white",
        centering=(0.5, 0.5),
    )


def draw_centered_multiline(
    draw: ImageDraw.ImageDraw,
    xy_y: int,
    text: str,
    font: ImageFont.ImageFont,
    canvas_width: int,
    spacing: int,
) -> None:
    bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=spacing, align="center")
    width = bbox[2] - bbox[0]
    draw.multiline_text(
        ((canvas_width - width) / 2, xy_y),
        text,
        fill="black",
        font=font,
        spacing=spacing,
        align="center",
    )


def make_card(size: int, title: str, subtitle: str) -> Image.Image:
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    title_font = find_font(bold=True, size=max(24, round(size * 0.044)))
    body_font = find_font(bold=False, size=max(18, round(size * 0.030)))

    draw_centered_multiline(draw, round(size * 0.29), title, title_font, size, spacing=10)
    wrapped = "\n".join(textwrap.wrap(subtitle, width=48))
    draw_centered_multiline(draw, round(size * 0.50), wrapped, body_font, size, spacing=8)
    return image


def add_year_label(image: Image.Image, year: int, size: int) -> Image.Image:
    result = image.copy()
    draw = ImageDraw.Draw(result)
    font = find_font(bold=True, size=max(24, round(size * 0.044)))
    label = str(year)
    bbox = draw.textbbox((0, 0), label, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    pad = round(size * 0.018)
    margin = round(size * 0.021)
    left = size - text_width - (2 * pad) - margin
    top = size - text_height - (2 * pad) - margin

    draw.rounded_rectangle(
        (left, top, size - margin, size - margin),
        radius=max(8, round(size * 0.016)),
        fill="white",
        outline="black",
        width=max(1, round(size * 0.003)),
    )
    draw.text((left + pad, top + pad - bbox[1]), label, font=font, fill="black")
    return result


def ffconcat_path(path: Path) -> str:
    return path.resolve().as_posix().replace("'", "'\\''")


def encode_video(
    ffmpeg: str,
    slides: list[tuple[Path, float]],
    output: Path,
    fps: int,
) -> None:
    concat_file = slides[0][0].parent / "slides.ffconcat"
    lines = ["ffconcat version 1.0"]
    for slide, duration in slides:
        lines.append(f"file '{ffconcat_path(slide)}'")
        lines.append(f"duration {duration:.3f}")
    lines.append(f"file '{ffconcat_path(slides[-1][0])}'")
    concat_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

    output.parent.mkdir(parents=True, exist_ok=True)
    command = [
        ffmpeg,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_file),
        "-vf",
        f"fps={fps},format=yuv420p",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "18",
        "-movflags",
        "+faststart",
        "-t",
        f"{sum(duration for _, duration in slides):.3f}",
        str(output),
    ]
    subprocess.run(command, check=True)


def build_video(args: argparse.Namespace) -> Path:
    if args.size <= 0 or args.fps <= 0:
        raise ValueError("--size and --fps must be positive integers.")

    ffmpeg = require_ffmpeg()
    sources = discover_year_images(args.input_dir.resolve())
    args.output = args.output.resolve()

    with tempfile.TemporaryDirectory(prefix="metaverse_2017_2020_") as temp_name:
        temp_dir = Path(temp_name)
        slides: list[tuple[Path, float]] = []

        opening_path = temp_dir / "00_opening.png"
        make_card(args.size, TITLE, OPENING_SUBTITLE).save(opening_path)
        slides.append((opening_path, DEFAULT_OPENING_SECONDS))

        for index, (year, source_path) in enumerate(sources, start=1):
            slide_path = temp_dir / f"{index:02d}_{year}.png"
            add_year_label(fit_image(source_path, args.size), year, args.size).save(slide_path)
            slides.append((slide_path, DEFAULT_IMAGE_SECONDS))

        ending_path = temp_dir / "99_ending.png"
        make_card(args.size, ENDING_TITLE, ENDING_SUBTITLE).save(ending_path)
        slides.append((ending_path, DEFAULT_ENDING_SECONDS))

        encode_video(ffmpeg, slides, args.output, args.fps)

        if args.keep_slides:
            slide_output = args.output.parent / f"{args.output.stem}_slides"
            if slide_output.exists():
                shutil.rmtree(slide_output)
            shutil.copytree(temp_dir, slide_output)
            print(f"Slides: {slide_output}")

    duration = sum(duration for _, duration in slides)
    print(f"Created: {args.output}")
    print(f"Years: {START_YEAR}–{END_YEAR} ({len(sources)} images)")
    print(f"Duration: approximately {duration:.1f} seconds")
    print(f"Resolution: {args.size}×{args.size} at {args.fps} fps")
    return args.output


def main() -> int:
    try:
        build_video(parse_args())
    except (FileNotFoundError, ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
