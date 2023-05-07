from fastapi import APIRouter

from . import get_updates, send_message


router = APIRouter(prefix='/v1')


router.include_router(get_updates.router)
router.include_router(send_message.router)
