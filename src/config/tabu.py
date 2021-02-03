"""
Configuration of algorith tabu
"""

# Libraries
import os
from dotenv import load_dotenv


# Load the process
load_dotenv(verbose=True)


configuration = {
    'tabu_duration': int(os.getenv('TABU_DURATION', '10')),
    'iterations': int(os.getenv('TABU_ITERATIONS', '700')),
    'distance_algorith': os.getenv('ALGORITH_DISTANCE'),
}
