import re

def solution(new_id):
  new_id = new_id.lower()
  new_id = ''.join(re.findall('[a-z0-9\_\-\.]', new_id))
  new_id = re.sub('\.+', '.', new_id)
  new_id = re.sub('^\.', '', new_id)
  new_id = re.sub('\.$', '', new_id)
  if (len(new_id) == 0):
    new_id = 'a'
  if (len(new_id) > 15):
    new_id = new_id[:15]
  new_id = re.sub('\.$', '', new_id)
  if (len(new_id) < 3):
    while (len(new_id) != 3):
      new_id += new_id[-1]
  return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution('.abc123-_..............ㅋㅋㅋㅋㅋㅋ.'))

# print(solution("z-+.^."))
# print(solution(	"=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
