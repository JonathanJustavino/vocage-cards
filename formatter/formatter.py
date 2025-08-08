import os
import pandas as pd
from tqdm import tqdm

script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(script_dir)
cards_folder = os.path.join(root_dir, 'spanish/dnf/csv')
bundle_path = os.path.join(root_dir, 'spanish/dnf/bundle', 'dnf_bundle.tsv')
formatted_bundle_path = os.path.join(root_dir, 'spanish/dnf/bundle', 'dnf_bundle.csv')

file_count = len(os.listdir(cards_folder))
files = [f"{n}.csv" for n in range(1, file_count + 1)]

files.remove('790.csv') # remove empty card


def read_files(file):
    file_path = f"{cards_folder}/{file}"
    if os.path.getsize(file_path) == 0:
        return
    df = None
    try:
        df = pd.read_csv(file_path, header=None)
        return df
    except pd.errors.ParserError:
        print("Parse Error")
        print(file)

def bundle_data():
    dfs = []
    df_column_length = []
    errors = []
    df_lens = []

    for file in tqdm(files):
        df = read_files(file)
        dfs.append(df)
        col_length = len(df.columns)
        df_column_length.append((file, col_length))
        df_lens.append((col_length, file))
        if col_length != 2:
            errors.append((file, col_length))
    if len(errors) > 0:
        print(errors)

    print("concatting")
    df = pd.concat(dfs, ignore_index=True)

    print(df)
    df.columns = ["German", "Spanish"]
    print(df)
    df.to_csv(bundle_path, sep='\t', index=False)


def read_bundle(file_path):
    return pd.read_csv(file_path, sep='\t')


def format_bundle(df: pd.DataFrame):
    df['German'] = df['German'].astype(str).str.replace(';', ',')
    df['Spanish'] = df['Spanish'].astype(str).str.replace(';', ',')
    df.to_csv(formatted_bundle_path, sep='\t', index=False)
    print(df)


def main():
    bundle_data()
    df = read_bundle(bundle_path)
    format_bundle(df)


if __name__ == '__main__':
    main()