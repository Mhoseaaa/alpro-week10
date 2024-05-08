def count_emails(filename):
    email_counts = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From:'):
                email = line.split()[1]
                email_counts[email] = email_counts.get(email, 0) + 1
    return email_counts

filename = input("Masukkan nama file: ")
email_counts = count_emails(filename)
print(email_counts)