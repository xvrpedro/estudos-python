conj1 = {"Carlos", "Josiel", "Jandira", "Aline"}
conj2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

# aqui eu uso intersecção, pois é o ponto aonde os dois conjuntos batem.
print(f"\"Quem são as pessoas que estão presentes nos dois grupos?\": {conj1.intersection(conj2)}")

# diferença simétrica tira as intersecções, os repetidos e ficam apenas os não repetidos.
print(f"\"Quem são as pessoas que estão apenas em um grupo?\": {conj1.symmetric_difference(conj2)}")