# src/data_processing/inspect_data.py

def inspect_dataframe(df, name):
    print("\n" + "="*50)
    print(f"{name} INFO")
    print("="*50)

    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())

    print("\nDtypes:\n", df.dtypes)

    print("\nMissing values:\n", df.isnull().sum())

    print("\nSample rows:\n", df.head())