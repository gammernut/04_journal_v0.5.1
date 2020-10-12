import journal

import utill


def main():
    utill.print_header(code_name='Journal app')
    run_event_loop()


def run_event_loop():
    print('what do you want to do with your journal?')
    user_input_main_loop = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # []  # list()

    while user_input_main_loop != 'x':
        user_input_main_loop = input('\n[L]ist entries, [A]dd an entry, E[x]it: \n')
        user_input_main_loop = user_input_main_loop.lower().strip()

        if user_input_main_loop == 'l':
            list_entries(journal_data)
        elif user_input_main_loop == 'a':
            add_entries(journal_data)
        elif user_input_main_loop != 'x':
            print(f"sorry, we don't understand {user_input_main_loop}")

    print('done, goodbye.')
    journal.save(journal_name, journal_data)


def list_entries(journal_entry):  # journal_entry was data
    print('your entries: ')
    entries = reversed(journal_entry)
    for idx, entry in enumerate(entries):  # idx is index
        print(f'*[{idx + 1}]{entry} ')


def add_entries(journal_entry):
    text = input('Type your entry, <enter> to exit: \n')
    journal.add_entry(text, journal_entry)
    # journal_entry.append(text)


main()
