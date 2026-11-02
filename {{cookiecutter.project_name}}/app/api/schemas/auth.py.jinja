from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class AuthBase(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")


class TokenData(AuthBase):
    user_id: UUID
    session_id: UUID


class Token(AuthBase):
    access_token: str
    token_type: str = "bearer"


class EmailVerify(AuthBase):
    email: EmailStr
    otp_code: str


class ResendOtp(AuthBase):
    email: EmailStr


class EmailLogin(AuthBase):
    email: EmailStr
    password: str = Field(..., min_length=8)


class SignUpResponse(BaseModel):
    pass


class OtpResendResponse(BaseModel):
    pass


class LogoutResponse(BaseModel):
    pass
