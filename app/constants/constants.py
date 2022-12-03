API_BASE_URL = 'https://api.mangadex.org/'
ORG_BASE_URL = 'https://mangadex.org/'

GET_SEASONAL_UPDATES = f'{API_BASE_URL}list/4be9338a-3402-4f98-b467-43fb56663927?includes[]=user'
GET_RECENTLY_UPDATED = f'{API_BASE_URL}chapter?includes[]=manga&includes[]=scanlation_group&translatedLanguage[' \
                       f']=en&contentRating[]=safe&contentRating[]=suggestive&contentRating[]=erotica&order[' \
                       f'readableAt]=desc&offset=0&limit=24'

GET_RECENTLY_ADDED = f'{API_BASE_URL}manga?limit=30&contentRating[]=safe&contentRating[]=suggestive&' \
                     'contentRating[]=erotica&order[createdAt]=desc&includes[]=cover_art'


def GET_COVER_URL(manga_id: str) -> str:
    return f'{API_BASE_URL}cover?limit=1&offset=0&manga%5B%5D={manga_id}&order%5BcreatedAt%5D=' \
           f'asc&order%5BupdatedAt%5D=asc&order%5Bvolume%5D=asc'


MANGA_DETAILS_URL_BUILD = f'{API_BASE_URL}manga?includes[]=cover_art&order[followedCount]=desc' \
                          f'&contentRating[]=safe&contentRating[]=suggestive&contentRating[' \
                          f']=erotica&hasAvailableChapters=true&ids[]='


def IMAGE_URL(manga_id: str, image_url: str, bit: str = ".256.jpg") -> str:
    return f'{ORG_BASE_URL}covers/{manga_id}/{image_url}{bit}'


def PERTICULAR_MANGA(manga_id: str) -> str:
    return f'{API_BASE_URL}manga/{manga_id}?includes[]=artist&includes[]=author&includes[]=cover_art'


def GET_CHAPTERS(manga_id: str, limit: int = 96, offset: int = 0) -> str:
    return f'{API_BASE_URL}manga/{manga_id}/feed?translatedLanguage[]=en&limit={str(limit)}&includes[]=scanlation_group' \
           f'&includes[]=user&order[volume]=desc&order[chapter]=desc&offset={str(offset)}&contentRating[' \
           f']=safe&contentRating[]=suggestive&contentRating[]=erotica&contentRating[]=pornographic'


def GET_CHAPTER_IMAGES(chapter_id: str) -> str:
    return f'{API_BASE_URL}at-home/server/{chapter_id}?forcePort443=false'


def GET_CHAPTER_DETAIL(chapter_id: str) -> str:
    return f'{API_BASE_URL}chapter/{chapter_id}?includes[]=scanlation_group&includes[]=manga&includes[]=user'


def SEARCH_URL(title: str) -> str:
    return f'{API_BASE_URL}manga?title={title}&limit=5&contentRating[]=safe&contentRating[]=suggestive&contentRating[' \
           f']=erotica&includes[]=cover_art&order[relevance]=desc'
