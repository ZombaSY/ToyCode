import numpy as np

"""
문제 이해를 못해서 못풀겠다...
이진 트리에서 pre-post order 구하는건데, 
인풋이 좌표상으로 표시된 노드인데 어떻게 자동으로 연결하는지...
"""


# 노드를 사용하지 않은 버전
def solution(nodeinfo):
    answer = [[]]

    check_node = np.ones(len(nodeinfo), dtype=np.bool)
    np_node = np.array(nodeinfo)
    np_node = np_node.transpose()

    post_order = []
    pre_oder = []

    high_y = np_node[1].max()
    low_y = np_node[1].min()

    while len(pre_oder) < len(nodeinfo):
        print("high_y :", high_y)
        is_selected = False
        print(np_node)
        filtered_node = np.array(list(filter(lambda x: x[1] <= high_y, np_node.transpose()))).transpose()
        max_y = filtered_node[1].max(axis=0)
        max_y_index = np.where(np_node[1] == max_y)[0]
        final_index = 0

        candidate_node = []
        for i in max_y_index:
            candidate_node.append(np_node.transpose()[i])

        candidate_node = np.array(candidate_node).transpose()

        # print("max_y_index :", max_y_index)
        print("candidate_node : \n", candidate_node)

        for i in max_y_index:
            min_x = candidate_node[0].min(axis=0)
            min_x_index = np.where(np_node[0] == min_x)[0]
            if check_node[i]:
                if i == min_x_index:
                    final_index = i
                    pre_oder.append(final_index+1)
                    is_selected = True

        check_node[final_index] = False

        if high_y > low_y & is_selected:
            high_y = np.array(list(filter(lambda x: x[1] < high_y, np_node.transpose()))).transpose()[1].max()
        else:
            high_y = np.array(list(filter(lambda x: x[1] > high_y, np_node.transpose()))).transpose()[1].min()

        print("pre order :", pre_oder)

    return answer


"""
import numpy as np


# 노드 사용 버전
def solution(nodeinfo):
    answer = [[]]

    np_node = np.array(nodeinfo).transpose()
    print(np_node)

    high_y = np_node[1].max()
    low_y = np_node[1].min()
    high_y_indexes = np.where(np_node[1] == high_y)[0]

    all_nodes = []

    for i in range(len(nodeinfo)):
        all_nodes.append(Node(i+1))

    print(high_y)

    while high_y > low_y:
        high_y = np.array(list(filter(lambda x: x[1] < high_y, np_node.transpose()))).transpose()[1].max()

        print(high_y)

    return answer


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
"""


def main():

    input_node = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    answer = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
    solution(input_node)


if __name__ == "__main__":
    main()
