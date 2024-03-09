def search(filename, text):
    with open(filename) as f:
        for line in f:
            if text in line:
                print(line)

search('test.txt', 'Failed')

# Joint Search

                                                                   
def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text in line and text2 in line:
                print(line)

search('test.txt', 'Failed', '108.65.113.83')