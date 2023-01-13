# def reverseFile():
#     # with open("text1.txt") as f:
#     #     text = f.read()
#     #     text = text[::-1]
#     #
#     # f = open("text2.txt", "w")
#     # f.write(text)
#     for text in reversed(f.open("text1.txt").readlines()):
#         g.open("text2.txt", "w").write(text)
# reverseFile()
#
#
# x = [line.strip() for line in open("text1.txt")]
# f = open("text2.txt", "w")
# f.write(x[0][::-1])

open('text2.txt', 'w').write(open("text1.txt", 'r').read()[::-1])
