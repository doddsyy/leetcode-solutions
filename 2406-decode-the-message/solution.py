class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        unique_letters = []
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        ans = []
        for letter in key.replace(' ',''):
            if letter not in unique_letters:
                unique_letters.append(letter)
        
        my_dict = dict(zip(unique_letters,alpha ))
        print(my_dict)
        for l in message:
            if l == ' ':
                ans.append(' ')
            else:
                ans.append(my_dict[l])
        return ''.join(ans)
        
