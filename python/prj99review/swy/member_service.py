from swy.exception.member import IdException, NickException, PwException
from swy.memberVo import MemberVo
from swy.member_repository import join_r


def join_s(vo: MemberVo) -> int:
    if len(vo.id) < 4:
        raise IdException()
    if len(vo.pw) < 4:
        raise PwException()
    if len(vo.nick) < 4:
        raise NickException()

    result = join_r(vo)
    return result
