# caption-gener8r

Training a neural network to generate Instagram captions for photos using a biggg set of scraped Instagram data

## THE ARTICLE
https://towardsdatascience.com/do-it-for-the-gram-instagram-style-caption-generator-4e7044766e34

![](article_ss.png)

## Data scraper: instagram-profilecrawl by Tim Grossman

Quickly crawl the information (e.g. followers, tags etc...) of an instagram profile. Automation Script for crawling information from ones instagram profile.  
Like e.g. the number of posts, followers, and the tags of the the posts

### Getting started
Just do:
```bash
git clone https://github.com/timgrossmann/instagram-profilecrawl.git
```

It uses selenium and requests to get all the information so install them with:
```bash
pip install -r requirements.txt
```

Install the proper `chromedriver` for your operating system.  Once you [download it](https://sites.google.com/a/chromium.org/chromedriver/downloads) just drag and drop it into `instagram-profilecrawl/assets` directory.

### How to use it
type this command in Terminal:
```bash
python3 crawl_profile.py username1 username2 ... usernameX
```

### Special variables that worked well for us
In `util/settings.py`, we made the following changes:
* change variable `limit_amount` to 100
* change variable `sleep_time_between_post_scroll` to 3 or 4 depending on wifi strength
* change variable `sleep_time_between_comment_loading` to 0.5 if you do not need comment data, 3 if you do

### Optional login
If you want to scrape private users (profiles) whom you follow:
1. Open Settings.py
2. Search for `login_username` & `login_password`
3. Put your information inside the quotation marks

Second option:
just the settings to your script
```python
Settings.login_username = 'my_insta_account'
Settings.login_password = 'my_password_xxx'
```

### If you need more information about how to work the profile crawler, please visit the OG GitHub Repo (https://github.com/timgrossmann/instagram-profilecrawl)

## Dependencies
* `selenium`
* `netwulf`
* `networkx`
* `emoji`
* `pyenchant`
* `keras`
* `tensorflow`
* `PIL`
