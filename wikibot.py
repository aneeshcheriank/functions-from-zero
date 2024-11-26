import wikipedia
import click


@click.group()
def cli():
    # placeholder to define the CLI group
    pass


@cli.command()  # attach scrape as a commad to cli
@click.option(
    "--name",
    default="Microsoft",
    help="Name to search on Wikipedia",
    prompt="Wikipedia page to scrape",
)
@click.option(
    "--length", default=1, type=int, help="Number of sentences for the summary"
)
def scrape(name, length):
    result = wikipedia.summary(name, sentences=length)
    print(result)
    return result


if __name__ == "__main__":
    cli()
    # python wikibot.py scrape --name Microsoft --length 1
