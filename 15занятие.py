# #номера телефонов.убрать некорректные.исправить 8029
with open('input.txt','r',encoding='utf-8') as file:
    for s,j in enumerate(file):
        if j[:6]=='+37529' or j[:6]=='+37533'or j[:6]=='+37525'or j[:6]=='+37544' and len(j)==13 and j[1:].isdigit():
            with open('output.txt','a',encoding='utf-8') as file:
                file.write(''.join(j))
        elif j[:4]=='8029' or j[:4]=='8033' or j[:4]=='8025' or j[:4]=='8044' and len(j)==11 and j.isdigit():
            lst=['+375'+j[2:]]
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(''.join(lst))
phones=[]
codes=['33','44','25']
valid_phones=[]
for phone in phones:
    if phone.startswith('+375'):
        pass
    if len(phone)==13 and phone[4:].isdigit() and phone[4:6] in codes:
        valid_phones.append(phone)
    elif phone.startswith('80'):
        phone=phone.replace('80','+375')
    else:
        continue
#дан файл с почтами. убрать не корректные
with open('email.txt','r',encoding='utf-8') as file:
    for s,j in enumerate(file):
        dog = j.find('@')
        point=j.rfind('.')
        if j.count('@')==1 and j[dog:].count('.')==1 and j[dog+1:point].isalpha() and j[dog+1:point].isalpha() and len(j[:dog])>=1 and j[:dog].isalnum()==True:
            with open('output.txt', 'a', encoding='utf-8') as file:
                file.write(''.join(j))
        elif j.count('@')==1 and j[dog:].count('.')==1 and j[dog+1:point].isalpha() and j[dog+1:point].isalpha() and len(j[:dog])>=1 and j[:dog].isalnum()==False:
            for k in (j[:dog]):
                if k.isalnum()==False and k!='.' or k!='_' or k!='-':
                        break
                else:
                    with open('output.txt', 'a', encoding='utf-8') as file:
                        file.write(''.join(j))





