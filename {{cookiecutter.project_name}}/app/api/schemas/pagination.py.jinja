from pydantic import BaseModel, ConfigDict, Field

MAX_PAGE_LIMIT: int = 100


class CursorParams(BaseModel):
    # unknown query params (e.g. cache busters added by proxies) are ignored, not rejected
    model_config = ConfigDict(str_strip_whitespace=True, extra="ignore")

    limit: int = Field(20, ge=1, le=MAX_PAGE_LIMIT)
    # opaque token from the previous page's response; omit for the first page
    cursor: str | None = None


class ListQuery(CursorParams):
    """Base for list endpoint query params.

    Subclass per resource: add the filter fields and narrow `sort` to a
    Literal of the allowed fields, "-" prefix for descending, e.g.

        UserSort = Literal["created_at", "-created_at"]

        class UserListQuery(ListQuery):
            is_active: bool | None = None
            sort: UserSort = "-created_at"

    Use it in the router as `query: Annotated[UserListQuery, Query()]` and pass
    `**query.model_dump(exclude_none=True)` to `get_records`, so unset filters
    are not applied.
    """

    sort: str = "-created_at"
