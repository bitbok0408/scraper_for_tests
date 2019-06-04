import re

a = {"text": "<li class=\"list-group-item\" style=\"border:0px none;\">\n                <span class=\"label label-info\">0%</span>\n                Укр asdsad            </li>"}


# m = re.match(r"(</span>\\n)?( )+(?P<first_name>[А-Яа-яЁёЇiїІіЄєҐґ' ]+)+( )+(</li>)?", a['text'])
# m = re.match(r"(?P<first_name>[A-Za-z ]) (?P<last_name>\w+)", "Malcolm Reynolds")

m = re.search(r"(?P<first_name>\w+)+( )+(</li>)+", a['text'])

print(m.group("first_name"))
print(m.groups())



#(\<\/span\>\\n)?( )+[?P=<test> А-Яа-яЁёЇiїІіЄєҐґ']*( )+(\<\/li\>)?