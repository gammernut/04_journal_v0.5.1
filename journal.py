import os


def load(name):
    # add from file if it exists.
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('./journals/', name + '.jrl'))
    print(f"......saving to: {filename}")
    file_output_string = open(filename, 'w')


def add_entry(text, journal_data):
    journal_data.append(text)
