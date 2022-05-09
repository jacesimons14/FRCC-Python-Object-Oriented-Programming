import urllib.request, urllib.parse, urllib.error

link = input("input a link to scrape data from\n")

page = urllib.request.urlopen(link)

char_count = 0
para_count = 0

print_data = False

for line in page:
    if line == '':
        print_data = True
    while print_data:
        for char in line:
            char_count += 1
            if char == 'p':
                para_count += 1
        if char_count >= 3000:
            break
        print(line.decode().strip())

print("Char count: " + str(char_count))
print("Paragraph count: " + str(para_count))