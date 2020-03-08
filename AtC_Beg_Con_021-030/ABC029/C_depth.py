from collections import deque
n = int(input())

alphali = ["c", "b", "a"]  # "c", "b", "a"の順に詰めていく
ans = ""
stack = deque()
for al in alphali:
    stack.append(al)  # stackの初期状態を設定

phase = 0  # 段階を考える（ansにくっついている文字数），どれだけ掘り下げたか

while stack != deque():  # stackが空になるまで回す
    ans += stack.pop()  # stackにおいて一番右の文字をansに加える
    phase += 1  # 段階を掘り下げ，ansに1つ付与されたので段階を1上げる
    if phase != n:  # 終点じゃなければ
        for al in alphali:  # stackに "c", "b", "a"を詰める
            stack.append(al)
    else:  # 終点ならば
        print(ans)  # できた文字列を出力
        phase -= 1  # 段階を1つ戻す
        if ans[-1] == "c":  # 最後の文字が"c"なら
            phase -= 1  # もう1つ戻らなければならない
            ans = ans[:-1]
            for x in ans[::-1]:  # 末尾が"c"である限りどんどん戻る
                if x == "c":
                    phase -= 1
                    ans = ans[:-1]
                else:  # そうでなければfor文を終了
                    break
        ans = ans[:-1]  # 最後の文字とはおさらば