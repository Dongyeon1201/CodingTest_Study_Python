def is_correct_skill_tree(skill, skill_tree):
    idx = 0
    skill_num = 0

    while skill_num < len(skill) and idx < len(skill_tree):

        if skill_tree[idx] == skill[skill_num]:
            skill_num += 1

        else:
            if skill_tree[idx] in skill[skill_num + 1 :]:
                return False

        idx += 1

    return True


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        if is_correct_skill_tree(skill, skill_tree):
            answer += 1

    return answer


skill = "CBD"
# skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "BACBDE"]
skill_trees = ["CAERTYUIOD"]
print(solution(skill, skill_trees))
