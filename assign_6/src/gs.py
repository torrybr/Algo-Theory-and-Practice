import sys
import time
from src import generate_problems
from src import stable_matching_helpers


def run_gale_shapley():



if __name__ == "__main__":
    start_time = time.process_time()
    input = generate_problems.parse_json_file(sys.argv[1])
    end_time = time.process_time()
    print("Ran in: {:.5f} secs".format(end_time - start_time))
