import pandas as pd


class DataProcessor:
    """
    This class is responsible for:
    1. Segmenting customer data based on a chosen column
    2. Calculating basic statistics for each segment
    """

    def segment(self, df: pd.DataFrame, by: str) -> dict:
        """
        Segment the DataFrame based on the selected column
        """

        # Step 1: Check if segmentation column exists
        if by not in df.columns:
            raise ValueError(f"Segmentation column '{by}' not found in the data")

        # Step 2: Group data by the selected column
        segments = {}
        for segment_name, segment_df in df.groupby(by):
            segments[str(segment_name)] = segment_df

        return segments

    def analyze(self, segment_df: pd.DataFrame) -> dict:
        """
        Calculate basic metrics for a single customer segment
        """

        # Step 3: Count customers in the segment
        analysis = {
            "customer_count": len(segment_df)
        }

        # Step 4: Calculate purchase-related metrics if available
        if "purchase_amount" in segment_df.columns:
            analysis["total_purchase"] = segment_df["purchase_amount"].sum()
            analysis["average_purchase"] = segment_df["purchase_amount"].mean()

        return analysis
