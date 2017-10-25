import sys
import time
from src import generate_problems
<<<<<<< Updated upstream
from src import stable_matching_helpers


def run_gale_shapley(preferences):
=======
import json
from src import stable_matching_helpers


def write_json(obj, filename):
    with open(filename, mode='w') as f:
        json.dump(obj, f)


def run_gale_shapley(preferences, output_file_name):
    final_to_file = []
>>>>>>> Stashed changes
    for i in range(len(preferences)):
        free_men = sorted(preferences[i][0].keys()) # Turns into a list of free men by sorting
        engagements = {}
        while free_men:
<<<<<<< Updated upstream
            print("Testing Free Man "+ free_men[0])
            current_prefs = preferences[i][0].get(free_men[0])
            free_men.pop(0)
            print(current_prefs)

if __name__ == "__main__":
    preferences = generate_problems.parse_json_file(sys.argv[1])
    run_gale_shapley(preferences)
=======
            current_man = free_men.pop(0)
            # print("Testing Free Man " + "'" + current_man + "'")
            current_man_prefs = preferences[i][0].get(current_man)
            # print(current_man_prefs)
            # w = m's highest ranked such woman to whom he has not yet proposed, removes the woman from his list because
            # he has now proposed to her
            women = current_man_prefs.pop(0)

            # if women is not free
            if women in engagements:
                engaged_bro = engagements.get(women)
                current_womens_prefs = preferences[i][1].get(women)
                if current_womens_prefs.index(engagements.get(women)) > current_womens_prefs.index(current_man):
                    engagements[women] = current_man
                    free_men.append(engaged_bro)
            # print("the engagement stays")
            else:
                engagements[women] = current_man
                # print(engagements)
        final_to_file.append(stable_matching_helpers.inverse_dict(engagements))
    generate_problems.write_obj_to_json_file(output_file_name, final_to_file)




if __name__ == "__main__":
    #generate_problems.create_my_problems(3500)
    test = False
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    preferences = generate_problems.parse_json_file(input_file_name)
    start_time = time.process_time()
    run_gale_shapley(preferences, output_file_name)
    end_time = time.process_time()
    if test:
        my_file = "/Users/torrybrelsford/Documents/cs320/git/torrybr/assign_6/src/output.json"
        out = "/Users/torrybrelsford/Documents/cs320/git/torrybr/assign_6/output/big_prob_out.json"
        print(generate_problems.json_files_equal(my_file,
                                                 out))
    print("Ran in: {:.5f} secs".format(end_time - start_time))
>>>>>>> Stashed changes
