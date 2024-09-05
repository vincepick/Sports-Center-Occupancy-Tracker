import re 

# program to extract the percentage value without the percentage sign using regex

def extractor(input_string):
    percentage = re.search(r'(\d+)%', input_string)
    if percentage:
# Extract the matched value (which is the percentage number)
        return percentage.group(1)




