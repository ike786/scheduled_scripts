from datetime import datetime, timedelta
import pytz
from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
    EWSDateTime, EWSTimeZone, Configuration, NTLM, GSSAPI, CalendarItem, Message, \
    Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
    HTMLBody, Build, Version, FolderCollection

credentials = Credentials(username='snellemantom\\i.vidler', password='66pilloA%')

version = Version(build=Build(14, 3, 123, 4))
config = Configuration(
    server='mail.snellemantom.com.au', credentials=credentials, version=version, auth_type=NTLM
)

my_account = Account(primary_smtp_address='i.vidler@snellemantom.com.au', credentials=credentials,
                     config=config, access_type=DELEGATE)

for item in my_account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.body, item.attachments)

