from youtube.models import Search
from youtube.schemas import (SearchOptionalParameters, SearchPart,
                             YouTubeRequest, YouTubeResponse)

from ..extensions import youtube_client


def get_playlists(query: str, max_results: int = 10) -> list[dict]:
    part: SearchPart = SearchPart()
    optional: SearchOptionalParameters = SearchOptionalParameters(
        q=query, type=["playlist"], maxResults=max_results
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=part, optional_parameters=optional
    )
    response: YouTubeResponse = youtube_client.search(search_schema=search_schema)
    items: list[Search] = response.items
    res: list[dict] = []
    for item in items:
        res.append(
            {
                "title": item.title,
                "description": item.description,
                "url": f"https://www.youtube.com/playlist?list={item.resource_id}",
            }
        )
    return res
