import argparse
import os


def get_args():
    """Get command line arguments"""
    parser = argparse.ArgumentParser(
        prog="Mpox kmer typing", description="""Main script to
        type mpox sequences to clade and sub-clade using a kmer based
        approach."""
    )
    parser.add_argument("--type",
                        "-t",
                        type=str,
                        required=True,
                        choices=["fastq", "fasta"],
                        help="Specify input file type")
    parser.add_argument("--input",
                        "-i",
                        type=str,
                        required=True,
                        help="Path to input file")
    parser.add_argument("--output",
                        "-o",
                        type=str,
                        required=False,
                        default=os.getcwd(),
                        help="Output folder for results files")
    parser.add_argument("--refsketch",
                        "-r",
                        type=str,
                        required=False,
                        help="Path to reference sketch file")

    return parser.parse_args()
