#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
这个脚本用于向数据库中批量插入数据。
Model.objects.bulk_create()是批量插入数据最快的方式
'''

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_models.settings")

import django
if django.VERSION >= (1, 7):#check django version
    django.setup()

 
def main():
    from people.models import Person
    with open('personlist.txt') as f:   

        # 以下四行,用列表解析代替,更快更方便
        # BlogList = []
        # for line in f:
        #     parts = line.split(' ')
        #     BlogList.append(Blog(title=parts[0], content=parts[1]))
         
        PersonList = [Person(name=line.split(' ')[0], age=line.split(' ')[1],
            income=line.split(' ')[2]) for line in f]
        
        # 执行一条SQL存入多条数据，会快很多
        Person.objects.bulk_create(PersonList)
 
if __name__ == "__main__":
    main()
    print('Done!')
