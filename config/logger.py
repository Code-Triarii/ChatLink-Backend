import logging

def get_logger() -> logging.Logger:
    """
    Function to instanciate the logger component.

    Parameters
    ----------
    - N/A

    Returns
    ----------
    - logger (logging.Logger): logger object instance
    """

    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s: %(message)s',
        handlers=[logging.StreamHandler()]
    )

    return logging.getLogger(__name__)