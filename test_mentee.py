from mentee import Mentee

def test_import_Mentee():
    "Class Mentee can be imported"
    from mentee import Mentee


test_data = [{'index': 1, 'first_name': 'Lacy', 'last_name': 'Keefe', 'language': 'Romanian'}, {'index': 2, 'first_name': 'Luisa', 'last_name': 'Nagy', 'language': 'English'}, {'index': 3, 'first_name': 'Kristina', 'last_name': 'Pfeifer', 'language': 'Romanian'}, {'index': 4, 'first_name': 'Lars', 'last_name': 'Greene', 'language': 'Romanian'}]

test_names = ['Lacy Keefe', 'Luisa Nagy', 'Kristina Pfeifer', 'Lars Greene']

class TestMentee():
    
    def test_count_mentees(self):
        "Return the number of mentees"
        mt = Mentee()
        assert mt.count_mentees(test_data) == 4

    def test_spoken_languages(self):
        "Return a set of spoken languages"
        mt = Mentee()
        assert mt.spoken_languages(test_data) == {'Romanian', 'English'}

    def test_prep_fullname(self):
        "Return a dict with index as a key and full name as user"
        mt = Mentee()
        assert mt.prep_fullname(test_data) == test_names

    def test_get_average(self):
        "Return an average length of metees full names"
        mt = Mentee()
        assert mt.get_average(test_names) == 11

    def test_get_longest(self):
        "Return a longest full name"
        mt = Mentee()
        assert mt.get_longest(test_names) == (15, ['Kristina Pfeifer'])

    def test_get_shortest(self):
        mt = Mentee()
        assert mt.get_shortest(test_names) == (9, ['Lacy Keefe', 'Luisa Nagy'])
