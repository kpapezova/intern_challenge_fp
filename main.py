## name of csv file: mentees_list.csv
import mentee
import json

# refactoring

user = mentee.Mentee()

loaded_data = user.load_mentee("mentees_list.csv")       # load users from csv

number_of_mentees = user.count_mentees(loaded_data)
# print(f"Number of mentees: {number_of_mentees}")

languages = user.spoken_languages(loaded_data)
# print(f"Set of all languages: {languages}")

full_names = user.prep_fullname(loaded_data)        # prepare list of full names of all mentees

avg_length = user.get_average(full_names)
# print(f"An average length of mentees full names is {avg_length} characters.")

longest_length, l_name = user.get_longest(full_names)
# print(f"The longest full name has this user: {l_name} with {longest_length} characters.") 

shortest_length, s_name = user.get_shortest(full_names)
# print(f"The shortest full name has this user {s_name} with {shortest_length} characters.")


#  Report
report_data = {"number of mentees" : number_of_mentees, "languages" : list(languages), "average full name length" : avg_length, "longest length full name/s" : (longest_length, l_name), "shortest length full name/s" : (shortest_length, s_name)}

with open("mentees_report.json", "w") as f:
    json.dump(report_data, f, indent=4)
