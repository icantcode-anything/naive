import re

text = (
    "On a quiet night, Sarah walked through the garden, gazing at the endless sky. "
    "The wind felt Soft as it brushed against her face, whispering Tales of distant galaxies. "
    "Along the path, a lantern flickered, reminding her of childhood Adventures spent wishing upon the glowing moon. "
    "In the stillness, she realized that among all the chaos of life, there will always be a Reason to look up — "
    "a shining reminder that hope never fades."
)

# Find capitalized words that aren't at the start of a sentence
caps = [
    w for w in re.findall(r'\b[A-Z][a-z]+\b', text)
    if not re.search(r'(?:^|[.!?]\s+)' + w, text)
]

# Keep only the intended hidden words
hidden_words = ["Soft", "Tales", "Adventures", "Reason"]
filtered_caps = [w for w in caps if w in hidden_words]

hidden = ''.join(w[0] for w in filtered_caps)

print("Capitalized mid-sentence words:", filtered_caps)
print("Hidden message:", hidden)
