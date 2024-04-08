# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

#  Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['a','e','i','o','u','A','E','I','O','U'];
        indexes=[];
        for i in range(0,len(s)):
            if s[i] in l:
                indexes.append(i);
        reversed_indexes = indexes[::-1]

        new_str = ""
        for i in range(len(s)):
            if i in indexes:
                new_str += s[reversed_indexes[indexes.index(i)]]
            else:
                new_str += s[i]

        return new_str
solution = Solution()
s="hello"
print(solution.reverseVowels(s))


# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels=['a','e','i','o','u','A','E','I','O','U'];
#         indexofvowels=[];
#         reverseindexofvowels=[];
#         for i in range(len(s)):
#             if s[i] in vowels:
#                 indexofvowels.append(i)
        
#         reverseindexofvowels=indexofvowels[::-1]
#         print(indexofvowels)
#         print(reverseindexofvowels)
#         newstring=""
#         count=0
#         for i in range(len(s)):
#             if i in indexofvowels:
#                 newstring=newstring+s[reverseindexofvowels[count]]
#                 count+=1
#             else:
#                 newstring=newstring+s[i]
#         return(newstring)