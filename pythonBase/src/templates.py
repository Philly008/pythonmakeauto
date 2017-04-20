'''
Created on 2016年12月29日

@author: admin
'''
import fileinput, re 
# 匹配中括号里的字段
field_pat = re.compile(r'\[(.+?)\]')
# 我们将变量收集到这里：
scope = {}
# 用于 re.sub 中：
def replacement(match):
    code = match.group(1)
    try:
        # 如果字段可以求值，返回它：
        return str(eval(code, scope))
    except SyntaxError:
        # 否则执行相同作用域内的赋值语句......
        exec(code in scope)
        # ......返回空字符串：
        return ''

# 将所有文本以一个字符串的形式获取：
lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)
# 将 field 模式的所有匹配项都替换掉：
print(field_pat.sub(replacement, text))

        
        
        
        
        
        