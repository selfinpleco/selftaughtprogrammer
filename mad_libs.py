import re

text = """キリンは大昔から _複数名詞_ の興味の対象でした。
キリンは _複数名詞_ の中で一番背が高いですが、科学者たちは
そのような長い _体の一部_ をどうやって獲得したのか説明できません。
キリンの身長は _数値_ _単位_ 近くあり、その高さのほとんどは脚と
_体の一部_ によるものです。
"""

def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語（=ヒント）
    の部分は後を２つのアンダースコアではさんでください。ヒントの単語
    にはアンダースコアを含めないでください。 _hint_hint_はだめです。
    _hint_ はOKです。
    """

    hints = re.findall("_.*?_", mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力：".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")


mad_libs(text)
