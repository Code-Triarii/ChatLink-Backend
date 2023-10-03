import yaml
from config.logger import get_logger
import os

def get_config() -> dict:
    """
    YAML configuration file processing function.

    Parameters
    ----------
    - N/A

    Returns
    ----------
    - parsed_config: returns the configuration parsed dict.

    """
    
    try:
        with open('config/config.yaml', 'r') as cfg_file:
            parsed_config = process_env_values(
                yaml.safe_load(
                    cfg_file
                )
            )
            return parsed_config
    except FileNotFoundError:
        get_logger().info(
            {
                'action': 'get_config',
                'error': 'FileNotFoundError',
                'cause': 'config file may not found'
            }
        )
    except:
        get_logger().info(
            {
                'action': 'get_config',
                'error': 'Unexpected',
                'cause': f'Unexpected error during config initialization'
            }
        )


def process_env_values(data: any) -> dict:
    """
    Function to process env values.

    Parameters
    ----------
    - data (dict, list and unexpected value): desired data to be processed.

    Returns
    ----------
    - replaced_data (dict): returns data with processed env values.

    """

    if isinstance(data, dict):
        replaced_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                replaced_data[key] = replace_env_values(value)
            elif isinstance(value, dict):
                replaced_data[key] = process_env_values(value)
            else:
                replaced_data[key] = value
        return replaced_data
    elif isinstance(data, list):
        return [process_env_values(item) for item in data]
    else:
        return data


def replace_env_values(value: str) -> str:
    """
    Function to replace the config values by the environment variables values.

    Parameters
    ----------
    - value (str): string which can be default values, env values or direct values.
    
    Returns
    ----------
    - value (str): returns the value of the environment variable or the default value.

    """
    value = value.split(':DEFAULT:')

    if len(value) > 1:
        if value[0].startswith('${') and value[0].endswith('}'):
            env_value = os.environ.get(value[0][2:-1])
            if env_value is not None:
                return env_value
            return value[1]
    if value[0].startswith('${') and value[0].endswith('}'):
        return os.environ.get(value[0][2:-1])
    
    return value[0]

