"""Method for saving and accessing student list"""

import pickle
from collections import Counter
import csv
from itertools import chain

students = [ {"name":"Jaayden","words":[],"review words": [], "reading strategy": [], "group": ""} ]

pickle.dump( students, open( "save.p", "wb" ) )

students = pickle.load( open( "save.p", "rb" ) )

students_path = './students.pkl'

def save_students(students):
    with open(students_path, 'wb') as fp:
        pickle.dump(students, fp)
        save_students(students)


def load_students():
    with open(students_path, 'rb') as fp:
        return pickle.load(fp)


def get_student_name_from_user():
    """gets student from use, returns student as student_name"""
    student_name = raw_input("Enter student name: ")
    return student_name


def get_word_from_user():
    """gets word from user input, returns word as new_word"""
    new_word = raw_input("Enter word: ")
    return new_word


def get_words_from_user():
    """gets list of new words separated by commas, returns list of words"""
    new_words = raw_input("Enter new words separated by commas: ")
    return new_words

def get_book_from_user():
    """gets book from user to be added to student dictionary"""
    book = raw_input("Enter new book: ")
    return book

def get_book_level_from_user():
    """gets book level from user to be added to student dictionary"""
    book_level = raw_input("Enter book level: ")
    return book_level

def get_student_reading_strategy():
    """gets reading strategy from user to be added to student dictionary"""
    student_reading_strategy = raw_input("Enter reading strategy: ")
    return student_reading_strategy

def get_student_group_from_user():
    """gets student reading group from user"""
    student_group = raw_input("Enter one letter for student reading group: ")
    student_group = student_group.upper()
    return student_group


def check_student_name_in_list(student_name):
    """checks if student is in dictionary, returns student names"""
    students = load_students()
    if any(student["name"] ==  student_name for student in students):
        return student_name
    else:
        print "Sorry, we couldn't find that student in your list."
        run_program()


def check_student_group_in_list(student_group):
    """checks if student is in dictionary, returns student names"""
    students = load_students()
    if any(student["group"] ==  student_group for student in students):
        return student_group
    else:
        print "Sorry, we couldn't find that group in your list."
        run_program()


def add_student(student_name):
  """Adds new student dictionary to student list"""
  students = load_students()
  students.append({'name': student_name, 'words': [], 'review words': [], 'reading strategy': [], 'books' : [], 'group': ""})
  print "{} has been added".format(student_name)
  save_students(students)



def remove_student(student_name):
  """Removes student from dictionary. Leaves empty dictionary"""
  students = load_students()
  for index, student in enumerate(students):
     if students[index]["name"] == student_name:
        students.pop(index)
        "{} has been removed".format(student_name)
        break
  save_students(students)


def remove_student_word(student_name, new_word):
  """Removes word from student dictionary."""
  students = load_students()
  for student in students:
      if student["name"] == student_name:
        student_words = student["words"]
        for words in student_words:
            student_words.remove(new_word)
            break
  print "{} has been removed from {}'s list.".format(new_word, student_name)
  save_students(students)


def remove_word_from_students(new_word):
  """Removes word from student dictionaries in list of students"""
  students = load_students()
  for student in students:
      if new_word in student["words"]:
        student["words"].remove(new_word)
      else:
          continue
  print "{} has been removed.".format(new_word)
  save_students(students)


def edit_student(student_name):
  """Prompts user to enter student name to be changed, replaces it with new student name"""
  students = load_students()
  for index, student in enumerate(students):
      if students[index]["name"] == student_name:
          new_student = raw_input("Enter new student: ")
          students[index]["name"] = new_student
          print "{} has been edited".format(new_student)
          break
  save_students(students)


def view_students():
  """Prints list of students"""
  students = load_students()
  for student in students:
    print "Name: {}".format(student["name"])


def view_students_words():
  """Prints list of words for all students"""
  students = load_students()
  for student in students:
    print student["name"]
    for words in student["words"]:
         print "    -{}".format(words)


def view_students_review_words():
  """Prints list of words for all students"""
  students = load_students()
  for student in students:
    for words in student["review words"]:
         print "    -{}".format(words)

