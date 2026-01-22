import matplotlib.pyplot as plt
import os

class Visualizer:
    def plot_segments(self, analysis_results: dict, output_dir: str) -> list:
        os.makedirs(output_dir, exist_ok=True)

        segments = list(analysis_results.keys())
        values = [v.get("total_purchase", 0) for v in analysis_results.values()]

        plt.bar(segments, values)
        plt.xlabel("Segment")
        plt.ylabel("Total Purchase")
        plt.title("Total Purchase by Segment")

        path = os.path.join(output_dir, "segment_chart.png")
        plt.savefig(path)
        plt.close()

        return [path]
