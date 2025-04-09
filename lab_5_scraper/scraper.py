"""
Crawler implementation.
"""
import os
# pylint: disable=too-many-arguments, too-many-instance-attributes, unused-import, undefined-variable, unused-argument
import pathlib
from typing import Pattern, Union
from core_utils.config_dto import ConfigDTO
from core_utils.constants import ASSETS_PATH, CRAWLER_CONFIG_PATH
import requests
# from bs4 import BeautifulSoup
# import datetime


class IncorrectSeedURLError(Exception):
    pass


class NumberOfArticlesOutOfRangeError(Exception):
    pass


class IncorrectNumberOfArticlesError(Exception):
    pass


class IncorrectHeadersError(Exception):
    pass


class IncorrectEncodingError(Exception):
    pass


class IncorrectTimeoutError(Exception):
    pass


class IncorrectVerifyError(Exception):
    pass


class Config:
    """
    Class for unpacking and validating configurations.
    """

    def __init__(self, path_to_config: pathlib.Path) -> None:
        """
        Initialize an instance of the Config class.

        Args:
            path_to_config (pathlib.Path): Path to configuration.
        """
        if not isinstance(path_to_config, pathlib.Path):
            raise TypeError
        self.path_to_config = path_to_config
        self._extract_config_content()

    def _extract_config_content(self) -> ConfigDTO:
        """
        Get config values.

        Returns:
            ConfigDTO: Config values
        """
        with open(self.path_to_config, 'r', encoding='utf-8') as config_file:
            config_dict = config_file.read()
            if not isinstance(config_dict, dict):
                raise TypeError("inappropriate type of input arguments")
        config = ConfigDTO(config_dict['seed_urls'],
                           config_dict['total_articles_to_find_and_parse'],
                           config_dict['headers'],
                           config_dict['encoding'],
                           config_dict['timeout'],
                           config_dict['should_verify_certificate'],
                           config_dict['headless_mode'])
        return config

    def _validate_config_content(self) -> None:
        """
        Ensure configuration parameters are not corrupt.
        """
        config = self._extract_config_content()
        if not all(isinstance(url, str) for url in config.seed_urls) or ...:
            raise IncorrectSeedURLError
            # тут будет регулярка в if, когда разберусь что это и с чем это едят
        if config.total_articles not in range(1, 151):
            raise NumberOfArticlesOutOfRangeError
        if not isinstance(config.total_articles, int) or config.total_articles < 0:
            raise IncorrectNumberOfArticlesError
        if not isinstance(config.headers, dict):
            raise IncorrectHeadersError
        if not isinstance(config.encoding, str):
            raise IncorrectEncodingError
        if not isinstance(config.timeout, int) or config.timeout <= 0 or config.timeout >= 60:
            raise IncorrectTimeoutError
        if not isinstance(config.should_verify_certificate, bool):
            raise IncorrectVerifyError

    def get_seed_urls(self) -> list[str]:
        """
        Retrieve seed urls.

        Returns:
            list[str]: Seed urls
        """
        seed_urls = self._extract_config_content().seed_urls
        return seed_urls

    def get_num_articles(self) -> int:
        """
        Retrieve total number of articles to scrape.

        Returns:
            int: Total number of articles to scrape
        """
        num_articles = self._extract_config_content().total_articles
        return num_articles

    def get_headers(self) -> dict[str, str]:
        """
        Retrieve headers to use during requesting.

        Returns:
            dict[str, str]: Headers
        """
        headers = self._extract_config_content().headers
        return headers

    def get_encoding(self) -> str:
        """
        Retrieve encoding to use during parsing.

        Returns:
            str: Encoding
        """
        encoding = self._extract_config_content().encoding
        return encoding

    def get_timeout(self) -> int:
        """
        Retrieve number of seconds to wait for response.

        Returns:
            int: Number of seconds to wait for response
        """
        timeout = self._extract_config_content().timeout
        return timeout

    def get_verify_certificate(self) -> bool:
        """
        Retrieve whether to verify certificate.

        Returns:
            bool: Whether to verify certificate or not
        """
        verify_certificate = self._extract_config_content().should_verify_certificate
        return verify_certificate

    def get_headless_mode(self) -> bool:
        """
        Retrieve whether to use headless mode.

        Returns:
            bool: Whether to use headless mode or not
        """
        headless_mode = self._extract_config_content().headless_mode
        return headless_mode


def make_request(url: str, config: Config) -> requests.models.Response:
    """
    Deliver a response from a request with given configuration.

    Args:
        url (str): Site url
        config (Config): Configuration

    Returns:
        requests.models.Response: A response from a request
    """
    if not isinstance(url, str) or not isinstance(config, Config):
        raise TypeError
    response = requests.get(url,
                            headers=Config.get_headers(),
                            timeout=Config.get_timeout(),
                            verify=Config.get_verify_certificate())
    return response


class Crawler:
    """
    Crawler implementation.
    """

    #: Url pattern
    url_pattern: Union[Pattern, str]

    def __init__(self, config: Config) -> None:
        """
        Initialize an instance of the Crawler class.

        Args:
            config (Config): Configuration
        """

    def _extract_url(self, article_bs: BeautifulSoup) -> str:
        """
        Find and retrieve url from HTML.

        Args:
            article_bs (bs4.BeautifulSoup): BeautifulSoup instance

        Returns:
            str: Url from HTML
        """

    def find_articles(self) -> None:
        """
        Find articles.
        """

    def get_search_urls(self) -> list:
        """
        Get seed_urls param.

        Returns:
            list: seed_urls param
        """


# 10
# 4, 6, 8, 10


class HTMLParser:
    """
    HTMLParser implementation.
    """

    def __init__(self, full_url: str, article_id: int, config: Config) -> None:
        """
        Initialize an instance of the HTMLParser class.

        Args:
            full_url (str): Site url
            article_id (int): Article id
            config (Config): Configuration
        """

    def _fill_article_with_text(self, article_soup: BeautifulSoup) -> None:
        """
        Find text of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def _fill_article_with_meta_information(self, article_soup: BeautifulSoup) -> None:
        """
        Find meta information of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def unify_date_format(self, date_str: str) -> datetime.datetime:
        """
        Unify date format.

        Args:
            date_str (str): Date in text format

        Returns:
            datetime.datetime: Datetime object
        """

    def parse(self) -> Union[Article, bool, list]:
        """
        Parse each article.

        Returns:
            Union[Article, bool, list]: Article instance
        """


def prepare_environment(base_path: Union[pathlib.Path, str]) -> None:
    """
    Create ASSETS_PATH folder if no created and remove existing folder.

    Args:
        base_path (Union[pathlib.Path, str]): Path where articles stores
    """
    try:
        base_path.mkdir(exist_ok=False)
    except FileExistsError:
        if os.listdir(base_path):
            base_path.rmdir()
            base_path.mkdir()
        else:
            pass
    except AttributeError:
        if not isinstance(base_path, str):
            raise TypeError
        new_path = pathlib.Path(base_path)
        new_path.mkdir()


def main() -> None:
    """
    Entrypoint for scrapper module.
    """
    configuration = Config(path_to_config=CRAWLER_CONFIG_PATH)
    prepare_environment(ASSETS_PATH)


if __name__ == "__main__":
    main()
# Hello, dear mentor!