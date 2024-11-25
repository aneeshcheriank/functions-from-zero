import wikipedia
import click

def scrape(name='Microsoft', length=1):
    result = wikipedia.summary(name, sentences=length)
    return result

if __name__ == '__main__':
    print(scrape('Wikipedia'))