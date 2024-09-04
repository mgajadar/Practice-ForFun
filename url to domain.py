url = input("Paste URL:\n")

#Remove the www. if present
if "www." in url:
    url = url.replace("www.", "")

# Step 2: Extract the domain name by splitting at '//' and then at '.'
domain = url.split("//")[-1].split(".")[0]

print(domain)