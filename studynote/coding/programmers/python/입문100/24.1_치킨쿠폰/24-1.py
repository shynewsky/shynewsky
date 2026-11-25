# 하나 먹으면, 쿠폰 하나
# 쿠폰 10개에 서비스치킨 하나
# 즉, 쿠폰 10개에 쿠폰1개 추가

def solution(coupon):
    service = 0
    while coupon // 10 > 0:  #
        service += coupon // 10
        coupon = coupon // 10 + coupon % 10

    return service
