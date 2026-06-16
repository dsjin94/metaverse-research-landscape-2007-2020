# Metaverse Research Landscape Evolution | 2007–2020

A reproducible Python project for visualizing and animating how Metaverse-related research structures changed from 2007 to 2020.

## Project Overview

This project presents one complete research arc in two periods:

### Part 1 — 2007–2016: The Virtual Worlds Era

Research centered on:

- virtual worlds
- simulation
- education
- rehabilitation
- virtual reality

### Part 2 — 2017–2020: The Infrastructure Transition

Research increasingly shifted toward:

- blockchain
- Internet of Things
- smart contracts
- digital twins
- machine learning
- artificial intelligence

Together, the two periods show the transition from virtual-world applications toward infrastructure-oriented Metaverse research.

## Purpose

The project transforms bibliographic and semantic-network results into reproducible visual outputs.

Its goals are to:

- document the historical evolution of Metaverse research
- visualize changing semantic structures
- preserve the original research workflow
- provide reusable code for future analysis and animation
- publish period-based video summaries derived from the yearly figures

## Reproducible Workflow

```text
Yearly semantic-network figures
        ↓
Python video-generation scripts
        ↓
Two period-based MP4 videos
```

The yearly figures are stored in `outputs/figures/`. The two root-level Python scripts read those figures, add opening and closing cards and yearly labels, and generate the final videos in `outputs/videos/`.

## Repository Structure

```text
metaverse-research-landscape-2007-2020/
├── 2007-2016.py
├── 2017-2020.py
├── README.md
├── pyproject.toml
├── rename_metaverse_figures.ps1
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── outputs/
│   ├── figures/
│   │   ├── metaverse_landscape_2007.jpeg
│   │   ├── ...
│   │   └── metaverse_landscape_2020.jpeg
│   ├── networks/
│   └── videos/
│       ├── Metaverse_Landscape_2007_2016.mp4
│       └── Metaverse_Landscape_2017_2020.mp4
└── src/
    └── metaverse_landscape/
        └── __init__.py
```

The local `prev/` directory contains earlier script versions and is intentionally excluded from GitHub through `.gitignore`.

## Requirements

- Python 3.10 or later
- Pillow
- FFmpeg available on the system `PATH`

Install Pillow:

```powershell
python -m pip install Pillow
```

Confirm that FFmpeg is available:

```powershell
ffmpeg -version
```

On Windows, FFmpeg can be installed with WinGet:

```powershell
winget install --id Gyan.FFmpeg -e
```

After installation, restart the terminal or Positron so the updated `PATH` is recognized.

## Generate the Videos

From the repository root, run:

```powershell
python .\2007-2016.py
python .\2017-2020.py
```

The scripts generate:

- `outputs/videos/Metaverse_Landscape_2007_2016.mp4`
- `outputs/videos/Metaverse_Landscape_2017_2020.mp4`

Default output specifications:

- resolution: 768 × 768
- frame rate: 30 fps
- 2007–2016 duration: approximately 20.5 seconds
- 2017–2020 duration: approximately 13.5 seconds

## Video Structure

Each video contains:

1. an opening title card
2. one figure for each year in the period
3. a year label on every figure
4. a closing interpretation card

### 2007–2016

Focus: virtual worlds, simulation, education, rehabilitation, and virtual reality.

### 2017–2020

Focus: blockchain, Internet of Things, smart contracts, security, digital twins, machine learning, and artificial intelligence.

## Output Policy

The public repository contains:

- reproducible Python scripts
- yearly JPEG figures
- final MP4 videos
- project documentation

The underlying restricted Web of Science data are not published. Public outputs are derived figures, videos, and reproducible presentation code rather than the original licensed bibliographic dataset.

## Project Scope

The project intentionally ends in 2020 because it reflects the period analyzed in the original research. It is presented as a complete historical arc rather than an artificially extended timeline.

## Series Statement

Part of **Metaverse Research Landscape Evolution | 2007–2020**, a two-part semantic-network visualization of how Metaverse-related research structures changed over time.
