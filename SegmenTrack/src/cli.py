import argparse
from csv_data_loader import CSVDataLoader
from data_processor import DataProcessor
from visualizer import Visualizer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--segment", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    loader = CSVDataLoader()
    processor = DataProcessor()
    visualizer = Visualizer()
    reporter = ReportGenerator()

    df = loader.load(args.input)
    loader.validate(df)

    segments = processor.segment(df, args.segment)

    analysis_results = {
        name: processor.analyze(seg_df)
        for name, seg_df in segments.items()
    }

    plots = visualizer.plot_segments(analysis_results, "output")

    reporter.generate_report(analysis_results, plots, args.output)

    print("✅ Report generated successfully")

if __name__ == "__main__":
    main()
