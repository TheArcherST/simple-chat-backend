from fastapi import APIRouter, Depends

from database import crud

from schemas import v1 as schemas

from ..common import authenticated_user, database_session, SessionType

router = APIRouter()


@router.get(
    '/sendMessage',
    response_model=schemas.extra.msg_responses.Ok,
    responses={
        404: {"model": schemas.extra.err_responses.Schemas.ChatNotFound}
    }
)
async def send_message(
        session: SessionType = Depends(database_session),
        user: schemas.user.User = Depends(authenticated_user),
        chat: str = ...,
        text: str = ...,
):

    chat_user = await crud.user.get_user_by_username_or_create(
        session=session,
        username=chat,
    )

    if chat_user is None:
        raise schemas.extra.err_responses.Exceptions.UserNotFound()

    await crud.messages.send_message(
        session=session,
        from_user_id=user.id,
        chat_id=chat_user.id,
        text=text,
    )

    return schemas.extra.msg_responses.Ok()
