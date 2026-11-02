from datasets import load_dataset

ds = load_dataset("json", data_files="chat.jsonl", split="train")
print(ds)
print(ds[0])