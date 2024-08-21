#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de durancion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentaje de tiempo vacìo removido
tiempo_vacio_promedio =  100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto =  100 - dalto_curso * 1000 // crudo_dalto / 10

print("--------------------------")
print("El curso de Dalto dura: ")
print(f"- un {int(diferencia_con_min)}% menos que el mas rapido")
print(f"- un {int(diferencia_con_max)}% menos que el mas lento")
print(f"- un {int(diferencia_con_promedio)}% menos que el promedio")
print("--------------------------")


print("--------------------------")
print(f"el curso promedio elimina un {int(tiempo_vacio_promedio)}% de tiempo vacio")
print(f"este curso elimino {int(tiempo_vacio_dalto)}% de tiempo vacio")
print("--------------------------")


print("--------------------------")
print(f"ver 10 horas de este curso equivale a ver {int(otros_cursos_promedio / dalto_curso * 10)} horas de otros cursos")
print(f"ver 10 horas de otros cursos equivale a ver {int(dalto_curso / otros_cursos_promedio * 10)} horas de este curso")
print("--------------------------")
