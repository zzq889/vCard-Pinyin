#!/usr/bin/python
# -*- coding: utf-8 -*-
import vobject, StringIO
from pinyin import Pinyin

def first_upper(s):
    return s[0].upper() + s[1:]

p = Pinyin()
s = StringIO.StringIO(open('st.vcf', 'r').read())
f = open('st2.vcf', 'w')
for card in vobject.readComponents(s):
    if len(card.contents['n']) != 1:
	print 'len != 1, exit'
        break
    parts = card.contents['n'][0].value
    if 'x-phonetic-first-name' not in card.contents and len(parts.given) > 0:
        card.add('x-phonetic-first-name')
        card.x_phonetic_first_name.value = first_upper(p.get_pinyin(parts.given))
    if 'x-phonetic-last-name' not in card.contents and len(parts.family) > 0:
        card.add('x-phonetic-last-name')
        card.x_phonetic_last_name.value = first_upper(p.get_pinyin(parts.family))
    f.write(card.serialize())
f.close()
