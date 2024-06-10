# Read the links from the file
with open('links-umexpert.txt', 'r') as file:
    urls = [url.strip() for url in file.readlines()]

# Add .html at the end of each URL
modified_urls = [url + '.html' for url in urls]

# Write the modified URLs back to the file or to a new file
with open('links-umexpert-modified.txt', 'w') as file:
    for url in modified_urls:
        file.write(url + '\n')

# Optionally, print the modified URLs to verify
for url in modified_urls:
    print(url)
