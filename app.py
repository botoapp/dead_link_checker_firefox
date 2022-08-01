import os

import requests
from playwright.sync_api import sync_playwright


# TODO: make it async
def test_urls(urls):
    for url in urls:
        try:
            resp = requests.get(url)
            resp.raise_for_status()

            print(f"{url} IS OK")
        except Exception as e:
            print(e)
            print(f"{url} FAILED!")


def run(playwright):
    firefox_path = os.environ.get("FIREFOX_PATH")
    browser = None

    try:
        browser = playwright.firefox.launch(
            executable_path=firefox_path, headless=False
        )

        page = browser.new_page()
        page.goto("https://boto.io")

        links = page.query_selector_all('a:visible')

        hrefs = [
            l.get_attribute("href") for l in links
        ]

        # close after all operations on the page.
        browser.close()

        external_hrefs = [
            h for h in hrefs if h[:4] == "http"
        ]

        return external_hrefs

    except Exception:
        if browser:
            browser.close()

        raise


def handler(event, context):
    with sync_playwright() as playwright:
        urls = run(playwright)
        test_urls(urls)
