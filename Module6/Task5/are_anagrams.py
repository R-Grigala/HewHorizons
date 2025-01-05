def are_anagrams(text1, text2):

    cleaned_text1 = sorted(text1.lower().replace(" ", ""))
    cleaned_text2 = sorted(text2.lower().replace(" ", ""))

    return cleaned_text1 == cleaned_text2

inpt_text1 = input("Enter the first text: ").strip()
inpt_text2 = input("Enter the second text: ").strip()

if inpt_text1 and inpt_text2 and are_anagrams(inpt_text1, inpt_text2):
    print("Anagrams")
else:
    print("Not anagrams")