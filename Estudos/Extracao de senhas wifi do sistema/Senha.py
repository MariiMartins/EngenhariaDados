import subprocess

# Obtendo os dados dos perfis de Wi-Fi
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# Decodificando os dados
data = meta_data.decode('utf-8', errors="backslashreplace")

# Dividindo os dados linha por linha
data = data.split('\n')

# Criando uma lista para armazenar os perfis
profiles = []

# Percorrendo os dados
for i in data:
    # Encontrando "All User Profile" em cada item
    if "All User Profile" in i:
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        profiles.append(i)

# Exibindo cabeçalho
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("__" * 30)

# Percorrendo os perfis
for i in profiles:
    try:
        # Obtendo os dados do perfil, incluindo a senha
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', i, 'key=clear'])

        # Decodificando e dividindo os resultados linha por linha
        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')

        # Encontrando a senha nos resultados
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        # Exibindo o nome do perfil e a senha (se houver)
        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))

    # Caso ocorra algum erro no processo
    except subprocess.CalledProcessError:
        print("Erro ao tentar obter as informações do perfil.")
