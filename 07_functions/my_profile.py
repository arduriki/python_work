def my_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


profile_data = my_profile('jordi', 'ardura', location='vic', age=36, work='programmer')

print(profile_data)