from youtube.models import Search, Video
from youtube.schemas import (SearchOptionalParameters, SearchPart,
                             YouTubeListResponse, YouTubeRequest,
                             YouTubeResponse)

from ....extensions import youtube_client
from .schemas import CreateVideoSchema


def get_videos(query: str, max_results: int = 10) -> list[CreateVideoSchema]:
    part: SearchPart = SearchPart()
    optional: SearchOptionalParameters = SearchOptionalParameters(
        q=query, type=["videos"], maxResults=max_results
    )
    search_schema: YouTubeRequest = YouTubeRequest(
        part=part, optional_parameters=optional
    )
    response: YouTubeResponse = youtube_client.search(search_schema=search_schema)
    items: list[Search] = response.items
    video_ids: list[str] = [item.resource_id for item in items]
    response: YouTubeListResponse = youtube_client.find_videos_by_ids(
        video_ids=video_ids
    )
    videos: list[Video] = response.items
    res: list[CreateVideoSchema] = [
        CreateVideoSchema(
            id=video.id,
            title=video.snippet.title,
            channel_title=video.snippet.channel_title,
            description=video.snippet.description,
            comments_count=video.statistics.comments_count,
            likes_count=video.statistics.likes_count,
            views_count=video.statistics.views_count,
        )
        for video in videos
    ]
    return res
