class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        book = defaultdict(list)
        
        for path in paths:
            vals = path.split(" ")
            dir_name = vals[0] + "/"
            
            for i, val in enumerate(vals):
                if i == 0:
                    continue
                first_index, last_index = val.index('(') + 1, val.index(')')
                file_content = val[first_index:last_index]
                file_name = val[:first_index - 1]
                
                if file_content not in book:
                    book[file_content] = [dir_name + file_name]
                else:
                    book[file_content].append(dir_name + file_name)
       
        return [book[key] for key in book.keys() if len(book[key]) > 1]
            