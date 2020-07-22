# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

from . import lang_EU
from .utils import splitbyx, get_digits

ZERO = ('μηδέν',)

ONES_FEMININE = {
    1: ('μία',),
    2: ('δύο',),
    3: ('τρείς',),
    4: ('τέσσερις',),
    5: ('πέντε',),
    6: ('έξι',),
    7: ('εφτά',),
    8: ('οχτώ',),
    9: ('εννιά',),
}

ONES_NEUTRAL = {
    1: ('ένα',),
    2: ('δύο',),
    3: ('τρία',),
    4: ('τέσσερα',),
    5: ('πέντε',),
    6: ('έξι',),
    7: ('εφτά',),
    8: ('οχτώ',),
    9: ('εννιά',),
}

TENS = {
    0: ('δέκα',),
    1: ('έντεκα',),
    2: ('δώδεκα',),
    3: ('δεκατρία',),
    4: ('δεκατέσσερα',),
    5: ('δεκαπέντε',),
    6: ('δεκαέξι',),
    7: ('δεκαεφτά',),
    8: ('δεκαοχτώ',),
    9: ('δεκαεννιά',),
}

TWENTIES = {
    2: ('είκοσι',),
    3: ('τριάντα',),
    4: ('σαράντα',),
    5: ('πενήντα',),
    6: ('εξήντα',),
    7: ('εβδομήντα',),
    8: ('ογδόντα',),
    9: ('εννενήντα',),
}

HUNDREDS = {
    1: ('εκκατόν',),
    2: ('διακόσια',),
    3: ('τριακόσια',),
    4: ('τετρακόσια',),
    5: ('πεντακόσια',),
    6: ('εξακόσια',),
    7: ('εφτακόσια',),
    8: ('οχτακόσια',),
    9: ('εννιακόσια',),
}

THOUSANDS = {
    1: ('χίλια', 'χιλιάδες'),  # 10^3
    2: ('εκατομμύρια', ),  # 10^6
    3: ('δισεκατομμύρια', ),  # 10^9
    4: ('τρισεκατομμύρια', ),  # 10^12
}

# THOUSANDS = {
#     1: ('тысяча', 'тысячи', 'тысяч'),  # 10^3
#     2: ('миллион', 'миллиона', 'миллионов'),  # 10^6
#     3: ('миллиард', 'миллиарда', 'миллиардов'),  # 10^9
#     4: ('τρισεκκατομύρια', 'триллиона', 'триллионов'),  # 10^12
#     # 5: ('квадриллион', 'квадриллиона', 'квадриллионов'),  # 10^15
#     # 6: ('квинтиллион', 'квинтиллиона', 'квинтиллионов'),  # 10^18
#     # 7: ('секстиллион', 'секстиллиона', 'секстиллионов'),  # 10^21
#     # 8: ('септиллион', 'септиллиона', 'септиллионов'),  # 10^24
#     # 9: ('октиллион', 'октиллиона', 'октиллионов'),  # 10^27
#     # 10: ('нониллион', 'нониллиона', 'нониллионов'),  # 10^30
# }

GENERIC_DOLLARS = ('δολάριο', 'δολάρια')
GENERIC_CENTS = ('σέντ', 'σέντς')

