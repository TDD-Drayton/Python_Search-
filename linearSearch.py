#Python
thisList = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh"]
target = "aaa"


def linear_search(search_list, target_value):
    matches = []
   for x in range(len(search_list)):
       if search_list[x] == target_value:
            matches.append(x)
   if matches:
       return matches
   else:
       raise ValueError(f"{target_value} not in list")


if __name__ == "__main__":

   # Function call
    tL_position= linear_search(thisList, target)
   print(tL_position)
   

#Output [0, 7]
