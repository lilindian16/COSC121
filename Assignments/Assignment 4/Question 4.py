def records_from_file(filename):
    
    """This RETURNS a list from a given file. Inside the list, each line 
    contains a tuple. This contains a tuple with information about the course 
    and a tuple containing information about the student. The course tuple
    contains the course code and its name as a string. The student tuple 
    contains the student name, family name as a string as well as their 
    ID number as an integer. For example, it would return
    (('ABC000', 'DEFGHIJ'), (123456, 'DEF', 'GHI'))
    """
    
    infile = open(filename)
    contents = infile.readlines()
    final_result = []
    for values_in_datasheet in contents[1: ]:
        result = values_in_datasheet.strip().split(',')
        course_tuple = tuple(result[0:2])
        student_id = int(result[2])
        first_name = result[3]
        last_name = result[4]
        student_tuple = (student_id, first_name, last_name)
        both_tuples_combined = (course_tuple, student_tuple)
        final_result.append(both_tuples_combined)
   
    return final_result


def all_courses(records):
    """This function takes the list of tuples from the function records_from_file
    returns a dictionary that maps the course code to the course name. The 
    course code is the key
    """
    
    course_and_id_dict = {}             #This creates an empty dictionary
    for all_tuples in records:
        course_info_tuple = all_tuples[0]       #Extracts all course information
        course_id = course_info_tuple[0]
        course_name = course_info_tuple[1]
        
        course_and_id_dict[course_id] = course_name
        
    return course_and_id_dict


def all_students(records):
    """This takes the list that was created by the function records_from_file.
    It then returns a dictionary that maps the student numbers as integers 
    to the student's name which is a tuple.
    """
    
    student_number_and_name = {}
    for each_tuple in records:
        all_student_information = each_tuple[1]
        student_number = int(all_student_information[0])
        student_name = (all_student_information[1:3])
        
        student_number_and_name[student_number] = student_name
        
    return student_number_and_name


def course_rolls(records):
    """This takes the list produced from the function records_from_file. Then 
    it returns a dictionary that maps the course codes to sets of sutudent 
    numbers. The key is the course code and the value is the student numbers.
    """
    
    dict_map_course_and_stud_num = {}
    
    for each_tuple in records:
        
        course_info = each_tuple[0]
        student_info = each_tuple[1]
        course_id = course_info[0]
        student_id = student_info[0]
        
        if course_id in dict_map_course_and_stud_num:
            dict_map_course_and_stud_num[course_id].add(student_id)
            
        else:
            dict_map_course_and_stud_num[course_id] = set()
            dict_map_course_and_stud_num[course_id].add(student_id)
    
    return(dict_map_course_and_stud_num)


            
        

    