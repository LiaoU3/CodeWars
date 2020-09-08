# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"


def domain_name(url):
    ans =''
    if url.find('www') != -1 :
        for letter in url[url.find('www') + 4:]:
            if letter != '.':
                ans += letter
            else:
                break
    elif url.find('://') != -1:
        for letter in url[url.find('://') + 3:]:
            if letter != '.':
                ans += letter
            else:
                break
    return ans

print(domain_name('https://www.cnet.com'))
print(domain_name("www.xakep.ru"))
print(domain_name("https://youtube.com"))