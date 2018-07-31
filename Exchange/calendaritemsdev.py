from exchangelib import DELEGATE, Account, Credentials, Configuration, NTLM, Build, Version, Attendee

credentials = Credentials(username='snellemantom\\i.vidler', password='66pilloA%')

version = Version(build=Build(14, 3, 123, 4))
config = Configuration(
    server='mail.snellemantom.com.au', credentials=credentials, version=version, auth_type=NTLM
)

my_account = Account(primary_smtp_address='m.kerrigan@snellemantom.com.au', credentials=credentials,
                     config=config, access_type=DELEGATE)

for item in my_account.calendar.all().order_by('-datetime_received')[:100]:
    try:
        if '@snellemantom.com.au' not in item.required_attendees \
                or 'boardroom' in item.required_attendees \
                or 'meetingroom' in item.required_attendees:
            attendees = []
            Subject = str(item.subject)
            Start = str(item.start)
            End = str(item.end)
            Location = str(item.location)
            for x in item.required_attendees:
                attendees.append(str(x.mailbox.name).replace(" | Snelleman Tom","").replace("'",""))
            print(Subject + " - " + Location + " - " + Start + " to " + End + " - " + " ".join(attendees))
    except:
        pass