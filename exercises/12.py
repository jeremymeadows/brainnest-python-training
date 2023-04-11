# Read a mail archive and print the emails who sent a message. The useful lines
# start with `From: ` then contain the email address.
#
# Part 2: Count how many times each email address appears, and print out the one
# which appeats most frequently.
#
# Part 3: Count how many times each domain name appears, and print out the one
# which appears most frequently.

file = open(input('Enter a file name: '))

emails = [line.split()[1]
          for line in file.readlines() if line.startswith('From:')]
for email in emails:
    print('Sender:', email)
print('Total number of lines:', len(emails))

email_counts = {email: emails.count(email) for email in emails}
print(max(email_counts.items(), key=lambda i: i[1]))

domains = [email.split('@')[1] for email in emails]
domain_counts = {domain: domains.count(domain) for domain in domains}
print(max(domain_counts.items(), key=lambda i: i[1]))
