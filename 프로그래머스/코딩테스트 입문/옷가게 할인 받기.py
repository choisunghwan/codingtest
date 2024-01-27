def solution(price):
    if 500000 <= price <= 1000000:
        sale1 = price * 0.2
        return int(price - sale1)
    elif 300000 <= price <= 500000:
        sale2 = price * 0.1
        return int(price - sale2)
    elif 10 <= price <= 300000:
        sale3 = price * 0.05
        return int(price - sale3)
    