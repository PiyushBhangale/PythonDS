import pyhash
# Define FNV and Murmur hash functions from Pyhash.
bit_vector = [0]*20
print(bit_vector)
fnv_hasher = pyhash.fnv1_32()
murmur_hasher = pyhash.murmur3_32()

# Calculate output of FNV and Murmur hash for Pikachu and Charmander.
fnv_hash_pikachu = fnv_hasher("Pikachu") % 20
murmur_hash_pikachu = murmur_hasher("Pikachu") % 20

fnv_hash_charmander = fnv_hasher("Charmander") % 20
murmur_hash_charmander = murmur_hasher("Charmander") % 20

# Print the output of FNV and Murmur hashes.
print("FNV hash output for Pikachu: " + str(fnv_hash_pikachu))
print("Murmur hash output for Pikachu: " + str(murmur_hash_pikachu))

print("FNV hash output for Charmander: " + str(fnv_hash_charmander))
print("Murmur hash output for Charmander: " + str(murmur_hash_charmander))

# Flip the bits of bit_vector in the corresponding locations from above hashes.
bit_vector[fnv_hash_pikachu] = 1
bit_vector[murmur_hash_pikachu] = 1

bit_vector[fnv_hash_charmander] = 1
bit_vector[murmur_hash_charmander] = 1

print(bit_vector)

# Calculate output of FNV and Murmur hash for Bulbasaur.
fnv_hash_bulbasaur = fnv_hasher("Bulbasaur") % 20
murmur_hash_bulbasaur = murmur_hasher("Bulbasaur") % 20

# Print the FNV and Murmur hashes of Bulbasaur.
print("FNV hash output for Bulbasaur: " + str(fnv_hash_bulbasaur))
print("Murmur hash output for Bulbasaur: " + str(murmur_hash_bulbasaur))

print(bit_vector[fnv_hash_bulbasaur])
print(bit_vector[murmur_hash_bulbasaur])
