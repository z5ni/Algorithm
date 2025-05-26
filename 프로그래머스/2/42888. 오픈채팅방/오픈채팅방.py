def solution(record):
    result = []
    name = dict()
    for r in record:
        r = list(r.split())
        if r[0] == "Enter":
            name[r[1]] = r[2]
        if r[0] == "Change":
            name[r[1]] = r[2]
        
    for r in record:
        r = list(r.split())
        if r[0] == "Enter":
            result.append(f"{name[r[1]]}님이 들어왔습니다.")
        if r[0] == "Leave":
            result.append(f"{name[r[1]]}님이 나갔습니다.")
    
    return result