import pandas as pd


def generate_report(candidate_data):

    df = pd.DataFrame(candidate_data)

    df = df.sort_values(
        by="Score",
        ascending=False
    )

    return df