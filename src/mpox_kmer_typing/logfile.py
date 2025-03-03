import logging


def set_up_logger(stdout_file: str, stderr_file: str) -> logging.Logger:
    """Creates logger for component - all logging messages go to stdout
    log file, error messages also go to stderr log. If component runs
    correctly, stderr is empty.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")

    out_handler = logging.FileHandler(stdout_file, mode="w")
    out_handler.setFormatter(formatter)
    logger.addHandler(out_handler)

    err_handler = logging.FileHandler(stderr_file, mode="w")
    err_handler.setLevel(logging.ERROR)
    err_handler.setFormatter(formatter)
    logger.addHandler(err_handler)

    return logger
