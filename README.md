# Dead link checker with Firefox


# Getting Started

Check out available commands inside the `Makefile`.

Example:
```
make build
make run
```
then in another shell:
```
make exec
```

Check `app.py` for some examples of how to use Playwright to get screenshots, crawl the HTML rendered by JS and 
check if the href lead to successfull status codes.


# Motivation

The initial intent was to check for dead links on boto.io while running this container in a Lambda. Unfortunately, the container is quite heavy and slow; it uses 3GB of memory on my local and takes >10 seconds to run.


# Improvements
- make the `py` code async
- check different headless browsers


# References

https://github.com/george-lim/firefox-lambda

https://web.archive.org/web/20220524072235/https://playwright.dev/python/docs/api/class-elementhandle#element-handle-get-attribute

https://github.com/microsoft/playwright-python/blob/v1.12.0/playwright/sync_api/_generated.py