import psycopg2
import os


def database(indicator):
    try:
        # setup connection string
        connect_str = "dbname='atti' user='atti' host='localhost' password='asdf1234'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # set autocommit option, to do every query when we call it
        conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # run a SELECT statement
        cursor.execute(indicator)
        # Fetch and print the result of the last execution
        rows = cursor.fetchall()
        for row in rows:
            print(" ".join(map(str, row)))
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def full_name():
    return database("""SELECT CONCAT(first_name,' ',last_name) FROM mentors;""")


def nick_name_of_mentors_from_miskol():
    return database("""SELECT nick_name FROM mentors WHERE city='Miskolc';""")


def contact_of_carol():
    return database("""SELECT CONCAT(first_name,' ',last_name,' - ',phone_number)
                    AS full_name FROM applicants WHERE first_name='Carol';""")


def contact_of_second_girl():
    return database("""SELECT CONCAT(first_name,' ',last_name,' - ',phone_number)
                    AS full_name FROM applicants WHERE email LIKE '%adipiscingenimmi.edu';""")


def insert_new_row():
    return database("""INSERT INTO applicants(first_name,last_name,phone_number,email,application_code)
                    SELECT 'Markus','Schaffarzyk','003620/725-2666','djnovus@groovecoverage.com',54823
                    WHERE NOT EXISTS(SELECT application_code FROM applicants WHERE
                    applicants.application_code=54823);""")


def update_phone_number_of_jemima():
    return database("""UPDATE applicants SET phone_number='003670/223-7459'
                    WHERE first_name = 'Jemima' and last_name = 'Foreman';""")


def delete_guys_who_has_that_email():
    return database("""SELECT first_name,last_name FROM applicants
                WHERE email LIKE '%mauriseu.net';""")


def list_everything_about_that_nick_name(name):
    return database("""SELECT * FROM
                    mentors WHERE nick_name='{0}';""".format(name))


def menu_points():
    print("1. List full names of mentors.")
    print("2. List nick names of mentors in Miskolc.")
    print("3. List contact details of 'Carol'.")
    print("4. Contact about a girl who has a hat and her e-mail ends with '@adipiscingenimmi.edu'.")
    print("5. Add new contact.")
    print("6. Update phone number of Jamima.")
    print("7. Delete row where e-mail ends with 'mauriseu.net'.")
    print("8. Show everythink about that nick name")
    print("Enter 'q' to exit")


def menu():
    pass


def main():
    menu()


if __name__ == '__main__':
    main()