from app import app
import requests
from app.constants.constants import *
from flask import request


@app.route("/get_seasonal_updates", methods=['GET'])
def get_seasonal_updates():
    req = requests.get(GET_SEASONAL_UPDATES)
    return req.json()


@app.route("/get_recently_updated", methods=['GET'])
def get_recently_updated():
    req = requests.get(GET_RECENTLY_UPDATED)
    return req.json()


@app.route("/get_recently_added", methods=['GET'])
def get_recently_added():
    req = requests.get(GET_RECENTLY_ADDED)
    return req.json()


@app.route("/get_cover", methods=['GET'])
def get_cover():
    req = requests.get(GET_COVER_URL(request.args.get('manga_id')))
    return req.json()


@app.route("/get_manga_details", methods=['POST'])
def get_manga_details_url():
    data = request.json
    url = MANGA_DETAILS_URL_BUILD

    for ids in data['ids']:
        url += ids + "&ids[]="

    req = requests.get(url[:-7])
    return req.json()


@app.route("/get_image_url", methods=['GET'])
def get_image_url():
    manga_id = request.args.get('manga_id')
    image_url = request.args.get('image_url')
    bit = request.args.get('bit', default=".256.jpg")
    print(IMAGE_URL(manga_id, image_url, bit))
    req = requests.get(IMAGE_URL(manga_id, image_url, bit))
    if req.status_code == 200:
        return req.content
    else:
        return req.content


@app.route("/manga/<manga_id>/<manga_title>/", methods=['GET'])
def get_particular_manga(manga_id: str, manga_title: str):
    print(manga_title)
    req = requests.get(PERTICULAR_MANGA(manga_id))
    return req.json()


@app.route("/get_chapters", methods=['GET'])
def get_chapters():
    manga_id = request.args.get("manga_id")
    limit = int(request.args.get('limit'))
    offset = int(request.args.get('offset'))

    req = requests.get(GET_CHAPTERS(manga_id, limit, offset))
    return req.json()


@app.route("/get_chapter_images", methods=['GET'])
def get_chapter_images():
    chapter_id = request.args.get('chapter_id')
    req = requests.get(GET_CHAPTER_IMAGES(chapter_id))
    return req


@app.route("/get_chapter_detail", methods=['GET'])
def get_chapter_detail():
    chapter_id = request.args.get('chapter_id')
    req = requests.get(GET_CHAPTER_DETAIL(chapter_id))
    return req.json()


@app.route("/search", methods=['GET'])
def search_url():
    title = request.args.get('title')
    req = requests.get(SEARCH_URL(title))
    return req.json()
