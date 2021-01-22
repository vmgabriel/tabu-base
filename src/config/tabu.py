"""
Configuration of algorith tabu
"""

# Libraries
import os
from dotenv import load_dotenv


# Load the process
load_dotenv(verbose=True)


configuration = {
    'tabu_duration': os.getenv('TABU_DURATION'),
    'iterations': os.getenv('TABU_ITERATIONS'),
    'distance_algorith': os.getenv('ALGORITH_DISTANCE'),
}
