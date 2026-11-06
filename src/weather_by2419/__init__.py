# read version from installed package
from importlib.metadata import version
__version__ = version("weather_by2419")

from .weather_by2419 import (
    celsius_to_fahrenheit,
    summarize_temperatures,
    clean_readings,
)