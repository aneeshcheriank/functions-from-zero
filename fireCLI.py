import fire
import wikipedia


def scrape(name, length):
    result = wikipedia.summary(name, sentences=length)
    print(result)
    return result


if __name__ == "__main__":
    fire.Fire(scrape)
