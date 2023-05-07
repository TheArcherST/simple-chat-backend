from fastapi import APIRouter, Depends

from database import crud

from schemas import v1 as schemas
from data_intermediary.message import MessageDataIntermediary

from ..common import authenticated_user, database_session, SessionType


router = APIRouter()


@router.get(
    '/getUpdates',
    response_model=schemas.message.MessageList
)
async def get_updates(
        session: SessionType = Depends(database_session),
        user: schemas.user.User = Depends(authenticated_user),
):

    results = await crud.messages.get_unreceived_messages(
        session=session,
        for_user_id=user.id,
    )
    results = list(results)

    message_ids = [i.id for i in results]
    await crud.messages.mark_messages_as_received(
        session=session,
        message_ids=message_ids,
    )

    results = await MessageDataIntermediary.models_to_schemas(session, results)

    return results
