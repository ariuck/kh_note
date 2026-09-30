from swy.exception.member import IdException, PwException, NickException
from swy.memberVo import MemberVo
from swy.member_service import join_s


def join_c():
    id = input("id : ")
    pw = input("pw : ")
    nick = input("nick : ")

    vo = MemberVo(id, pw, nick)
    try:
        result = join_s(vo)
    except IdException as e:
        print("[Member-Join-001] ID 너무 짧아서 에러남" , e)
        result = -1
    except PwException as e:
        print("[Member-Join-002] PW 너무 짧아서 에러남", e)
        result = -1
    except NickException as e:
        print("[Member-Join-003] NICK 너무 짧아서 에러남", e)
        result = -1
    print("join result : ", result)

    '''
    {
        head : {
            status_code : 200
            status_msg : OK
        } ,
        body : {
            "result" , 1
        }
    }
    '''


# map 사용 , class 실습 , 쓰레드 , 스코프