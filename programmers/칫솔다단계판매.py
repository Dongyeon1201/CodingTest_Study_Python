def solution(enroll, referral, seller, amount):

    # 초대한 사람과 얻은 이익금 누적 액수를 저장
    # {판매자 : [초대한 판매자, 누적 이익금], ... } 형태
    info = {name: [invite, 0] for name, invite in zip(enroll, referral)}

    # 판매자, 판매 액수를 얻어온다.
    for sell_name, sell_amount in zip(seller, amount):

        # 현재 판매자의 정보
        # 이익을 나누며, 상위 판매자로 갱신된다.
        seller_state = sell_name

        # 초기 이익을 판매자에게 우선 할당
        next_sell_amount = sell_amount * 100
        info[sell_name][1] += next_sell_amount

        # 상위 판매자가 존재하지 않거나, 판매 이익이 1원을 넘지 않을 때까지 반복
        while info[seller_state][0] != "-" and next_sell_amount > 1:

            # 상위 판매자에게 떼어줄 이익을 현재 판매자이 얻은 이익에서 뺀다.
            info[seller_state][1] -= next_sell_amount // 10

            # 떼어준 만큼 상위 판매자의 이익에 누적해준다.
            info[info[seller_state][0]][1] += next_sell_amount // 10

            # 상위 판매자로 넘어간 이익을 저장한다.
            # 해당 이익을 다음 상위 판매자에게 다시 나눠줘야하기 때문이다.
            next_sell_amount //= 10

            # 상위 판매자로 변경한다.
            seller_state = info[seller_state][0]

        # 가장 마지막 상위 판매자의 이익을 제외한다.
        info[seller_state][1] -= next_sell_amount // 10

    # 각 판매자의 누적된 이익을 반환한다.
    return [info[sell_name][1] for sell_name in enroll]


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))