class Num2Word_EL(lang_EU.Num2Word_EU):
    CURRENCY_FORMS = {
        'AUD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'CAD': (GENERIC_DOLLARS, GENERIC_CENTS),
        # repalced by EUR
        'EUR': (('ευρώ', 'ευρώ'), ('λεπτό', 'λεπτά')),
        'GBP': (('λίρα αγγλίας', 'λίρες αγγλίας'), ('λεπτό', 'λεπτά')),
        'USD': (GENERIC_DOLLARS, GENERIC_CENTS),
        'RUB': (('ρούβλι', 'ρούβλια'), ('καπίκι', 'καπίκια')),
        'SEK': (('κορώνα', 'κορώνες'), GENERIC_CENTS),
        'NOK': (('κορώνα', 'κορώνες'), GENERIC_CENTS),
        'PLN': (('ζλότι', 'ζλότι', 'ζλότι'), GENERIC_CENTS),
        'MXN': (('πέσο', 'πέσος'), GENERIC_CENTS),
        'RON': (('λέου', 'λέι', 'λέι'), (GENERIC_CENTS)),
    }

    def setup(self):
        self.negword = "μείον"
        self.pointword = "κόμμα"
        self.ords = {"μηδέν": "μηδενοστός",
                     "ένας": "πρώτος",
                     "δύο": "δεύτερος",
                     "τρείς": "τρίτος",
                     "τέσσερις": "τέταρτος",
                     "πέντε": "πέμπτος",
                     "έξι": "έκτος",
                     "εφτά": "έβδομος",
                     "οχτώ": "όγδοος",
                     "εννιά": "ένατος",
                     "εκκατόν": "εκκατοστός"}
        self.ords_feminine = {"μία": "πρώτη",
                              "δύο": "δεύτερη",
                              "τρείς": "τρίτη",
                              "τέσσερις": "τέταρτη",
                              "πέντε": "πέμπτη",
                              "έξι": "έκτη",
                              "εφτά": "έβδομη",
                              "οχτώ": "όγδοη",
                              "εννιά": "έννατη"}
        self.ords_neutral = {"ένα": "πρώτο",
                             "δύο": "δεύτερο",
                             "τρία": "τρίτο",
                             "τέσσερα": "τέταρτο",
                             "πέντε": "πέμπτο",
                             "έξι": "έκτο",
                             "εφτά": "έβδομο",
                             "οχτώ": "όγδοο",}
                    
    def to_cardinal(self, number):
        n = str(number).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
            return u'%s %s %s' % (
                self._int2word(int(left)),
                self.pointword,
                self._int2word(int(right))
            )
        else:
            return self._int2word(int(n))

    def pluralize(self, n, forms):
        if n % 100 < 10 or n % 100 > 20:
            if n % 10 == 1:
                form = 0
            elif 5 > n % 10 > 1:
                form = 1
            else:
                form = 2
        else:
            form = 2
        return forms[form]

    def to_ordinal(self, number):
        self.verify_ordinal(number)
        outwords = self.to_cardinal(number).split(" ")
        lastword = outwords[-1].lower()
        try:
            if len(outwords) > 1:
                if outwords[-2] in self.ords_feminine:
                    outwords[-2] = self.ords_feminine.get(
                        outwords[-2], outwords[-2])
                elif outwords[-2] == 'десять':
                    outwords[-2] = outwords[-2][:-1] + 'и'
            if len(outwords) == 3:
                if outwords[-3] in ['один', 'одна']:
                    outwords[-3] = ''
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[:-3] in self.ords_feminine:
                lastword = self.ords_feminine.get(
                    lastword[:-3], lastword) + "сотый"
            elif lastword[-1] == "ь" or lastword[-2] == "т":
                lastword = lastword[:-1] + "ый"
            elif lastword[-1] == "к":
                lastword = lastword + "овой"
            elif lastword[-5:] == "десят":
                lastword = lastword.replace('ь', 'и') + 'ый'
            elif lastword[-2] == "ч" or lastword[-1] == "ч":
                if lastword[-2] == "ч":
                    lastword = lastword[:-1] + "ный"
                if lastword[-1] == "ч":
                    lastword = lastword + "ный"
            elif lastword[-1] == "н" or lastword[-2] == "н":
                lastword = lastword[:lastword.rfind('н') + 1] + "ный"
            elif lastword[-1] == "д" or lastword[-2] == "д":
                lastword = lastword[:lastword.rfind('д') + 1] + "ный"
        outwords[-1] = self.title(lastword)
        return " ".join(outwords).strip()

    def _cents_verbose(self, number, currency):
        return self._int2word(number, currency == 'RUB')

    def _int2word(self, n, feminine=False):
        if n < 0:
            return ' '.join([self.negword, self._int2word(abs(n))])

        if n == 0:
            return ZERO[0]

        words = []
        chunks = list(splitbyx(str(n), 3))
        i = len(chunks)
        for x in chunks:
            i -= 1

            if x == 0:
                continue

            n1, n2, n3 = get_digits(x)

            if n3 > 0:
                words.append(HUNDREDS[n3][0])

            if n2 > 1:
                words.append(TWENTIES[n2][0])

            if n2 == 1:
                words.append(TENS[n1][0])
            elif n1 > 0:
                ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
                words.append(ones[n1][0])

            if i > 0:
                words.append(self.pluralize(x, THOUSANDS[i]))

        return ' '.join(words)
