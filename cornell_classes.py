import google_service


def valid_class(department, number):
    """
    Checks to see if a provided department and class number actually
    exist at Cornell.
    Input:
    department - department prefix of a class
    number - class number
    """
    with open("cornell_classes.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip().lower()
            if department + " " + number == stripped_line:
                return True
        return False


def generate_class_output(department, number):
    """
    Generate text output of bot for a given class.
    Input:
    department - department prefix of a class
    number - class number
    """
    output = "Here is what I could find about " + \
        department.upper() + " " + number + ":\n\n"
    for p in google_service.find_posts(department, number, 5):
        output += p + "\n\n\n"
    output += "\nHere is a link to CUReviews: \n"
    output += "https://www.cureviews.org/course/" + \
        department.upper() + "/" + number + "\n\n\n"
    output += "Please note this is a beta version."
    return output
