import application_process_functions as sql


def main():
    in_correct_input = True
    menu = {'1': sql.full_name, '2': sql.nick_name_of_mentors_from_miskol, '3': sql.contact_of_carol,
            '4': sql.contact_of_second_girl, '5': sql.insert_new_row, '6': sql.update_phone_number_of_jemima,
            '7': sql.delete_guys_who_has_that_email, '8': sql.list_everything_about_that_nick_name, 'q': 'exit'}
    while in_correct_input:
        print("")
        sql.menu_points()
        correct_input = input('Give me a number between 1-8: ')
        if correct_input == 'q':
            break
        elif correct_input in menu:
            if correct_input == '8':
                name = input("\nGive me a nick name:")
                menu[correct_input](name)
            else:
                menu[correct_input]()

if __name__ == '__main__':
    main()
