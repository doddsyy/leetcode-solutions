class Solution:
    def interpret(self, command: str) -> str:

        output = ''
        index = 0

        for i in range(len(command)):
            if command[i] == 'G':
                output+= 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    output+= 'o'
                else: 
                    output += 'al'

        return output     
