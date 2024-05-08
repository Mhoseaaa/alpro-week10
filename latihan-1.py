# Definisikan dictionary
dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Cetak header
print("key\tvalue\titem")

# Loop melalui setiap pasangan kunci-nilai dalam dictionary
for key, value in dictionary.items():
    print(f"{key}\t{value}\t{key}")  # Cetak kunci, nilai, dan kunci lagi sebagai item
