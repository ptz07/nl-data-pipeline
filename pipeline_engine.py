# pipeline_engine.py
# NL → Data pipeline engine
# Author: Pronit Ray

def generate_pipeline_code(instruction: str) -> str:
    """
    Converts a natural language instruction to Python code for data pipelines.
    Currently supports:
        - Loading CSV files
        - Merging datasets on common columns
        - Dropping missing values
        - Saving output CSV
    """

    # Split instruction into steps
    instruction_lower = instruction.lower()

    code_lines = [
        "# Auto-generated Python pipeline",
        f"# Original instruction: {instruction}",
        "import pandas as pd",
        "",
    ]

    # Detect CSV files mentioned
    import re
    csv_files = re.findall(r'\b\w+\.csv\b', instruction_lower)
    csv_vars = []

    for idx, csv_file in enumerate(csv_files):
        var_name = f"df{idx+1}"
        csv_vars.append(var_name)
        code_lines.append(f"{var_name} = pd.read_csv('{csv_file}')")

    # Merge if more than one CSV
    if len(csv_vars) >= 2:
        code_lines.append(f"\n# Merge datasets on common columns")
        merged_var = "df_merged"
        code_lines.append(f"{merged_var} = {csv_vars[0]}")
        for var in csv_vars[1:]:
            code_lines.append(f"{merged_var} = {merged_var}.merge({var}, how='inner')")
        final_var = merged_var
    elif len(csv_vars) == 1:
        final_var = csv_vars[0]
    else:
        final_var = None

    # Drop missing values if mentioned
    if "drop missing" in instruction_lower or "remove missing" in instruction_lower or "drop na" in instruction_lower:
        code_lines.append(f"\n# Remove missing values")
        if final_var:
            code_lines.append(f"{final_var} = {final_var}.dropna()")

    # Save output if mentioned
    output_match = re.search(r'save as (\w+\.csv)', instruction_lower)
    if output_match:
        output_file = output_match.group(1)
        if final_var:
            code_lines.append(f"\n# Save output to CSV")
            code_lines.append(f"{final_var}.to_csv('{output_file}', index=False)")
        else:
            code_lines.append(f"# No dataset to save, but instruction mentioned saving as {output_file}")

    code_lines.append("\nprint('Pipeline executed successfully!')")

    return "\n".join(code_lines)