def print_student_name():
  """Prints student name"""
  students = load_students()
  student_name = get_student_name_from_user()
  for student in students:
      if student_name == student["name"]:
         print student_name
  return student_name


def get_students_words():
    """ Return a set of all students' words. """
    students = load_students()
    return set(chain.from_iterable([student['words'] for student in students]))
    # return [student['words'] for student in students]



def print_student_words(student_name):
    """ Prints words for individual student. If student word list is empty, prints message saying that they have
    no new words to learn. IF student word list contains words, prints word list with message"""
    students = load_students()
    for student in students:
        if student["name"] == student_name:
            if student["words"] == []:
                    print "{} has no new words to learn!".format(student_name)
            else:
                print "{} is learning ".format(student_name)
                for words in student["words"]:
                    print "    -{}".format(words)

def count_words():
    """Prints how many words in student's word list by getting the length of that list"""
    students = load_students()
    for student in students:
      print "{} is learning {} words".format(student["name"], len(student['words']))


def count_each_word():
    """Counts the instances of a single word in all student dictionaries"""
    students = load_students()
    new_word = get_word_from_user()
    count = 0
    for student in students:
      if new_word in student["words"]:
          count += 1
    print "{} students are learning {}".format(count, new_word)


def split_new_words(new_words):
    """Splits words separated by commas for entry into student word list"""
    new_words = new_words.split(',')
    words = []
    for word in new_words:
       words.append(word.strip())
    return words


def add_word_to_students(new_word):
  """Adds new word to student dictionary in list of students"""
  students = load_students()
  for student in students:
    student["words"].append(new_word)
  print "{} has been added.".format(new_word)
  save_students(students)


def add_word_to_student(student_name, new_word):
    """ Adds single word to individual student"""
    students = load_students()
    for index, student in enumerate(students):
        if students[index]["name"] == student_name:
            students[index]["words"].append(new_word)
    print "{} has been added to {}'s words.".format(new_word, student_name)
    save_students(students)


def add_words_to_student(student_name, new_words):
    """Adds list of words to indivual student"""
    students = load_students()
    new_words = split_new_words(new_words)
    for index, student in enumerate(students):
        if students[index]["name"] == student_name:
            students[index]["words"].extend(new_words)
    save_students(students)


def add_words_to_students(new_words):
  """Adds new words to student dictionaries in list of students"""
  students = load_students()
  new_words = split_new_words(new_words)
  for student in students:
    student["words"].extend(new_words)
    save_students(students)


def get_student_review_words(student_name):
    """gets review words from student dictionary"""
    students = load_students()
    for student in students:
      if student["name"] == student_name:
        student_review_words = student["review words"]
        return student_review_words


def get_student_words(student_name):
    """gets words from student dictionary"""
    students = load_students()
    for student in students:
      if student["name"] == student_name:
        student_words = student["words"]
        return student_words


def add_reading_strategy_student(student_name):
    """ adds reading strategy to list of reading strategies in student dictionary."""
    students = load_students()
    student_reading_strategy = get_student_reading_strategy()
    for student in students:
        if student["name"] == student_name:
            student["reading strategy"].append(student_reading_strategy)
    save_students(students)

def add_reading_strategy_group(student_group):
    """ adds reading strategy to list of reading strategies in student dictionary."""
    students = load_students()
    student_reading_strategy = get_student_reading_strategy()
    for student in students:
        if student["group"] == student_group:
            student["reading strategy"].append(student_reading_strategy)
    save_students(students)

def remove_reading_strategy_student(student_name, student_reading_strategy):
  """Removes reading strategy from student dictionary by creating a new list that does not include word to be removed."""
  students = load_students()
  strategies_to_keep = []
  for student in students:
      if student["name"] == student_name:
        for strategies in student["reading strategy"]:
            if strategies != student_reading_strategy:
                strategies_to_keep.append(strategies)
        student["reading strategy"] = strategies_to_keep
  print "{} has been removed from {}'s reading strategies.".format(student_reading_strategy, student_name)
  save_students(students)


