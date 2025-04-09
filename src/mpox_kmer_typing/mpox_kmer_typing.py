#!/usr/bin/env python3

"""Main script for kmer typing a new sequence.
Input: Fastq or fasta. NB: Paired fastq inputs need to be combined before
being input into this script.
Output: tsv mash result file, clade designation, confidence in designation
and required actions
"""

import logging
import os
import sys
import analytics.kmer_typing_functions as ktf
from mpox_kmer_typing.logfile import set_up_logger
from mpox_kmer_typing.directories import set_up_log_folder
from analytics.processing import check_ref_sketch, check_input_file, create_seq_sketch, check_mash_file_status
from mpox_kmer_typing.commands import get_args

from analytics.kmer_typing_functions import create_sequence_sketch


def main():
    """
    Main method for kmer typing mpox sequences (fastq or fasta) to clade and sub-clade.
    """
    # init parameters
    src = sys.path[0]
    exitcode = 0
    args = get_args()

    # Get sample name from fasta file
    sample_name = '.'.join(os.path.split(args.input)[1].split(".")[:-1])
    # setup directories
    out_file, err_file = set_up_log_folder(args, sample_name)
    set_up_logger(out_file, err_file)

    logging.info("Starting mpox kmer typing. Args received: %s", str(args))

    # Check if reference sketch is specified
    check_ref_sketch(src, args)
    # Check input file exists
    exitcode = check_input_file(args, exitcode)

    # create_sequence_sketch(args.input)
    # Create sequence sketch - specify min copies of kmer to reduce likelihood of errors
    sequence_file, exitcode = create_seq_sketch(args, exitcode)
    # Run mash dist
    mash_file = ktf.run_mash_dist(sequence_file, args.refsketch)
    # check mash file created
    check_mash_file_status(mash_file, exitcode)
    # Tidy mash dataframe
    mash_df = ktf.tidy_mash_df(mash_file)
    # Check clade difference
    pivot_df = ktf.get_clade_difference(mash_df)
    # Extract top hits
    top_hits = ktf.extract_top_hits(mash_df, args.output)
    return exitcode


if __name__ == "__main__":
    sys.exit(main())
