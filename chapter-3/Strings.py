let = (str(input())).lower()
let = let.replace("a", '', -1)
let = let.replace("i", '', -1)
let = let.replace("e", '', -1)
let = let.replace("o", '', -1)
let = let.replace("u", '', -1)
let = let.replace('', '.')
let=let[:-1]
print(let)