def print_reading_strategy_student(student_name):
    """prints most recent reading strategy for individiaul student. If student has no reading strategy, prints message
    that they have no strategies to learn right now."""
    students = load_students()
    for student in students:
        if student["name"] == student_name:
            if student["reading strategy"] == []:
                print "{} has no reading strategies to learn right now!".format(student_name)
            else:
                student_reading_strategy = (student["reading strategy"][-1]).lower()
    print"{} is working hard to {}".format(student_name, student_reading_strategy)

def print_reading_strategy_group(student_group):
    """prints most recent reading strategy for individiaul student. If student has no reading strategy, prints message
    that they have no strategies to learn right now."""
    students = load_students()
    for student in students:
        if student["group"] == student_group:
            if student["reading strategy"] == []:
                print "Students in group {} have no reading strategies to learn right now!".format(student_group)
            else:
                student_reading_strategy = (student["reading strategy"][-1]).lower()
    print"Students in group {} are working hard to {}".format(student_group, student_reading_strategy)
    print "\n"

def print_reading_strategies_all_students():
    """prints most recent reading strategy in student list for all students. If student has no reading strategy, prints message that they
    have no strategies to learn right now"""
    students = load_students()
    for student in students:
            if student["reading strategy"] == []:
                print "{} has no reading strategies to learn right now!".format(student["name"])
            else:
                student_reading_strategy = (student["reading strategy"][-1]).lower()
                print"{} is working hard to {}".format(student["name"], student_reading_strategy)

def print_reading_group(student_name):
    """prints student's current reading group"""
    students = load_students()
    for student in students:
        if student["name"] == student_name:
            print "{} is in group {}".format(student_name, student["group"])


def add_current_book_student(student_name):
    """adds book student is currently reading to current book list"""
    students = load_students()
    book = get_book_from_user()
    book_level = get_book_level_from_user()
    for student in students:
        if student["name"] == student_name:
            student["books"].append((book, book_level,))
    save_students(students)

def add_current_book_group(student_group):
    """adds book group of students is currently reading to current book list"""
    students = load_students()
    book = get_book_from_user()
    book_level = get_book_level_from_user()
    for student in students:
        if student["group"] == student_group:
            student["books"].append((book, book_level,))
    save_students(students)


def add_current_book_all():
    """adds book group of students is currently reading to current book list"""
    students = load_students()
    book = get_book_from_user()
    book_level = get_book_level_from_user()
    for student in students:
                student["books"].append((book, book_level,))
    save_students(students)


def print_current_book_student(student_name):
    """prints book and book level student is currently reading. If student has no book, prints message saying
    that they have no book right now"""
    students = load_students()
    for student in students:
        if student["name"] == student_name:
            if student["books"] == []:
                print "{} has no books right now!".format(student_name)
            else:
                print "{} is reading '{}', level {}".format(student_name, student["books"][-1][0], student["books"][-1][1])
    print "\n"

def print_current_book_group(student_group):
    """prints book and book level student is currently reading. If student has no book, prints message saying
    that they have no book right now"""
    students = load_students()
    for student in students:
        if student["group"] == student_group:
            if student["books"] == []:
                print "Students in group {} have no books right now!".format(student_group)
                break
            else:
                print "Students in  group {} are reading '{}', level {}".format(student_group, student["books"][-1][0], student["books"][-1][1])
                break
    print "\n"

def print_current_book_all():
    students = load_students()
    for student in students:
            if student["books"] == []:
                print "{} has no books right now!".format(student["name"])
            else:
                print "{} is reading '{}', level {}".format(student["name"], student["books"][-1][0], student["books"][-1][1])

def get_sight_words_group(student_group):
    """prints book and book level student is currently reading. If student has no book, prints message saying
    that they have no book right now"""
    students = load_students()
    group_words = []
    for student in students:
        if student["group"] == student_group:
            for word in student["words"]:
                if word not in group_words:
                    group_words.append(word)
    return group_words

def print_sight_words_group(group_words):
    students = load_students()
    print "Students are learning"
    for word in group_words:
        print "- {}".format(word)
    print "\n"

def print_list_of_students_who_dont_know_a_word(new_word):
    students = load_students()
    print new_word
    for student in students:
        if new_word in student["words"]:
            print student["name"]



