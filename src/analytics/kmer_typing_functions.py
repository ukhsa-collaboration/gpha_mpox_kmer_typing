#!/usr/bin/env python3

import logging
import os
import subprocess
import pandas as pd


def create_sequence_sketch(fastq_file):
    """Creates sequence sketch for input file

    Arguments:
        input_file -- fasta or fastq input file
        output -- .msh file
    """

    sketch_file = os.path.join(fastq_file + ".msh")

    command = ["mash", "sketch", "-r",
               "-m", "2",
               "-k", "31",
               "-g", "197206",
               fastq_file
               ]

    subprocess.run(command, check=True, timeout=180)

    return sketch_file


def run_mash_dist(sequence_file, reference_sketch):
    """Runs mash dist on input file

    Arguments:
        sequence_file -- .msh file (fastq input) or .fasta file (fasta input)
        reference_sketch -- reference sketch file - default = orthpox reference set
    Output: tsv file with mash distance results
    """
    sequence_name = os.path.splitext(sequence_file)[0]

    mash_file = os.path.join(sequence_name + ".mash_dist.tsv")

    command = ["mash", "dist",
               reference_sketch, sequence_file]

    with open(mash_file, "w", encoding="utf-8") as outfile:
        subprocess.run(command, check=True, timeout=180, stdout=outfile)

    return mash_file


def tidy_mash_df(mash_file: str) -> pd.DataFrame:
    """Tidy and add columns needed for analysis to mash df

    Arguments:
        mash_file -- raw mash out file (.tsv)
    Outputs:
        Updated mash tsv file with columns added
    """

    mash_df = pd.read_csv(mash_file, sep="\t", header=None)

    mash_df.rename(columns={0: "Sketch", 1: "Sample", 2: "Distance", 3: "P-Value",
                            4: "Matches"},
                   inplace=True)
    mash_df['Clade'] = mash_df['Sketch'].str.split(pat="[0-9]_").str[-1]
    matches = mash_df['Matches'].str.split(pat="/", expand=True)
    mash_df['Proportion Matching Kmers'] = matches[0].astype(float) / matches[1].astype(float)
    mash_df.sort_values(by="Proportion Matching Kmers", inplace=True, ascending=False)

    return mash_df


def get_clade_difference(mash_df: pd.DataFrame) -> pd.DataFrame:
    """If top hit comes back as clade I or II reference, calculate the
    difference between the two references to get an indication of
    confidence in clade designation.

    Arguments:
        mash_df -- Tidied mash dataframe
    Outputs:
        Difference in value between Clade I and Clade II.

    """

    pivot_df = mash_df.pivot(index="Sample", columns="Sketch",
                             values="Proportion Matching Kmers")

    pivot_df['Difference'] = pivot_df['NC_003310.1_Mpox_virus_CladeI'] - pivot_df['NC_063383.1_Monkeypox_virus_CladeII']
    pivot_df = pivot_df.reset_index()

    return pivot_df


def extract_top_hits(mash_df, outdir: str):
    """Extract top match for each 

    Arguments:
        mash_df -- tidied mash dataframe
        outdir -- path to output folder
    """
    top_hit_file = os.path.join(outdir, "top_hits.csv")
    mash_df.sort_values(by=["Sample", "Proportion Matching Kmers"],
                        ascending=[True, False], inplace=True)
    top_hit_file = mash_df.groupby("Sample", as_index=False).nth[:1]
    top_hit_file.to_csv(top_hit_file)

    return top_hit_file
