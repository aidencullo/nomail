import email_filter

import environment
import output

e = environment.Environment()

username = e.get_username()
password = e.get_password()

sender = "info@email.meetup.com"
                    
a_filter = email_filter.Filter(username, password)
emails = a_filter.delete_emails(sender)

output.print_file()
