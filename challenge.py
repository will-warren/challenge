"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring_charsing of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

def compare(string1, substring2):
    perm_list = []
    build_perm_list(substring_chars=list(substring2), start=0, stop=len(substring2), perm_list=perm_list)

    # one simple, brute force way to test membership
    for pp in perm_list:
        if(pp in string1):
            return True

    # no match found
    return False


def build_perm_list(substring_chars, start, stop, perm_list):
    if(start == stop):
        perm_list.append(''.join(substring_chars))
        return None
    
    for i in range(start, stop):
        substring_chars[start], substring_chars[i] = substring_chars[i], substring_chars[start]
        build_perm_list(substring_chars=substring_chars, start=start + 1, stop=stop, perm_list=perm_list)
        substring_chars[start], substring_chars[i] = substring_chars[i], substring_chars[start]

def different_compare_method(string1, substring2):
    found_perms = find_perms(substring_chars=list(substring2), start=0, stop=len(substring2), match_str=string1)

    # No perms found
    if(found_perms is None):
        return False

    return True

def find_perms(substring_chars, start, stop, match_str):
    if(''.join(substring_chars) in match_str):
        return True

    if(start == stop):
        return None
    
    for i in range(start, stop):
        substring_chars[start], substring_chars[i] = substring_chars[i], substring_chars[start]
        found = find_perms(substring_chars=substring_chars, start=(start + 1), stop=stop, match_str=match_str)
        # match found! no futher processing required
        if(found is True):
            return True
        substring_chars[start], substring_chars[i] = substring_chars[i], substring_chars[start]

def main():
    # Test when two strings are identical
    assert compare(string1='test', substring2='test') is True
    # Test when no match is found
    assert compare(string1='abcd', substring2='efgh') is False
    # Test example input
    assert compare(string1='eidbaooo', substring2='ab') is True
    # Test example input
    assert compare(string1='eidboaoo', substring2='ba') is False
    # Test a long string with many possible permutations
    assert compare(string1='aquickbrownfoxjumpedoverthelazydog', substring2='xofnworb') is True

    # Advantages
    #   - time complexity is lower because you do one 'in' operation and one for loop.
    #
    # Problems with this approach:
    #   - potential for large space complexity if an array of 10,000! permutations must be built


    # A DIFFERENT APPROARCH.You could also test if a match exists after permutation is generated.  If a match is found, break the loop and return True. 
    # This way we do not have to continue to iterate after a match is found. It also avoids holding a list of permutations in memory.


    # Test when two strings are identical
    assert different_compare_method(string1='test', substring2='test') is True
    # Test when no match is found
    assert different_compare_method(string1='abcd', substring2='efgh') is False
    # Test example input
    assert different_compare_method(string1='eidbaooo', substring2='ab') is True
    # Test example input
    assert different_compare_method(string1='eidboaoo', substring2='ba') is False
    # Test a long string with many possible permutations
    assert different_compare_method(string1='aquickbrownfoxjumpedoverthelazydog', substring2='xofnworb') is True

    # Advantages of this approach
    # - less space complexity because we do not store a list of permuations in memory
    # 
    # Problems with this approach
    # - 'in' keyword is ran on every iteration, which this may outweigh the time saved by stopping the iteration when a match is found.

if __name__ == '__main__':
    main()