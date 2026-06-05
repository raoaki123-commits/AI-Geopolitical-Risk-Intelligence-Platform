import pandas as pd

def add_event(
    date,
    country,
    event,
    category
):

    df = pd.read_csv(
        "data/events.csv"
    )

    new_row = pd.DataFrame(
        [{
            "Date": date,
            "Country": country,
            "Event": event,
            "Category": category
        }]
    )

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(
        "data/events.csv",
        index=False
    )