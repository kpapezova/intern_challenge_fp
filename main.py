## name of csv file: mentees_list.csv
import mentee
import json

# refactoring

"""Load mentees from csv"""
csv_file = "mentees_list.csv"
users = mentee.Mentee(csv_file)
print(users.data)

## or user can input the name of csv
# csv_input = input("Insert a name of csv file: ")
# users = mentee.Mentee(csv_input)
# print(users.data)

"""Get a number of all mentees"""
number_of_mentees = users.num_of_mentees
print(number_of_mentees)


"""Set of all languages that mentees know"""
all_lang = users.languages
print(users.languages)

"""Preparation of full names"""
names = users.full_names
print(names)

'''

full_names = user.prep_fullname(loaded_data)        # prepare list of full names of all mentees

avg_length = user.get_average(full_names)
# print(f"An average length of mentees full names is {avg_length} characters.")

longest_length, l_name = user.get_longest(full_names)
# print(f"The longest full name has this user: {l_name} with {longest_length} characters.") 

shortest_length, s_name = user.get_shortest(full_names)
# print(f"The shortest full name has this user {s_name} with {shortest_length} characters.")


#  Report
report_data = {"number of mentees" : number_of_mentees, "languages" : list(languages), "average full name length" : avg_length, "longest length full name/s" : (longest_length, l_name), "shortest length full name/s" : (shortest_length, s_name)}


if __name__ == "__main__":
    with open("report.json", "w") as f:
        json.dump(report_data, f, indent=4)

'''