from operator import attrgetter, itemgetter
from itertools import groupby

class User:
    def __init__(self, user_id, user_name) -> None:
        self.user_id = user_id
        self.user_name = user_name
    def __repr__(self) -> str:
        return f'User({self.user_id})_{self.user_name}'

users = [User(23, 'S_1'), User(3, 'S_2'), User(2, 'S_3'), User(2, 'S_4'), User(99, 'S_5'), User(2, 'S_5'), User(3, 'S_6'), User(2, 'S_7')]

def output_groupby(items, key):
    for id, item in groupby(items,key=itemgetter(key)):
        print(f'{id=}')
        for ele in item:
            print(ele)
    print('='*30)

def groupby_item():
    tmp_arr = [{'user_id': user.user_id, 'name': user.user_name} for user in users]
    print('unsorted arr')
    output_groupby(tmp_arr, 'user_id')
    tmp_arr.sort(key=itemgetter('user_id'))
    print('sorted arr')
    output_groupby(tmp_arr, 'user_id')
    
    
            
def sorted_by_attr():
    sorted_with_lambda = sorted(users, key= lambda u : u.user_id)
    sorted_with_attrgetter = sorted(users, key= attrgetter('user_id'))
    print(f'{sorted_with_lambda=}')
    print(f'{sorted_with_attrgetter=}')

if __name__ == '__main__':
    #sorted_by_attr()
    groupby_item()