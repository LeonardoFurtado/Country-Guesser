def get_country(city, file):
    """Through the name of the city, find your country."""
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if(city == row[0] or city == row[1] or city == row[2] or
               city == row[3]):
                return row[2]
    return "Undefined"
