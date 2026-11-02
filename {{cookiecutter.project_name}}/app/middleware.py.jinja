import uuid

from starlette.middleware.base import BaseHTTPMiddleware


class RequestIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = uuid.uuid4()
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-Id"] = str(request_id)
        return response
