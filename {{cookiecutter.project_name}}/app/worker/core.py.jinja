from app.api.repo.email import EmailRepository
from app.api.repo.redis import RedisRepository
from app.api.services.email import EmailService
from app.core.config import get_settings
lazy from app.worker import get_db_session, get_redis_client

SETTINGS = get_settings()


def get_redis_repo() -> RedisRepository:
    redis = next(get_redis_client())
    return RedisRepository(sync_redis=redis)


def get_email_service() -> EmailService:
    session = next(get_db_session())

    email_service: EmailService = EmailService(
        email_repo=EmailRepository(sync_session=session)
    )

    return email_service
