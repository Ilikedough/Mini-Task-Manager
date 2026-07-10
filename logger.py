import logging


def setup_logger(name, filename = "log.log"):


    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(filename)

    formatter = logging.Formatter("%(asctime) - %(filename) - %(funcName) - %(levelname) - %(message)")

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    console_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if logger.handlers:
        return logger
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger