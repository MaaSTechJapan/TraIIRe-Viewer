import pandas as pd
from pandasgui import show

def show_parquet(fn: str):
    df = pd.read_parquet(fn)
    show(df)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Get Isochrone Map Data')
    parser.add_argument('fn', help='Target Parquet File')
    args = parser.parse_args()

    show_parquet(args.fn)
    