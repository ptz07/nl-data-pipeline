def generate_pipeline_code(instruction):
    """
    This function simulates generating Python data pipeline code
    based on natural language instructions.
    """

    code_lines = [
        "# Auto-generated Python data pipeline",
        "import pandas as pd",
        "import numpy as np",
        "",
        "# Your instruction: " + instruction
    ]

    # Simple parsing example (you can expand)
    if "load" in instruction.lower():
        code_lines.append("df = pd.read_csv('sales.csv')  # Example file")

    if "join" in instruction.lower():
        code_lines.append("df_customers = pd.read_csv('customers.csv')")
        code_lines.append("df = df.merge(df_customers, on='customer_id', how='left')")

    if "drop missing" in instruction.lower() or "remove missing" in instruction.lower():
        code_lines.append("df = df.dropna()")

    if "save" in instruction.lower():
        code_lines.append("df.to_csv('output.csv', index=False)")

    return "\n".join(code_lines)


