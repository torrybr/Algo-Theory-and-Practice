import sys
import time
from src import generate_problems
from src import stable_matching_helpers


def run_gale_shapley(preferences):
    for i in range(len(preferences)):
        free_men = sorted(preferences[i][0].keys())
        engagements = {}
        while free_men:
            print("Testing Free Man "+ free_men[0])
            current_prefs = preferences[i][0].get(free_men[0])
            free_men.pop(0)
            print(current_prefs)

if __name__ == "__main__":
    preferences = generate_problems.parse_json_file(sys.argv[1])
    run_gale_shapley(preferences)