import pytest
from click.testing import CliRunner
from wikibot import cli


@pytest.fixture
def cli_runner():
    """Fixture to create a CliRunner instance."""
    return CliRunner()


# simple test
def test_wikibot():
    runner = CliRunner()
    # Specify the subcommand 'scrape' followed by its options
    # cli expect scrape since scrape is the fucntion name and it is the command
    result = runner.invoke(cli, ["scrape", "--name", "Microsoft", "--length", 1])
    assert result.exit_code == 0
    assert "Microsoft" in result.output


# pylint: disable=redefined-outer-name
def test_scrape_with_defaults(cli_runner, mocker):
    """Test the scrape command with default arguments."""
    # Mock the wikipedia.summary function to avoid actual API calls
    mock_wikipedia = mocker.patch(
        "wikibot.wikipedia.summary", return_value="Mock summary for Microsoft."
    )

    result = cli_runner.invoke(cli, ["scrape"])

    # Assertions
    assert result.exit_code == 0  # Command runs successfully
    mock_wikipedia.assert_called_once_with("Microsoft", sentences=1)
    assert "Mock summary for Microsoft." in result.output


# pylint: disable=redefined-outer-name
def test_scrape_with_custom_arguments(cli_runner, mocker):
    """Test the scrape command with custom arguments."""
    mock_wikipedia = mocker.patch(
        "wikibot.wikipedia.summary", return_value="Mock summary for Python."
    )

    result = cli_runner.invoke(cli, ["scrape", "--name", "Python", "--length", "2"])

    # Assertions
    assert result.exit_code == 0
    mock_wikipedia.assert_called_once_with("Python", sentences=2)
    assert "Mock summary for Python." in result.output


# pylint: disable=redefined-outer-name
def test_scrape_prompt(cli_runner, mocker):
    """Test the scrape command when user is prompted for input."""
    mock_wikipedia = mocker.patch(
        "wikibot.wikipedia.summary", return_value="Mock summary for Django."
    )

    result = cli_runner.invoke(cli, ["scrape"], input="Django\n")

    # Assertions
    assert result.exit_code == 0
    mock_wikipedia.assert_called_once_with("Django", sentences=1)
    assert "Mock summary for Django." in result.output


# pylint: disable=redefined-outer-name
def test_scrape_invalid_length(cli_runner):
    """Test the scrape command with invalid length."""
    result = cli_runner.invoke(
        cli, ["scrape", "--length", "abc"]
    )  # Invalid input for --length

    # Assertions
    assert result.exit_code != 0  # Command should fail
    assert "Error" in result.output
    assert "Invalid value for '--length': 'abc' is not a valid integer" in result.output
