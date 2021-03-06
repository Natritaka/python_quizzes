
#######################################
# 条件文、繰り返し文
#######################################


def f1(a):
    # もしaが100以上ならxに2を、100より小さければ1を代入せよ

    # 以下を書きかえる
    if True:
        x = 0
    else:
        x = 0
    # ここまでを書き換える
    return x


def f2():
    # 1から10までの積を計算してxに代入せよ

    # 以下を書き換える
    x = 0
    # ここまでを書き換える
    return x

#######################################
# リストの操作
#######################################


def f3(l):
    # 与えられたリストlの2番目の要素をxに代入せよ
    # 例：[1,2,3,4]　=> 2

    # 以下を書き換える
    x = 0
    # ここまでを書き換える
    return x


def f4(l):
    # 与えられたリストlの3番目から5番目の要素からなるリストをxに代入せよ
    # 例：[1,2,3,4,5,6] =. [3,4,5]

    # 以下を書き換える
    x = []
    # ここまでを書き換える
    return x


def f5(l):
    # 与えられたリストlの最後のⅠつの要素を取り除いたリストをxに代入せよ
    # 例：[1,2,3,4,5,6] =. [1,2,3,4,5]

    # 以下を書き換える
    x = []
    # ここまでを書き換える
    return x


def f6(l):
    # 与えられたリストlの要素が全て整数であると分かっているとき、
    # そのリストの中から奇数だけを取り出したものをリストとしてxに代入せよ
    # （ヒント：for文とappendを使う）
    # 例：[1,2,3,4,5] => [1,3,5]

    # 以下を書き換える
    x = []
    # ここまでを書き換える
    return x


assert f1(100) == 2
assert f1(50) == 1
assert f2() == 3628800
assert f3(["a", "b", "c", "d", "e", "f"]) == "b"
assert f4(["a", "b", "c", "d", "e", "f"]) == ["c", "d", "e"]
assert f5(["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c", "d", "e"]
assert f6([11, 12, 13, 14, 15, 16, 20]) == [11, 13, 15]
print("OK")
