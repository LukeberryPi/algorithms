# https://leetcode.com/problems/assign-cookies/

greeds = [1,2]
sizes = [1,2,3]

def find_content_children(children_greed_values, cookie_sizes):
    content_children = 0
    available_cookies = len(cookie_sizes)

    for greed in children_greed_values:

        if not available_cookies:
            break

        if any(cookie >= greed for cookie in cookie_sizes):
            content_children += 1
            available_cookies -= 1

    return content_children

print(find_content_children(greeds, sizes))