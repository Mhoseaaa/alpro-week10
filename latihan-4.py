def count_email_domains(filename):
    email_domains = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('From '):
                email = line.split()[1]
                domain = email.split('@')[1]
                email_domains[domain] = email_domains.get(domain, 0) + 1
    return email_domains

filename = input("Masukkan nama file: ")
result = count_email_domains(filename)
print(result)