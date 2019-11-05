import os
import requests
import datetime


def get_users():#Получаем файл с информацией о пользователях
    url_u='https://jsonplaceholder.typicode.com/users'
    r_u=requests.get(url_u)
    respons_arr_u=r_u.json()
    return respons_arr_u

def get_tasks(user_id):#Получаем массивы выполненных и невыполненных задач
    url_t='https://jsonplaceholder.typicode.com/todos'
    r_t=requests.get(url_t)
    respons_arr_t=r_t.json()
    c_tasks=[]
    unc_tasks=[]
    for i in respons_arr_t:
        if i['userId']==user_id:
            if i['completed']:
                c_tasks.append(i['title'])
            else:
                unc_tasks.append(i['title'])
    return c_tasks,unc_tasks
    
def check_file(name):#Проверим, существует ли уже отчет по юзеру, если существует -- переименуем
    directory_file=os.path.abspath(os.curdir)+'/tasks/'
    file_name=directory_file+name+'.txt'#ссылка на файл
    if os.path.exists(file_name):
        time_file_mark=os.path.getmtime(directory_file)
        time_file=datetime.datetime.fromtimestamp(time_file_mark).strftime("%Y-%m-%dT%H-%M-%S")
        os.rename(file_name,directory_file+name+'_'+time_file+'.txt')
    return file_name
        
def create_file(name,email,company):#Создаем отчет по пользователю
    #Получаем дату
    now=datetime.datetime.now()
    date=now.strftime("%d.%m.%Y %H:%M:%S")
    #Создаем документ и заполняем его
    with open(file_name,'w')as file:
        str_one=name+' '+email+' '+date+'\n'
        str_two=company+'\n'
        str_three=''+'\n'
        strs_c='Завершенные задачи:'+'\n'
        strs_unc='Оставшиеся задачи:'+'\n'
        for j in c_tasks:
            if len(j)>50:
                j=j[:50]+'...'
                strs_c+=j+'\n'
            else:
                strs_c+=j+'\n'
        strs_c+='\n'
        for i in unc_tasks:
            if len(i)>50:
                i=i[:50]+'...'
                strs_unc+=i+'\n'
            else:
                strs_unc+=i+'\n'
        strs_unc+='\n'
        record=str_one+str_two+str_three+strs_c+strs_unc
        file.write(record)



try:
    os.mkdir('tasks')
except FileExistsError:
    print('Папка tasks уже существует')

users=get_users()
for user in range(len(users)):
    name=users[user]['name']
    email='<'+str(users[user]['email'])+'>'
    company=users[user]['company']['name']
    user_id=users[user]['id']
    c_tasks,unc_tasks=get_tasks(user_id)
    file_name=check_file(name)
    create_file(name,email,company)
