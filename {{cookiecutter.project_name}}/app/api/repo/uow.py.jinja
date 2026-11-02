from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

TRepo = TypeVar("TRepo")

"""
Share a single session across repositories to ensure atomic transactions.
This keeps repositories reusable and prevents services from manually
rebinding each repo to the same session.
"""


class UnitOfWorkRepository:
    def __init__(
        self,
        sync_session: Session | None = None,
        async_session: AsyncSession | None = None,
    ):
        self._sync_session = sync_session
        self._async_session = async_session

        self._repositories: dict[type, object] = {}

    @property
    def async_session(self) -> AsyncSession:
        if self._async_session is None:
            raise RuntimeError(
                f"{type(self).__name__} has no async session; "
                "construct it with async_session= or assign one before use"
            )
        return self._async_session

    @async_session.setter
    def async_session(self, session: AsyncSession | None):
        self._async_session = session

    @property
    def sync_session(self) -> Session:
        if self._sync_session is None:
            raise RuntimeError(
                f"{type(self).__name__} has no sync session; "
                "construct it with sync_session= or assign one before use"
            )
        return self._sync_session

    @sync_session.setter
    def sync_session(self, session: Session | None):
        self._sync_session = session

    def repo(self, repository_cls: type[TRepo], **kwargs) -> TRepo:
        repo = self._repositories.get(repository_cls)

        if repo is None:
            repo = repository_cls(async_session=self._async_session, **kwargs)
            self._repositories[repository_cls] = repo

        return repo

    async def flush(self):
        await self._async_session.flush()

    async def refresh(self, model):
        await self._async_session.refresh(model)

    async def commit(self):
        await self._async_session.commit()

    async def rollback(self):
        await self._async_session.rollback()
