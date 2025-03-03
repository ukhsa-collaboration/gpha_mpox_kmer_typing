import os
from typing import Type
import logging
import analytics.kmer_typing_functions as ktf


class TypeClass:
    """some class"""


def check_ref_sketch(src: str, args: [TypeClass]):
    # Check if reference sketch is specified
    if args.refsketch is None:
        args.refsketch = os.path.join("data/k31_s1000_orthopox_refs_genomic_renamed.fna.msh")
        logging.info("No reference file specified, using default orthopox reference: %s",
                     args.refsketch)


def check_input_file(args: [TypeClass], exitcode: int):
    # Check input file exists
    try:
        os.path.exists(args.input)
        logging.info("Running kmer typing on input file: %s", args.input)
    except FileNotFoundError as err:
        logging.error("%s: Input file does not exist:  %s", err, args.input)
        exitcode = 2
    return exitcode


def process_fastq(args: [TypeClass], exitcode: int):
    sequence_file = ktf.create_sequence_sketch(args.input)
    try:
        os.path.exists(sequence_file)
        logging.info("Sketch file successfully created: %s", sequence_file)
    except FileNotFoundError as err:
        logging.error("%s: Sketch file not found:  %s", err, sequence_file)
        exitcode = 2
    return sequence_file, exitcode


def create_seq_sketch(args: [TypeClass], exitcode: int):
    # Create sequence sketch - specify min copies of kmer to reduce likelihood of errors
    if args.type == "fastq":
        sequence_file = process_fastq(args, exitcode)
        return sequence_file, exitcode
    # Set fasta as seq file if consensus input:
    elif args.type == "fasta":
        sequence_file = args.input
        return sequence_file, exitcode


def check_mash_file_status(mash_file, exitcode: int):
    try:
        os.path.exists(mash_file)
        logging.info("Mash results file successfully created: %s", mash_file)
    except FileNotFoundError as err:
        logging.error("%s: Mash file not found:  %s", err, mash_file)
        exitcode = 2
    return exitcode
