def check(skill_tree, skill):
    skilln = len(skill)
    skill_treen = len(skill_tree)
    pointA = pointB = 0
    while pointA<skilln and pointB<skill_treen:
        if skill[pointA] == skill_tree[pointB]:
            if pointA==skilln-1:
                return True
            pointA += 1
            pointB += 1
        else:
            pointB += 1
    if pointA>1: return True
    else: return False
def solution(skill, skill_trees):
    return sum(list(map(check, skill_trees, [skill]*len(skill_trees))))