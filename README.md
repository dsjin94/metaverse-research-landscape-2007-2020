# Metaverse Research Landscape Evolution | 2007–2020

A reproducible research-visualization project showing how Metaverse-related semantic structures evolved from 2007 to 2020.

The project connects archived research reports, yearly semantic-network figures, reproducible Python scripts, and two public video summaries.

## Project Overview

This project presents one complete research arc in two periods.

### Part 1 — 2007–2016: The Virtual Worlds Era

Research centered on:

* virtual worlds
* simulation
* education
* rehabilitation
* virtual reality

### Part 2 — 2017–2020: The Infrastructure Transition

Research increasingly shifted toward:

* blockchain
* Internet of Things
* smart contracts
* security
* digital twins
* machine learning
* artificial intelligence

Together, the two periods show a transition from immersive virtual-world applications toward connected, infrastructure-oriented Metaverse research.

## Research Foundation

The visualization project is derived from a broader 2023 study of Metaverse-related research indexed in Web of Science.

The full study analyzed 128,858 records associated with Metaverse-related concepts and examined:

* annual publication trends
* country-level research distribution
* disciplinary and research-field patterns
* author-keyword frequencies
* concept correlations
* semantic-network structures
* yearly changes in the Metaverse research landscape

The broader research period extends through 2022. This repository focuses specifically on **2007–2020**, the period selected for the two-part public visualization series.

See [`archive/README.md`](archive/README.md) for details about the reports and data-availability policy.

## Purpose

The project transforms bibliographic and semantic-network results into reproducible visual outputs.

Its goals are to:

* document the historical evolution of Metaverse research
* visualize changing semantic structures
* preserve the analytical and interpretive foundation
* provide reproducible Python-based presentation code
* publish period-based video summaries derived from yearly figures
* separate public analytical outputs from restricted source data

## Analytical and Visual Workflow

```text
Web of Science research records
        ↓
Text, frequency, correlation, and network analysis
        ↓
Yearly semantic-network figures
        ↓
Python video-generation scripts
        ↓
Two period-based MP4 videos
        ↓
Public research communication
```

The original research reports preserve the broader analytical context and R-based network workflow.

The Python scripts in this repository use the exported yearly figures to create the final public videos. They add:

* opening title cards
* yearly network frames
* visible year labels
* closing interpretation cards

## Repository Structure

```text
metaverse-research-landscape-2007-2020/
├── 2007-2016.py
├── 2017-2020.py
├── README.md
├── pyproject.toml
├── rename_metaverse_figures.ps1
├── archive/
│   ├── Metaverse_Network_Analysis_Trend_2007_2022.pdf
│   ├── metaverse-trend-report-2023.pdf
│   └── README.md
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

* Python 3.10 or later
* Pillow
* FFmpeg available on the system `PATH`

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

* `outputs/videos/Metaverse_Landscape_2007_2016.mp4`
* `outputs/videos/Metaverse_Landscape_2017_2020.mp4`

Default output specifications:

* resolution: 768 × 768
* frame rate: 30 fps
* 2007–2016 duration: approximately 20.5 seconds
* 2017–2020 duration: approximately 13.5 seconds

## Video Structure

Each video contains:

1. an opening title card
2. one semantic-network figure for each year
3. a visible year label on every figure
4. a closing interpretation card

### 2007–2016

**The Virtual Worlds Era**

Focus:

* virtual worlds
* simulation
* education
* rehabilitation
* virtual reality

### 2017–2020

**The Infrastructure Transition**

Focus:

* blockchain
* Internet of Things
* smart contracts
* security
* digital twins
* machine learning
* artificial intelligence

## Interpretation

The yearly networks show that Metaverse research did not begin as a single, unified technical domain.

During the earlier period, its structure was organized mainly around virtual environments, simulation, education, rehabilitation, and VR.

During the later period, the landscape increasingly incorporated blockchain, IoT, smart contracts, security, digital twins, machine learning, and AI.

The videos therefore represent a structural transition in the research landscape rather than only a sequence of annual images.

## Data and Publication Policy

The public repository contains:

* archived analytical reports
* reproducible Python scripts
* yearly semantic-network figures
* final MP4 videos
* project documentation

The repository does not contain:

* the underlying licensed Web of Science records
* private R data objects
* restricted intermediate bibliographic datasets

The public artifacts are aggregated research outputs, figures, documentation, and presentation code derived from the original analysis.

## Project Scope

The public visual series intentionally ends in 2020 because it represents the historical period selected for this project.

The wider archived analysis extends through 2022, but the two-video structure is presented as a complete interpretive arc:

```text
Virtual worlds and simulation
        ↓
Education, rehabilitation, and VR
        ↓
Blockchain and IoT
        ↓
Smart contracts and digital twins
        ↓
Machine learning and AI
```

The project is therefore not an artificially extended timeline. It is a focused visualization of a research transition that can be interpreted with confidence.

## Public Video Series

### Part 1

**Metaverse Research Landscape Evolution 1 | 2007–2016: The Virtual Worlds Era**

### Part 2

**Metaverse Research Landscape Evolution 2 | 2017–2020: The Infrastructure Transition**

Series statement:

> Part of **Metaverse Research Landscape Evolution | 2007–2020**, a two-part semantic-network visualization of how Metaverse-related research structures changed over time.

## Research-to-Publication Structure

```text
Archived research reports
        ↓
Analytical workflow
        ↓
Yearly semantic-network figures
        ↓
Reproducible Python scripts
        ↓
Period-based videos
        ↓
Public research visibility
```
