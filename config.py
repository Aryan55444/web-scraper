APP_TITLE = "Web Scraper Pro"
APP_ICON = "🕷️"
APP_VERSION = "1.0.0"

DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
DEFAULT_TIMEOUT = 10
MIN_TIMEOUT = 5
MAX_TIMEOUT = 60

SCRAPE_OPTIONS = [
    "All Text",
    "Links",
    "Images",
    "Tables",
    "Headings",
    "Metadata",
    "Paragraphs",
    "HTML Source",
    "HTML Elements",
    "Code Snippets"
]

EXPORT_FORMATS = ["JSON", "CSV", "TXT", "HTML"]

TEST_WEBSITES = {
    "Quotes to Scrape": "https://quotes.toscrape.com",
    "Books to Scrape": "https://books.toscrape.com",
    "Example.com": "https://example.com",
    "HTTPBin HTML": "https://httpbin.org/html",
    "Scrape This Site": "https://scrapethissite.com"
}

REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

ERROR_MESSAGES = {
    403: {
        "title": "🚫 Access Forbidden",
        "message": "This website is blocking scraping requests.",
        "tips": [
            "Try one of the test websites listed below",
            "The website has anti-scraping protection",
            "Check the website's robots.txt and Terms of Service",
            "Consider using an API if available"
        ]
    },
    404: {
        "title": "❌ Page Not Found",
        "message": "The requested page could not be found.",
        "tips": [
            "Verify the URL is correct",
            "Check for typos in the web address",
            "The page may have been moved or deleted"
        ]
    },
    429: {
        "title": "⏸️ Too Many Requests",
        "message": "Rate limit exceeded.",
        "tips": [
            "Wait a moment before trying again",
            "Don't scrape too aggressively",
            "The server is protecting itself from overload"
        ]
    },
    500: {
        "title": "⚠️ Server Error",
        "message": "The website's server encountered an error.",
        "tips": [
            "Try again later",
            "The website may be experiencing issues",
            "Not a problem with the scraper"
        ]
    }
}
