from app import app
import requests
from app.constants.constants import *
from flask import request, jsonify
from app import cache


@app.route("/get_seasonal_updates/", methods=['GET'])
@cache.cached()
def get_seasonal_updates():
    req = requests.get(GET_SEASONAL_UPDATES)
    return req.json()


@app.route("/get_recently_updated/", methods=['GET'])
@cache.cached()
def get_recently_updated():
    req = requests.get(GET_RECENTLY_UPDATED)
    response_data = req.json()
    result = {"data": []}
    seen_manga = set()
    for data in response_data["data"]:
        temp = {"attributes": data["attributes"],
                "id": data["id"],
                "relationships": data["relationships"][:]
                }
        for manga in data["relationships"]:
            if manga["type"] == "manga" and manga["id"] not in seen_manga:
                manga_details = requests.get(PERTICULAR_MANGA(manga_id=manga["id"]))
                manga_details_dict = manga_details.json()
                temp["attributes"]["title"] = manga_details_dict["data"]["attributes"]["title"][
                    list(manga_details_dict['data']["attributes"]["title"].keys())[0]
                ]
                seen_manga.add(manga["id"])
                result["data"].append(temp)
    result["data"] = result["data"][:24]
    return jsonify(result)


@app.route("/get_recently_added/", methods=['GET'])
def get_recently_added():
    req = requests.get(GET_RECENTLY_ADDED)
    return req.json()


@app.route("/get_cover/", methods=['GET'])
def get_cover():
    req = requests.get(GET_COVER_URL(request.args.get('manga_id')))
    return req.json()


@app.route("/get_manga_details/", methods=['POST'])
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
@cache.cached()
def get_particular_manga(manga_id: str, manga_title: str):
    print(manga_title)
    req = requests.get(PERTICULAR_MANGA(manga_id))
    return req.json()


@app.route("/get_chapters", methods=['GET'])
@cache.cached()
def get_chapters():
    manga_id = request.args.get("manga_id")
    limit = int(request.args.get('limit', default=96))
    offset = int(request.args.get('offset', default=0))

    req = requests.get(GET_CHAPTERS(manga_id, limit, offset))
    return req.json()


@app.route("/get_chapter_images", methods=['GET'])
@cache.cached()
def get_chapter_images():
    chapter_id = request.args.get('chapter_id')
    req = requests.get(GET_CHAPTER_IMAGES(chapter_id))
    return req.content


@app.route("/get_chapter_detail", methods=['GET'])
@cache.cached()
def get_chapter_detail():
    chapter_id = request.args.get('chapter_id')
    req = requests.get(GET_CHAPTER_DETAIL(chapter_id))
    return req.json()


@app.route("/search", methods=['GET'])
@cache.cached()
def search_url():
    title = request.args.get('title')
    print(SEARCH_URL(title))
    req = requests.get(SEARCH_URL(title))
    return req.json()
