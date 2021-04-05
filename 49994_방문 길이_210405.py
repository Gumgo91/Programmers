def solution(dirs):
    hash = set()
    answer = x = y = 0
    for dir in dirs:
        if dir=='U' and y!=5:
            h = '{}_{}_{}_{}'.format(x,y,x,y+1)
            hr = '{}_{}_{}_{}'.format(x,y+1,x,y)
            y += 1
        elif dir=='D' and y!=-5:
            h = '{}_{}_{}_{}'.format(x,y,x,y-1)
            hr = '{}_{}_{}_{}'.format(x,y-1,x,y)
            y -= 1
        elif dir=='R' and x!=5:
            h = '{}_{}_{}_{}'.format(x,y,x+1,y)
            hr = '{}_{}_{}_{}'.format(x+1,y,x,y)
            x += 1
        elif dir=='L' and x!=-5:
            h = '{}_{}_{}_{}'.format(x,y,x-1,y)
            hr = '{}_{}_{}_{}'.format(x-1,y,x,y)
            x -= 1
        else: continue
        if h not in hash:
            hash.add(h)
            hash.add(hr)
            answer += 1
    return answer