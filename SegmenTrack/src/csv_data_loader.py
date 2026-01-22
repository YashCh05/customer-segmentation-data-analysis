import pandas as pd
import os


class CSVDataLoader:
    """
    This class is responsible for:
    1. Loading a CSV file
    2. Validating whether the data is usable
    """

    def load(self, file_path: str) -> pd.DataFrame:
        """
        Load a CSV file from the given path and return a pandas DataFrame
        """

        # Step 1: Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found at path: {file_path}")

        # Step 2: Read CSV into DataFrame
        df = pd.read_csv(file_path)

        return df

    def validate(self, df: pd.DataFrame) -> bool:
        """
        Validate the loaded DataFrame
        """

        # Step 3: Check if DataFrame is empty
        if df.empty:
            raise ValueError("CSV file is empty. No data to analyze.")

        # Step 4: Check if DataFrame has columns
        if len(df.columns) == 0:
            raise ValueError("CSV file has no columns.")

        # If all checks pass, data is valid
        return True