# def remove_reading_book_student(student_name, book):
#   """Removes reading strategy from student dictionary by creating a new list that does not include word to be removed."""
#   students = load_students()
#   strategies_to_keep = []
#   for student in students:
#       if student["name"] == student_name:
#         for book in student["books"]:
#             if book != (book, book_level,):
#                 strategies_to_keep.append(strategies)
#         student["reading strategy"] = strategies_to_keep
#   print "{} has been removed from {}'s reading strategies.".format(student_reading_strategy, student_name)
#   save_students(students)

def assign_student_reading_group(student_name):
    students = load_students()
    student_group = get_student_group_from_user()
    for student in students:
        if student["name"] == student_name:
            student["group"] = student_group
    save_students(students)

def print_student_group(student_group):
    students = load_students()
    print "Group {}:".format(student_group)
    for student in students:
        if student["group"] == student_group:
            print student["name"]
    # print "\n"


def test_students():
  """displays each word in student list, adds word to review list if student knows word.
  Word remains in list if student does not know word"""
  students = load_students()
  student_name = get_student_name_from_user()
  check_student_name_in_list(student_name)
  student_words = get_student_words(student_name)
  student_review_words = get_student_review_words(student_name)
  new_review_list = []
  new_word_list = []
  for word in student_words:
    print word
    answer = raw_input("y/n? ")
    if answer == "n":
        new_word_list.append(word)
    elif answer == "y":
        new_review_list.append(word)
    else:
        print "Please enter y/n "
  for index, student in enumerate(students):
      if students[index]['name'] == student_name:
          students[index]['words'] = new_word_list
          students[index]['review words'].extend(new_review_list)
  save_students(students)



def get_review_list_for_display(student_review_words, student_name):

    """Removes duplicates from review words so students see the word only once when testing. Review word list contains duplicates to show how many times the
    student has successfully read that word. They do not need to read the duplicates on the test"""

    students = load_students()
    review_display = []
    student_review_words = get_student_review_words(student_name)
    for word in student_review_words:
        if word not in review_display:
            review_display.append(word)
    return review_display


def display_review_words(review_display):

  """Displays each instance of a word in student review words, adds it again to the list if student knows word.
  Creates new review word list that will be added to the old review word list."""

  students = load_students()

  new_word_list = []
  for word in review_display:
    print word
    answer = raw_input("y/n? ")
    if answer == "y":
      pass
    elif answer == "n":
       new_word_list += [word]
  return new_word_list


def test_review_words():

    """Tests students on their review words. Displays each word and creates a new review list containing the words the student successfully read.
    These words are added to the review list, increasing the count of those words in the list and indicating that the student has correctly read that word multiple times"""

    students = load_students()
    student_name = get_student_name_from_user()
    check_student_name_in_list(student_name)
    student_review_words = get_student_review_words(student_name)
    student_words = get_student_words(student_name)
    review_display = get_review_list_for_display(student_review_words, student_name)
    new_word_list = display_review_words(review_display)
    for index, student in enumerate(students):
      if students[index]["name"] == student_name:
          students[index]["words"].extend(new_word_list)
    save_students(students)


def get_review_list_count():

    """Counts the number of times a word is in the review word list. Each time a student correctly reads the review list word, it is added to the list again.
    Higher count means more times read successfully, the student knows that word well"""

    review_list_count = {}
    students = load_students()
    student_name = student_name = get_student_name_from_user()
    student_name = check_student_name_in_list(student_name)
    review_words = get_student_review_words(student_name)
    for word in review_words:
        if word in review_list_count:
            review_list_count[word] += 1
        else:
            review_list_count[word] = 1
    return review_list_count


def get_words_to_keep_from_review_list():
    """Determines if the words in review list have been sucessfully read 2 times. If so, they are added to the remove list"""
    students = load_students()
    words_to_keep = []
    review_list_count = get_review_list_count()
    for word in review_list_count:
        if review_list_count[word] < 2:
            words_to_keep.append(word)
    print words_to_keep
    return words_to_keep


def remove_words_from_review_list():
    """Replaces list of review words with review words that students are still working on,
    thereby removing words that students have successfully read 2 times as review words, and 3 times total"""
    students = load_students()
    student_name = get_student_name_from_user()
    check_student_name_in_list(student_name)
    words_to_keep = get_words_to_keep_from_review_list()
    for index, student in enumerate(students):
      if students[index]["name"] == student_name:
          students[index]["review words"] = words_to_keep
    save_students(students)


