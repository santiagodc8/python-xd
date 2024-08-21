# Escribe un programa que asigne una calificación (A, B, C, D, F) según una nota dada.
# Asigna una calificación según la nota
# A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: menos de 60

nota = 10

if nota >= 90 and nota <= 100:
    print(f"tu nota {nota} corresponde a la calificacion A")
elif nota >= 80 and nota <= 89:
    print(f"tu nota {nota} corresponde a la calificacion B")
elif nota >= 70 and nota <= 79:
    print(f"tu nota {nota} corresponde a la calificacion C")
elif nota >= 60 and nota <= 69:
    print(f"tu nota {nota} corresponde a la calificacion D")
else: print(f"tu nota {nota} corresponde a la calificacion F")

#solucion chatgpt

# Dada una nota
nota = 85  # Puedes cambiar este valor para probar diferentes casos

# Asigna una calificación según la nota
if nota >= 90:
    calificacion = 'A'
elif nota >= 80:
    calificacion = 'B'
elif nota >= 70:
    calificacion = 'C'
elif nota >= 60:
    calificacion = 'D'
else:
    calificacion = 'F'

print("La calificación es:", calificacion)
