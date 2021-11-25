import config as cfg
import re

# for freq in cfg.list_freqs:
#     # place txt_i
#     with_txt_i = freq.replace("[n]", "[inspoint_n]")

# for freq in cfg.list_freqs:
#     row_elements = []
#     splits = freq.split("[n]")
#     for split in splits:
#         if len(splits) == 1:
#             print("Only one string in this split.")
#             print(f"Create radio button with string {split}")
#             row_elements.append(split)
#         else:
#             if split == "[n]":
#                 print("Create LineEdit for n")
#                 row_elements.append(f"LineEdit {split}")
#     # row_elements.append()
#     print(row_elements)

for freq in cfg.list_freqs:
    splits = re.split("([n])|([i])", freq)
    print(splits)
