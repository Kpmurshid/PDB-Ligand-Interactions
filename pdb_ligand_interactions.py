import json
import csv

# Get JSON file name from user input
json_file = input("Enter the JSON file name: ").strip()

# Load JSON file
try:
    with open(json_file, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: File '{json_file}' not found.")
    exit()

# Extract PDB ID
pdb_id = list(data.keys())[0]  # Extract first key as PDB ID
ligand_info = data[pdb_id][0]["ligand"]  # Get ligand details
interactions = data[pdb_id][0]["interactions"]  # Get interaction details

# Use sets to store unique interactions per category
ligand_interactions = set()
metal_interactions = set()
water_interactions = set()

for interaction in interactions:
    residue_name = interaction["end"]["chem_comp_id"]
    residue_chain = interaction["end"]["chain_id"]
    residue_id = interaction["end"]["author_residue_number"]
    interaction_type = ", ".join(interaction["interaction_details"])  # Bond type as interaction

    # Create compact format
    ligand = f"{ligand_info['chem_comp_id']}:{ligand_info['chain_id']}:{ligand_info['author_residue_number']}"
    residue = f"{residue_name}:{residue_chain}:{residue_id}"

    interaction_tuple = (pdb_id, ligand, residue, interaction_type)

    # Categorize interactions (removing duplicates using sets)
    if residue_name in ["HOH", "WAT", "H2O"]:  # Water
        water_interactions.add(interaction_tuple)
    elif any(metal in residue_name for metal in ["MG", "ZN", "FE", "CA", "CU", "NI", "MN"]):  # Metals
        metal_interactions.add(interaction_tuple)
    else:  # Ligands (default category)
        ligand_interactions.add(interaction_tuple)

# Merge ordered interactions: Ligands → Metals → Water
ordered_interactions = list(ligand_interactions) + list(metal_interactions) + list(water_interactions)

# Output file name based on PDB ID
csv_file = f"{json_file}_interactions.csv"

# Save to CSV
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["PDB_ID", "Ligand", "Residue", "Interaction"])
    writer.writerows(ordered_interactions)

print(f"Ordered & deduplicated binding site data saved to {csv_file}")

