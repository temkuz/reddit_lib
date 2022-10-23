from typing import TypedDict

from .base import Thing, ThingData


class Post(TypedDict):
    all_awardings: list
    allow_live_comments: bool
    approved_at_utc: str
    approved_by: None
    archived: bool
    author: str
    author_flair_background_color: str | None
    author_flair_css_class: str | None
    author_flair_richtext: list
    author_flair_template_id: str | None
    author_flair_text: str | None
    author_flair_text_color: str | None
    author_flair_type: str
    author_fullname: str
    author_is_blocked: bool
    author_patreon_flair: bool
    author_premium: bool
    awarders: list
    banned_at_utc: None
    banned_by: None
    call_to_action: bool
    can_gild: bool
    can_mod_post: bool
    category: str | None
    clicked: bool
    content_categories: None
    contest_mode: bool
    created: float
    created_utc: float
    crosspost_parent: str
    crosspost_parent_list: list
    discussion_type: None
    distinguished: str | None
    domain: str
    downs: int
    edited: float | bool
    gallery_data: dict
    gilded: int
    gildings: dict
    hidden: bool
    hide_score: bool
    id: str
    is_created_from_ads_ui: bool
    is_crosspostable: bool
    is_gallery: bool
    is_meta: bool
    is_original_content: bool
    is_reddit_media_domain: bool
    is_robot_indexable: bool
    is_self: bool
    is_video: bool
    likes: None
    link_flair_background_color: str
    link_flair_css_class: str
    link_flair_richtext: list
    link_flair_template_id: str
    link_flair_text: str | None
    link_flair_text_color: str
    link_flair_type: str
    locked: bool
    media: dict | None
    media_embed: dict
    media_metadata: dict
    media_only: bool
    mod_note: None
    mod_reason_by: None
    mod_reason_title: None
    mod_reports: list
    name: str
    no_follow: bool
    num_comments: int
    num_crossposts: int
    num_reports: None
    over_18: bool
    parent_whitelist_status: str
    permalink: str
    pinned: bool
    post_hint: str
    preview: dict
    pwls: int
    quarantine: bool
    removal_reason: str | None
    removed_by: None
    removed_by_category: str | None
    report_reasons: None
    saved: bool
    score: int
    secure_media: dict | None
    secure_media_embed: dict | None
    selftext: str
    selftext_html: str | None
    send_replies: bool
    spoiler: bool
    stickied: bool
    subreddit: str
    subreddit_id: str
    subreddit_name_prefixed: str
    subreddit_subscribers: int
    subreddit_type: str
    suggested_sort: str | None
    thumbnail: str
    thumbnail_height: int | None
    thumbnail_width: str | None
    title: str
    top_awarded_type: None
    total_awards_received: int
    treatment_tags: list
    ups: str
    upvote_ratio: str
    url: str
    url_overridden_by_dest: str
    user_reports: list
    view_count: None
    visited: bool
    whitelist_status: str
    wls: int


class ChildrenListing(Thing):
    data: Post


class PostListingData(ThingData):
    children: list[ChildrenListing]


class PostListing(Thing):
    data: PostListingData
