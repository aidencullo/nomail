import mypackage.session as session
import environment
import output
import blacklist
import file_op

e = environment.Environment()

username = e.get_username()
password = e.get_password()
gmail_session = session.Session(username, password)

senders = file_op.read_csv('blacklist.csv')
senders = ['no-reply@spotify.com']

deleted_emails = gmail_session.move(senders)
