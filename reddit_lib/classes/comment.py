from typing import TypedDict

from .base import Thing, ThingData


class Comment(TypedDict):
    all_awardings: list
    approved_at_utc: None
    approved_by: None
    archived: bool
    associated_award: None
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
    body: str
    body_html: str
    can_gild: bool
    can_mod_post: bool
    collapsed: bool
    collapsed_because_crowd_control: None
    collapsed_reason: str | None
    collapsed_reason_code: str | None
    comment_type: None
    controversiality: int
    created: float
    created_utc: float
    depth: int
    distinguished: None
    downs: int
    edited: bool
    gilded: int
    gildings: dict
    id: str
    is_submitter: bool
    likes: None
    link_id: str
    locked: bool
    mod_note: None
    mod_reason_by: None
    mod_reason_title: None
    mod_reports: list
    name: str
    no_follow: bool
    num_reports: None
    parent_id: str
    permalink: str
    removal_reason: None
    replies: str | dict
    report_reasons: None
    saved: bool
    score: int
    score_hidden: bool
    send_replies: bool
    stickied: bool
    subreddit: str
    subreddit_id: str
    subreddit_name_prefixed: str
    subreddit_type: str
    top_awarded_type: None
    total_awards_received: int
    treatment_tags: list
    unrepliable_reason: None
    ups: int
    user_reports: list


class ChildrenListing(Thing):
    data: Comment


class CommentListingData(ThingData):
    children: list[ChildrenListing]


class CommentListing(Thing):
    data: CommentListingData
