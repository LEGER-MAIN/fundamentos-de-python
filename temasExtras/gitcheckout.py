"""Ejemplos de comandos Git relacionados con cambiar de rama."""

# Git se ejecuta en la terminal, no se importa como un modulo de Python.
# En versiones actuales se recomienda `git switch` para cambiar de rama.
comandos = [
    "git branch                 # listar las ramas",
    "git switch main            # cambiar a la rama main",
    "git switch -c nueva-rama   # crear y cambiar a una rama",
]

# Se muestran como texto: este programa no ejecuta comandos ni modifica ramas.
for comando in comandos:
    print(comando)
