import os

import click

import requests
from bs4 import BeautifulSoup


def save_captions(prefix, user, caption_all):
    """
    Write a list of captions to files (one file per caption).
    :param prefix: The directory in which the files will be saved
    :param prefix: str
    :param user: Username of the account the posts' captions come from
    (will be used as a prefix in the filenames)
    :param user: str
    :param caption_all: A list of captions
    :param caption_all: list<str>
    :return: None
    """
    for idx, caption in enumerate(caption_all):
        filename = '{0}_{1}.txt'.format(user, idx)
        filename = os.path.join(prefix, filename)
        print('saving caption {0}'.format(filename))
        text_file = open(filename, 'w')
        text_file.write(caption)
        text_file.close()


def download_and_save_images(prefix, user, img_url_all):
    """
    Download and save a list of images from their urls.
    :param prefix: The directory in which the images will be saved
    :param prefix: str
    :param user: Username of the account the posts' images come from
    (will be used as a prefix in the filenames)
    :param user: str
    :param img_url_all: A list of image urls
    :param img_url_all: list<str>
    :return: None
    """
    for idx, img_url in enumerate(img_url_all):
        img_data = requests.get(img_url, verify=False).content
        filename = '{0}_{1}.jpg'.format(user, idx)
        filename = os.path.join(prefix, filename)
        print('saving image {0}'.format(filename))
        with open(filename, 'wb') as handler:
            handler.write(img_data)


@click.command()
@click.option('--images/--no-images', default=True,
              help='Scrap also images.')
@click.option('--captions/--no-captions', default=True,
              help='Scrap also captions.')
@click.option('--user', '-u', required=True,
              help='The account to scrap.')
@click.option('--number', '-n', default=10,
              help='Number of posts to scrap. (newer posts are scraped first).')
def scrap(images, captions, user, number):
    """
    Scrap photos and captions from posts of a single user.
    :param images: Include images in the data scraped
    :param images: boolean
    :param captions: Include captions in the data scraped
    :param captions: boolean
    :param user: The account to scrap
    :param user: str
    :return: None
    """
    BASE_URL = 'https://deskgram.org'
    SIG = "?_nc_ht=scontent-dfw5-1.cdninstagram.com"
    USER = user
    PATTERN_FOR_IMAGES = {'name': "div", 'attrs': {"class": "post-img"}}
    PATTERN_FOR_CAPTIONS = {'name': "div", 'attrs': {"class": "post-caption"}}
    DEST_FOLDER = './{0}'.format(USER)

    url = BASE_URL + '/' + USER
    img_url_all = list() if images else None
    caption_all = list() if captions else None

    if not os.path.exists(DEST_FOLDER):
        os.makedirs(DEST_FOLDER)

    while True:
        print('fetching {0}'.format(url))
        r = requests.get(url, verify=False)
        soup = BeautifulSoup(r.text, 'html.parser')

        if images:
            images = soup.findAll(**PATTERN_FOR_IMAGES)
            for image in images:
                img_url = image.img['src'].split('?')[0]
                img_url += SIG
                img_url_all.append(img_url)
                if len(img_url_all) == number and not captions:
                    break
            print('Found {0} images.'.format(len(images)))
            if len(img_url_all) == number and not captions:
                break

        if captions:
            captions = soup.findAll(**PATTERN_FOR_CAPTIONS)
            for caption in captions:
                caption_all.append(caption.text)
                print(len(caption_all))
                if len(caption_all) == number:
                    break
            print('Found {0} captions.'.format(len(captions)))
            if len(caption_all) == number:
                break

        links = soup.findAll('a')
        next_link = list(filter(lambda x: 'next_id' in x['href'], links))
        if len(next_link) == 0:
            break
        else:
            dest = next_link[0]['href']
            url = BASE_URL + dest

    if images:
        download_and_save_images(DEST_FOLDER, USER, img_url_all)

    if captions:
        save_captions(DEST_FOLDER, USER, caption_all)


if __name__ == '__main__':
    scrap()
