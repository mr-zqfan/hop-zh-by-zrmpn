import os

lines: list[tuple[str, str]] = []
with open('moran_fixed_simp.dict.yaml', 'r', encoding='utf-8') as fp:
    start_ = False
    for line in fp.readlines():
        if line[0] == '啊':
            start_ = True
        if not start_:
            continue
        word, py = line.strip().split()
        lines.append((word, py))


# 处理单字的情况
# ['a'] = [[\%([a哀矮癌澳瑷案岸廒暧氨遨嗳璈鏖啊碍骜盦毐皑翱嗄爱鳌蔼𩽾媪暗嗌盎岙按谙桉犴卬螯凹埯铵砹腌隘唉鹌傲鏊聱阿埃锿昂熬黯安胺袄吖叆隩嗷嫒庵垵拗锕敖挨獒哎唵奡奥懊坳鞍欸肮艾霭俺]\)]],
single_dict: dict[str, list[str]] = {}
for word, py in lines:
    if py[0] not in single_dict:
        single_dict[py[0]] = []
    single_dict[py[0]].append(word)

out_lines: list[str] = []
for py, words in single_dict.items():
    out_lines.append(f"['{py}'] = [[\\%([{py}{''.join(words)}]\\)]],")

with open('conv-one.txt', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(out_lines))

# 处理多字的情况
# ['aa'] = [[\%(aa\|[阿腌锕啊嗄吖]\)]],
multi_dict: dict[str, list[str]] = {}
for word, py in lines:
    if len(py) < 2:
        continue
    if py[:2] not in multi_dict:
        multi_dict[py[:2]] = []
    multi_dict[py[:2]].append(word)

out_lines = []
for py, words in multi_dict.items():
    out_lines.append(f"['{py}'] = [[\\%({py}\\|[{''.join(words)}]\\)]],")

with open('conv-multi.txt', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(out_lines))
