import unicodedata as uni

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def remove_accents_and_title(input_string):
    # Remove accents
    normalized_string = uni.normalize('NFD', input_string).encode('ascii', 'ignore').decode('utf-8')
    
    # Capitalize first word (title case)
    title_case_string = normalized_string.title()
    
    return title_case_string