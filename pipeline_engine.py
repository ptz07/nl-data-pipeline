def parse_instruction(instruction: str):
    steps = []
    instruction = instruction.lower()

    if "load" in instruction:
        if "sales.csv" in instruction:
            steps.append("Load sales.csv into dataframe")
        if "customers.csv" in instruction:
            steps.append("Load customers.csv into dataframe")
        if "csv" in instruction:
            steps.append("Load CSV file into dataframe")
        if "database" in instruction:
            steps.append("Connect to database and load table")

    if "remove missing" in instruction or "drop na" in instruction:
        steps.append("Remove rows with missing values")

    if "join" in instruction:
        steps.append("Join dataframes on common key")

    if "save" in instruction:
        if "csv" in instruction:
            steps.append("Save dataframe as CSV file")
        elif "parquet" in instruction:
            steps.append("Save dataframe as Parquet file")

    if not steps:
        steps.append("⚠️ No recognized steps found")

    return steps


def generate_python_code(steps):
    code_lines = ["import pandas as pd"]
    if "Load sales.csv into dataframe" in steps:
        code_lines.append("df = pd.read_csv('sales.csv')")
    if "Load customers.csv into dataframe" in steps:
        code_lines.append("df2 = pd.read_csv('customers.csv')")
    if "Join dataframes on common key" in steps:
        code_lines.append("df = df.merge(df2, on='customer_id', how='inner')")
    if "Remove rows with missing values" in steps:
        code_lines.append("df = df.dropna()")
    if "Save dataframe as CSV file" in steps:
        code_lines.append("df.to_csv('output.csv', index=False)")
    if "Save dataframe as Parquet file" in steps:
        code_lines.append("df.to_parquet('output.parquet', index=False)")
    return "\n".join(code_lines)
