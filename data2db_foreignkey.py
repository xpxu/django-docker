'''
带foreignkey的批量导入
'''

import os,sys
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_models.settings")

import django
if django.VERSION >= (1, 7):#check django version
    django.setup()

def main():
    from essayApp.models import Essay
    from userApp.models import User
    from publicationApp.models import Publication
    with open('essaylist.txt') as f:
        # User 是 foreignkey. 与Essay的关系是一对多. 
        EssayList = [Essay(owner=User.objects.get(name=line.split(' ')[0]),
                           content=line.split(' ')[1],
                           ) for line in f]
        Essay.objects.bulk_create(EssayList)

if __name__ == "__main__":
    main()
    print('Done!')
