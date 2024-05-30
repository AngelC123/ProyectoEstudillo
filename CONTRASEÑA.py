import hashlib

def hash_password(password: str) -> str:
    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')
    # Crear un objeto hash SHA-256
    hash_object = hashlib.sha256(password_bytes)
    # Obtener el valor hexadecimal del hash
    password_hash = hash_object.hexdigest()
    return password_hash

# Ejemplo de uso
contraseña = "chupin"
hashed_contraseña = hash_password(contraseña)
print(f"Contraseña: {contraseña}")
print(f"Hash: {hashed_contraseña}")
if "587928cf9ec142335508a4bb05bfa0af1da47296d3aef2b3e5c20ba6fbc3ce7b" == hashed_contraseña:
    print("SIIII")

#CONTRASEÑA MIGUEL = 123456789
#CONTRASEÑA SARA = basket123
#CONTRASEÑA ALEX = cruzazul
#CONTRASEÑA LEONARDO = chupin
