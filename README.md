[![arXiv](https://img.shields.io/badge/arXiv-2406.13901-b31b1b.svg)](https://arxiv.org/abs/2406.13901)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15572006.svg)](https://doi.org/10.5281/zenodo.15572006)
[![GitHub release](https://img.shields.io/github/v/release/USCqserver/chadd-paper?include_prereleases&label=pre-release&logo=github)](https://github.com/USCqserver/chadd-paper/releases)

# Data Repository for "Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression"

Amy F. Brown and Daniel A. Lidar

## Description
This repository contains the aggregate data and notebooks to recreate the plots contained in the Chromatic-Hadamard Dynamical Decoupling (CHaDD) paper, "Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression," [![arXiv](https://img.shields.io/badge/arXiv-2406.13901-b31b1b.svg)](https://arxiv.org/abs/2406.13901).

This repository is archived on Zenodo at the following DOI: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15572006.svg)](https://doi.org/10.5281/zenodo.15572006).

The latest release and the history of releases can be found in the GitHub release archive: [![GitHub release](https://img.shields.io/github/v/release/USCqserver/chadd-paper?include_prereleases&label=pre-release&logo=github)](https://github.com/USCqserver/chadd-paper/releases).

## Installation
First, verify that you have Poetry installed and available in your `$PATH`.
Poetry can be installed from the command line by running
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
On MacOS, the `poetry` command can be added to your `$PATH` as follows:
```shell
export PATH="/Users/YOUR-USERNAME/.local/bin:$PATH"
```
To install `chadd-paper`, simply run the following command in the root repository directory:
```shell
poetry install
```
To install a Jupyter kernel for `chadd-paper`, run
```shell
poetry run python -m ipykernel install --user --name=chadd-paper
```

## Contents
```
github.com/USCqserver/chadd-paper
├── README.md
├── notebooks/
│   └── plot_chadd_experiments.ipynb  # recreate plots in the CHaDD paper
├── chadd/
│   └── __init__.py  # utilities relating to CHaDD
├── data/
│   └── aggregate/
│       └── ibm_brisbane/
│           ├── experiment_samples.pickle
│           └── params.yaml
├── pyproject.toml  # dependencies
└── poetry.lock
```

## Usage
To reproduce the plots contained in the CHaDD paper, run
```bash
jupyter notebook notebooks/plot_chadd_experiments.ipynb
```

## Funding Acknowledgement
This material is based upon work supported by, or in part by, the U.S. Army Research Laboratory and the U.S. Army Research Office under contract/grant number W911NF2310255.
This research was supported by the Office of the Director of National Intelligence (ODNI), Intelligence Advanced Research Projects Activity (IARPA) and the Army Research Office, under the Entangled Logical Qubits program through Cooperative Agreement Number W911NF-23-2-0216.

## Citation

Please cite the CHaDD preprint and data repository as follows:

> **Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression**  
> Amy F. Brown, Daniel A. Lidar  
> arXiv:2406.13901  
> DOI: [10.48550/arXiv.2406.13901](https://doi.org/10.48550/arXiv.2406.13901)

> **Data Repository for "Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression"**  
> Amy F. Brown, Daniel A. Lidar  
> DOI: [10.5281/zenodo.15572006](https://doi.org/10.5281/zenodo.15572006)

BibTeX:
```bibtex
@misc{brown2025efficientchromaticnumberbasedmultiqubitdecoherence,
    title={Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression},
    author={Amy F. Brown and Daniel A. Lidar},
    year={2025},
    eprint={2406.13901},
    archivePrefix={arXiv},
    primaryClass={quant-ph},
    doi={10.48550/arXiv.2406.13901},
    url={https://doi.org/10.48550/arXiv.2406.13901},
}
@software{amy_f_brown_2025_15572006,
    title={Data Repository for "Efficient Chromatic-Number-Based Multi-Qubit Decoherence and Crosstalk Suppression"},
    author={Amy F. Brown and Daniel A. Lidar},
    month=jun,
    year=2025,
    publisher={Zenodo},
    doi={10.5281/zenodo.15572006},
    url={https://doi.org/10.5281/zenodo.15572006},
}
```
