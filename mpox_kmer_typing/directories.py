import os
from typing import Type
import logging


class TypeClass:
    """some class"""


def set_up_log_folder(args: [TypeClass], sample_name: str) -> [str, str]:
    # Set up log directory & files
    log_folder = os.path.join(args.output, "logs")

    if not os.path.exists(log_folder):
        os.mkdir(log_folder)

    out_file = os.path.join(log_folder, f"{sample_name}-mpox_kmer_typing.stdout")
    err_file = os.path.join(log_folder, f"{sample_name}-mpox_kmer_typing.stderr")
    return out_file, err_file



