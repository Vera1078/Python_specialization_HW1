# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter


text = 'Жил себе дед да баба, у них была курочка Ряба; снесла под полом яичко - пестро, востро, костяно, мудрено!' \
    'Дед бил - не разбил, баба била - не разбила, а мышка прибежала да хвостиком раздавила.' \
    'Дед плачет, баба плачет, курочка кудкудачет, ворота скрипят, со двора щепки летят, на избе верх шатается!' \
    'Шли за водою поповы дочери, спрашивают деда, спрашивают бабу:' \
    '- О чем вы плачете?' \
    ' Как нам не плакать! - отвечают дед да баба. - Есть у нас курочка Ряба; снесла под полом яичко - пестро, востро,' \
    'костяно, мудрено!' \
    'Дед бил - не разбил, баба била - не разбила, а мышка прибежала да хвостиком раздавила.' \
    'Как услышали это поповы дочери, со великого горя бросили ведра наземь, поломали коромысла и воротились домой' \
    'с пустыми руками.' \
    '- Ах, матушка! - говорят они попадье. - Ничего ты не знаешь, ничего не ведаешь, а на свете много деется:' \
    'живут себе дед да баба, у них курочка Ряба; снесла под полом яичко - пестро, востро, костяно, мудрено!' \
    'Дед бил - не разбил, баба била - не разбила, а мышка прибежала да хвостиком раздавила.' \

res = re.findall(r'\w+', text.lower())
limit = 10

print(';\n'.join(f"'{k}': {v} раз(а)" for k, v in Counter(res).most_common(limit)))