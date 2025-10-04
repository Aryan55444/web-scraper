# 🕷️ Web Scraper Pro

> **Your friendly web scraping companion. Extract data from any website in seconds.**

A beautiful, easy-to-use web scraping tool with a stunning dark theme interface. No coding required - just enter a URL and click scrape!

## ✨ What Can It Do?

**Extract Everything You Need:**
- 📝 **Text** - Get all text content from any page
- 🔗 **Links** - Collect all URLs and link text
- 🖼️ **Images** - Grab image URLs and descriptions
- 📊 **Tables** - Parse HTML tables into clean data
- 📑 **Headings** - Extract titles and subtitles (H1-H6)
- 🏷️ **Metadata** - Get page titles, descriptions, and social media tags
- 📄 **Paragraphs** - Extract all paragraph content

**Export Your Way:**
- 💾 Download as JSON, CSV, TXT, or styled HTML
- 📈 Open in Excel, analyze in Python, or read as text
- 🎨 Beautiful HTML reports with custom styling

**Smart Features:**
- 🌙 **Dark Theme** - Easy on the eyes, looks professional
- 📜 **History** - Track every scraping session
- ⚙️ **Customizable** - Adjust timeouts, user agents, SSL settings
- 🚀 **Fast** - Get results in seconds

## 🚀 Getting Started

### Step 1: Install Dependencies

Open your terminal and run:
```bash
pip install -r requirements.txt
```

That's it! All the required packages will be installed automatically.

### Step 2: Run the App

**Easy way (Windows):**
Double-click `run.bat`

**Or use command line:**
```bash
streamlit run app.py
```

### Step 3: Start Scraping!

The app opens automatically in your browser at `http://localhost:8501`

**Your first scrape:**
1. Enter a URL (try: `https://quotes.toscrape.com`)
2. Choose what to extract (Text, Links, Images, etc.)
3. Click **Start Scraping**
4. View results and download if needed

## 🧪 Try These Test Websites

Perfect for testing (they won't block you!):
- **https://quotes.toscrape.com** - Quotes and authors
- **https://books.toscrape.com** - Book catalog with images
- **https://example.com** - Simple test page
- **https://httpbin.org/html** - HTML test page

⚠️ **Note**: Many modern sites (like social media) block scrapers. Always start with test sites!

## 💡 How It Works

**Simple 5-step process:**

1. **You enter a URL** → The app fetches the webpage
2. **HTML is received** → BeautifulSoup parses the structure
3. **Data is extracted** → Finds all the elements you selected
4. **Results are displayed** → Beautiful tables and cards show your data
5. **Export if needed** → Download in your preferred format

**Behind the scenes:**
- Makes HTTP request to the website
- Parses HTML using BeautifulSoup
- Extracts specific elements (links, images, text)
- Organizes data into clean format
- Displays in dark theme UI
- Exports to JSON/CSV/TXT/HTML

## 🎨 What Makes It Special?

**Dark Theme Throughout:**
Beautiful dark blue gradients make extended use comfortable on your eyes. Every element is designed for the dark theme.

**Modular Architecture:**
Clean code structure with separate files for UI, scraping logic, and data export. Easy to understand and extend.

**Smart Error Messages:**
If something goes wrong, you get helpful tips to fix it - not cryptic error codes.

## 🛠️ Built With

- Python & Streamlit
- BeautifulSoup (HTML parsing)
- Requests (HTTP)
- Pandas (data handling)

## ⚠️ Please Remember

✅ **Do**: Use for learning, research, personal projects  
✅ **Do**: Respect robots.txt and Terms of Service  
✅ **Do**: Be gentle on websites (don't spam requests)  

❌ **Don't**: Scrape copyrighted content for commercial use  
❌ **Don't**: Overwhelm small websites with requests  
❌ **Don't**: Ignore legal restrictions  

## ❓ Common Questions

**Q: Why does my scrape fail with 403 error?**  
A: The website is blocking scrapers. Try the test websites instead!

**Q: Can I scrape social media sites?**  
A: Most have strong anti-bot protection. Use their official APIs instead.

**Q: Is this legal?**  
A: Web scraping legality varies by location and use case. Always check local laws and website terms.

**Q: Can I scrape JavaScript-heavy sites?**  
A: Not with this tool. For React/Vue apps, you'd need Selenium or Playwright.

## 🚀 Quick Troubleshooting

- **Import errors?** → Run `pip install -r requirements.txt`
- **Port already in use?** → Streamlit will auto-pick another port
- **SSL errors?** → Disable SSL verification in advanced settings
- **Slow/timeout?** → Increase timeout in settings

---

## 💝 Final Notes

This project is built for education and ethical use. Happy scraping! 🕷️

**Made with ❤️ • Python • Streamlit • Dark Theme Magic ✨**
