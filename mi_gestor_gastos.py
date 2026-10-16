#------Constantes-----#
#Valores fijos#
presupuesto_semanal = 100 #Lo maximo que quiero gastar en la semana#
limite_gasto_alto = 20 


#------Lista de gastos-----#
gastos = [
("supermercado", 32.50),
("transporte", 15.00),
("cine", 9.50),
("cena con amigas", 24.00),
("cafe", 3.20),
("farmacia", 12.80),
("suscripción streaming", 12.80),]

#Titulo del programa
print("===Mis gastos semanales===")
# Recorremos la lista con un bucle for.
# En cada vuelta, la tupla se "desempaqueta" en dos variables:
# descripcion (el texto) e importe (el número).
for descripcion, importe in gastos:
    # f"..." permite meter variables dentro del texto con { }.
    # :.2f significa "mostrar el número con 2 decimales".
    print(f"- {descripcion}: {importe:.2f} €")

# ---------- 2. TOTAL DE LOS GASTOS ----------
# Creamos una variable acumuladora que empieza en 0.
total = 0

# Recorremos otra vez la lista y vamos sumando cada importe al total.
# "total += importe" es lo mismo que "total = total + importe".
for descripcion, importe in gastos:
    total += importe

# \n al principio deja una línea en blanco antes de mostrar el total.
print(f"\nTotal gastado: {total:.2f} €")

# ---------- 3. GASTO MEDIO ----------
# La media es el total dividido entre el número de gastos.
# len(gastos) devuelve cuántos elementos tiene la lista (aquí, 7).
media = total / len(gastos)

# Mostramos la media con 2 decimales.
print(f"Gasto medio: {media:.2f} €")

# ---------- 4. GASTOS QUE SUPERAN LOS 20 € ----------
print(f"\nGastos que superan los {limite_gasto_alto} €:")

# Esta variable funciona como un "interruptor": empieza en False
# (no hemos encontrado ningún gasto alto todavía).
hay_gastos_altos = False

# Recorremos la lista otra vez, mirando cada gasto.
for descripcion, importe in gastos:
    # Si el importe es mayor que el límite, lo mostramos.
    if importe > limite_gasto_alto:
        print(f"- {descripcion}: {importe:.2f} €")
        # Cambiamos el interruptor a True: hemos encontrado al menos uno.
        hay_gastos_altos = True

# Si al terminar el bucle el interruptor sigue en False,
# significa que ningún gasto superó el límite.
if not hay_gastos_altos:
    print("Ninguno.")

    # ---------- 5. COMPARACIÓN CON EL PRESUPUESTO SEMANAL ----------
# Línea en blanco para separar esta parte de la anterior.
print()

# Si el total es mayor que el presupuesto, ejecuta el primer bloque.
if total > presupuesto_semanal:
    # Calculamos cuánto nos hemos pasado.
    exceso = total - presupuesto_semanal
    print(f"⚠ Te has pasado del presupuesto de {presupuesto_semanal} € por {exceso:.2f} €.")
# Si no (el total es menor o igual), ejecuta este otro bloque.
else:
    # Calculamos cuánto dinero nos queda disponible.
    restante = presupuesto_semanal - total
    print(f"✔ Estás dentro del presupuesto de {presupuesto_semanal} €. Te quedan {restante:.2f} €.")
    


