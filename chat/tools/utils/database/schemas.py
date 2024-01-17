from pydantic import BaseModel, Field


class CreateVideoSchema(BaseModel):
    id: str = Field(description="A unique id for this video")
    title: str = Field(description="A unique title for this video")
    description: str = Field(description="A unique description for this video")
    channel_title: str = Field(
        description="The channel title to which this video belongs"
    )
    views_count: int = Field(
        description="The number of times this video has been viewed"
    )
    likes_count: int = Field(description="The number of likes for this video")
    comments_count: int = Field(description="The number of comments for this video")
