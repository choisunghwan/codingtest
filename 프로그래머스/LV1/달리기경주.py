def solution(players, callings):
    rankinfo = {} # rankinfo딕셔너리 선언  -- 등수 : 선수이름 
    playerinfo ={}  # playerinfo딕셔너리 선언 -- 선수이름: 등수 

    #변수설명 >> i : 번호(등수) player: 선수 이름
    for i, player in enumerate(players): 
        rankinfo[i] = player
        #print(idx)
    #print (rankinfo)

    for i, player in enumerate(players):
        playerinfo[player] = i
    #print(playerinfo)






    for callname in callings:
        rank = playerinfo[callname]      # 현재 등수
        f_rank = rank - 1 # 앞 등수 
        f_name = rankinfo[f_rank] # 앞 선수이름

        rankinfo[f_rank] = callname 
        rankinfo[rank] = f_name

        playerinfo[f_name] = rank
        playerinfo[callname] = f_rank

    #print(list(rankinfo.values()))
    # answer = (list(rankinfo.values()))
    answer = list(rankinfo.values())
    return answer


print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))