def make_csv2():
    students = load_students()
    with open('sight_word_tracker.csv', 'wb') as csvfile:
        sight_word_writer = csv.writer(csvfile, delimiter= ',')
        # print 'students', students
        cols = ['name'] + list(get_students_words())
        sight_word_writer.writerow(cols)
        for student in students:
            output = [student['name']]
            words = Counter(student['words'])
            for col in cols:
                output += [words[col]]
            sight_word_writer.writerow(output)


def load_csv(filepath='sight_word_tracker.csv'):
    def parse_student_row(row, cols):
        student_name = row[0]
        student_words = [word for idx, word in enumerate(cols) if row[idx] == 1]
        return {
            'name': student_name,
            'words': student_words
        }

    with open(filepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        print dir()
        cols = csvreader[0]
        students = [ parse_student_row(row, cols) for row in csvreader[1:] ]
    return students

def get_uncompleted_word_counts():
    students = load_students()
    counts = sum([Counter(student['words']) for student in students], Counter())
    print counts
    return counts

def run_program():

    main_menu = """
                Welcome to the Student Literacy Manager!

                Enter a choice:
                    1.  Edit students
                    2.  View student sight words
                    3.  Edit student sight words
                    4.  Test student sight words
                    5.  Guided reading
                    6.  Quit program

                """

    while True:
        print (main_menu)
        user_option = raw_input("Choose an option: ")


        if user_option == "1":
            print """
                    Edit students

                    Enter a choice:
                        1. Add new student
                        2. Delete student
                        3. Edit student
                        4. Back

                        """
            user_choice = raw_input("What would you like to do?: ")

            if user_choice == "1":
                student_name = get_student_name_from_user()
                add_student(student_name)


            elif user_choice == "2":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                remove_student(student_name)


            elif user_choice == "3":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                edit_student(student_name)


            elif user_choice == "4":
                run_program()


            else:
                print "Sorry, that's not an option..."


        elif user_option == "2":
            print  """
                    View students and student words

                    Enter a choice:
                        1. View students
                        2. View all student words
                        3. View individual student words
                        4. View individual review words
                        5. Show student word counts
                        6. View uncompleted word counts
                        7. Print group sight words
                        8. Print list of students who are learning a word
                        9. Back

                        """
            user_choice = raw_input("What would you like to do?: ")

            if user_choice == "1":
                 view_students()


            elif user_choice == "2":
                 view_students_words()


            elif user_choice == "3":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                print_student_words(student_name)


            elif user_choice == "4":
                view_students_review_words()


            elif user_choice == "5":
                count_words()


            elif user_choice == "6":
                get_uncompleted_word_counts()

            elif user_choice == "7":
                student_group = get_student_group_from_user()
                check_student_group_in_list(student_group)
                group_words = get_sight_words_group(student_group)
                print_sight_words_group(group_words)

            elif user_choice == "8":
                new_word = get_word_from_user()
                print_list_of_students_who_dont_know_a_word(new_word)

            elif user_choice == "9":
                run_program()


            else:
                print "Sorry, that's not an option..."



        elif user_option == "3":
            print """
                Edit student words

                Enter a choice:
                    1. Add word to individual student
                    2. Add word to all students
                    3. Add words to individual student
                    4. Add words to all students
                    5. Remove word from individual student
                    6. Remove word from all students
                    7. Clear learned words from review list
                    8. Back

            """

            user_choice = raw_input("What would you like to do?: ")

            if user_choice == "1":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                new_word = get_word_from_user()
                add_word_to_student(student_name, new_word)


            elif user_choice == "2":
                new_word = get_word_from_user()
                add_word_to_students(new_word)


            elif user_choice == "3":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                new_words = get_words_from_user()
                add_words_to_student(student_name, new_words)


            elif user_choice == "4":
                new_words = get_words_from_user()
                add_words_to_students(new_words)


            elif user_choice == "5":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                new_word = get_word_from_user()
                remove_student_word(student_name, new_word)



            elif user_choice == "6":
                new_word = get_word_from_user()
                remove_word_from_students(new_word)

            elif user_choice == "7":
                remove_words_from_review_list()

            elif user_choice == "8":
                run_program()

            else:
                 print "Sorry, that's not an option..."


        elif user_option == "4":
            print """
                Test student

                Enter a choice:
                    1. Test student words
                    2. Test student review words
                    3. Back
                    """
            user_choice = raw_input("What would you like to do?: ")

            if user_choice == "1":
                 test_students()

            elif user_choice == "2":
                 test_review_words()

            elif user_choice == "3":
                run_program()

        elif user_option == "5":

            print """
                Reading

                Enter a choice:
                    1. Assign student reading group
                    2  Print current book
                    3. Print reading strategy
                    4. Add new book
                    5. Add reading strategy
                    6. Remove reading strategy from student
                    7. Print student summary
                    8. Print group summary
                    9. Back
                    """

            user_choice = raw_input("What would you like to do?: ")

            if user_choice == "1":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                assign_student_reading_group(student_name)

            if user_choice == "2":
                user_option = raw_input("Print book for student, group, or all? ")
                if user_option == "student":
                    student_name = get_student_name_from_user()
                    check_student_name_in_list(student_name)
                    print_current_book_student(student_name)

                elif user_option == "group":
                    student_group = get_student_group_from_user()
                    check_student_group_in_list(student_group)
                    print_current_book_group(student_group)

                elif user_option == "all":
                    print_current_book_all()

            elif user_choice == "3":
                user_option = raw_input("Print strategy for student, group, or all? ")

                if user_option == "student":
                    student_name = get_student_name_from_user()
                    check_student_name_in_list(student_name)
                    print_reading_strategy_student(student_name)

                elif user_option == "group":
                    student_group = get_student_group_from_user()
                    check_student_group_in_list(student_group)
                    print_reading_strategy_group(student_group)

                elif user_option == "all":
                    print_reading_strategies_all_students()



            elif user_choice == "4":
                user_option = raw_input("Add book to student, group, or all? ")

                if user_option == "student":
                    student_name = get_student_name_from_user()
                    check_student_name_in_list(student_name)
                    add_current_book_student(student_name)

                elif user_option == "group":
                    student_group = get_student_group_from_user()
                    check_student_group_in_list(student_group)
                    add_current_book_group(student_group)

                if user_option == "all":
                    add_current_book_all()


            elif user_choice == "5":
                user_option = raw_input("Add strategy to student, or group? ")
                if user_option == "student":

                    student_name = get_student_name_from_user()
                    check_student_name_in_list(student_name)
                    add_reading_strategy_student(student_name)

                elif user_option == "group":

                    student_group = get_student_group_from_user()
                    check_student_group_in_list(student_group)
                    add_reading_strategy_group(student_group)



            elif user_choice == "6":
                user_option = raw_input("Remove strategy from student, group, or all? ")
                if user_option == "student":
                    student_name = get_student_name_from_user()
                    check_student_name_in_list(student_name)
                    student_reading_strategy = get_student_reading_strategy()
                    remove_reading_strategy_student(student_name, student_reading_strategy)

                # elif user_option == "group":
                #     student_group = get_student_group_from_user()
                #     check_student_group_in_list(student_group)
                #     remove_reading_strategy_group(student_group, student_reading_strategy)



            elif user_choice == "7":
                student_name = get_student_name_from_user()
                check_student_name_in_list(student_name)
                print_reading_group(student_name)
                print_current_book_student(student_name)
                print_reading_strategy_student(student_name)
                print_student_words(student_name)

            elif user_choice == "8":
                student_group = get_student_group_from_user()
                check_student_group_in_list(student_group)
                print_student_group(student_group)
                print_current_book_group(student_group)
                print_reading_strategy_group(student_group)
                group_words = get_sight_words_group(student_group)
                print_sight_words_group(group_words)

            elif user_choice == "9":
                run_program()

        elif user_option == "6":
                print "goodbye!"
                break


        else:
            print "Sorry, that's not an option..."

run_program()
# student_name = get_student_name_from_user()
# remove_student(student_name)
# save_students(students)
