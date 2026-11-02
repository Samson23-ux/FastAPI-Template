import hashlib
import hmac
import secrets
from uuid import UUID

import sentry_sdk
import sentry_sdk.logger as sentry_logger

from app.api.repo.redis import RedisRepository
from app.core.config import get_settings
from app.core.exceptions import InvalidOtpError, OtpAttemptsExceededError, ServerError

SETTINGS = get_settings()


class OtpService:
    def __init__(self, redis_repo: RedisRepository):
        self._redis_repo = redis_repo

    @staticmethod
    def _otp_key(user_id: UUID) -> str:
        return f"otp:{user_id!s}"

    def _hash_otp(self, otp: str) -> str:
        return hmac.new(
            SETTINGS.OTP_SECRET_KEY.encode(), otp.encode(), hashlib.sha256
        ).hexdigest()

    @staticmethod
    def _otp_expire() -> int:
        return SETTINGS.OTP_EXPIRE_TIME * 60

    async def create_otp(self, user_id: UUID) -> str:
        otp: str = str(secrets.randbelow(900000) + 100000)

        try:
            await self._redis_repo.create_hset(
                self._otp_key(user_id),
                {"code": self._hash_otp(otp), "attempts": 0},
                self._otp_expire(),
            )
        except Exception as exc:
            sentry_sdk.capture_exception(exc)
            sentry_logger.error(
                "Error occurred while creating otp for user {user_id}",
                user_id=str(user_id),
            )

            raise ServerError() from exc

        return otp

    async def verify_otp(self, user_id: UUID, otp: str):
        try:
            otp_state = await self._redis_repo.consume_otp_code(
                self._otp_key(user_id), self._hash_otp(otp), SETTINGS.OTP_MAX_ATTEMPTS
            )
        except Exception as exc:
            sentry_sdk.capture_exception(exc)
            sentry_logger.error(
                "Error occurred while verifying otp for user {user_id}",
                user_id=str(user_id),
            )
            raise ServerError() from exc

        if otp_state == 1:
            return

        sentry_logger.warning(
            "Invalid otp received for user {user_id}",
            user_id=str(user_id),
        )

        if otp_state == -1:
            raise OtpAttemptsExceededError()
        raise InvalidOtpError()
