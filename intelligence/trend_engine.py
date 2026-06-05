import pandas as pd

def get_trends(df):
    """
    Count how many events exist in each category.
    """

    trends = df["Category"].value_counts()

    return trends