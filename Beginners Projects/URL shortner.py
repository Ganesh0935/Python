import pyshorteners
def shorten_url(url):
    s = pyshorteners.Shortener()
    shorten_url = s.tinyurl.short(url)
    return shorten_url

#Example usage:
original_url = "https://www.youtube.com/watch?v=H7rJ2EIyZYU"
S_url = shorten_url(original_url)
print("Original URL:",original_url)
print("Shortened URL:",S_url)