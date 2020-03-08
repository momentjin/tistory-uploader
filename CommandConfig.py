import Tistory
import click
import os
import UserInfo
from pathlib import Path
import json

@click.group()
def cli():
    pass

@click.command()
def init():
    os.popen('code user.json')

@click.command()
def token():
    Tistory.getAccessToken()
    return

@click.command()
def category():
    response = Tistory.getCategories()
    data = json.loads(response.text)
    categories = data['tistory']['item']['categories']
    my_categories = []
    for c in categories:
        a = {}
        for key in c.keys():
            if key == 'id' or key == 'name':
                a[key] = c[key] 
            
        my_categories.append(a) 

    UserInfo.write_categories(my_categories)
    return

@click.command()
@click.argument('file')
@click.option('-cg', '--category', help="카테고리 이름 입력")
def write(category, file):
    f = open(file, "r")

    req = {
        'title': os.path.basename(f.name).split('.')[0], 
        'content':f.read(),
    }

    if category == None:
        Tistory.writePost(req)
        return

    try:
        categoryId = UserInfo.get_category_id_by_name(category)
        req['category'] = categoryId
        Tistory.writePost(req)
    except:
        print('카테고리 정보를 확인해주세요. (user.json)')

@click.command()
@click.argument('id', nargs=-1)
@click.argument('file', nargs=1)
@click.option('-cg', '--category', help="카테고리 이름 입력")
def modify(category, id, file):
    f = open(file, "r")

    req = {
        "postId": id,
        'title': os.path.basename(f.name).split('.')[0], 
        'content':f.read(),
    }

    if category == None:
        Tistory.modifyPost(req)
        return

    try:
        categoryId = UserInfo.get_category_id_by_name(category)
        req['category'] = categoryId
        Tistory.modifyPost(req)
    except:
        print('카테고리 정보를 확인해주세요. (user.json)')



cli.add_command(init)
cli.add_command(category)
cli.add_command(token)
cli.add_command(write)
cli.add_command(modify)

if __name__ == '__main__':
    cli()