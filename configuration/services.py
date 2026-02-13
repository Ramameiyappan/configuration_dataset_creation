import pandas as pd

def process_excel(file_path, config):
    df = pd.read_excel(file_path)

    if "filter" in config:
        for col, val in config["filter"].items():
            df = df[df[col] == val]

    if "group_by" in config and "aggregate" in config:
        df = df.groupby(config["group_by"]).agg(
            config["aggregate"]
        ).reset_index()

    return df