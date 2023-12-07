import session
import environment
import output
import blacklist
import file_op

e = environment.Environment()

username = e.get_username()
password = e.get_password()

# senders = file_op.read_csv('blacklist.csv')
senders = ['trabajos_co@computrabajo.com']

gmail_session = session.Session(username, password)
deleted_emails = gmail_session.delete_emails(senders)
output.print_file(deleted_emails)
