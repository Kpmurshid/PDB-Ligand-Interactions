# PDB Ligand Interactions Extractor

## Overview
This Python script extracts and categorizes ligand-binding site interactions from a JSON file containing PDB interaction data. The output is saved as a CSV file with ordered, deduplicated binding site information.

## Features
- Extracts ligand interactions from a JSON file.
- Categorizes interactions into ligand, metal, and water interactions.
- Deduplicates interactions to ensure clean output.
- Saves results in a structured CSV format.

## Requirements
- Python 3.x

## Installation
Clone the repository and navigate to the project directory:

```sh
# Clone the repository
git clone https://github.com/Kpmurshid/PDB-Ligand-Interactions.git
cd PDB-Ligand-Interactions
```

## Usage
1. Prepare a JSON file with interaction data.
2. Run the script and provide the JSON file name when prompted:

```sh
python extract_interactions.py
```

3. The script will generate an output CSV file named `{PDB_ID}_interactions.csv`.

## Output Format
The CSV file will contain the following columns:

| PDB_ID | Ligand | Residue | Interaction |
|--------|--------|---------|-------------|
| 2XCT   | LIG:A:101 | ASP:B:45 | Hydrogen Bond |
| 2XCT   | LIG:A:101 | HOH:A:300 | Water Bridge |


## License
This project is licensed under the MIT License.

## Author
[**Muhammed Murshid KP**](https://github.com/Kpmurshid)

