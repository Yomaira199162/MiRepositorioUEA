def calcular_descuento(monto, porcentaje=10):
 #Calcula el monto del descuento
    monto = float(monto)
    porcentaje = float(porcentaje)
    descuento = monto * (porcentaje / 100)
    return descuento

if __name__=="__main__":
  # llamada 1: solo con monto (usa el 10% por defecto)
  monto1= 100 # <- Aquí va el monto nº 1
  descuento1 = calcular_descuento(monto1)
  total1= monto1 - descuento1
  print(f"Ejemplo 1 -> Monto: ${monto1:.2f} | Descuento: (10%: ${descuento1:.2f} | Total a pagar: ${total1:.2f}")

  # llamada 2: con monto y porcentaje indicado (15%)
  monto2= 250  # <- Aquí va el monto nº 2
  porcentaje2 = 25 # <- Ingreso manualmente el porcentaje de descuento
  descuento2 = calcular_descuento(monto2, porcentaje2)
  total2= monto2 - descuento2
  print(f"Ejemplo 2 -> Monto: ¨{monto2:.2f} | Descuento ({porcentaje2}%): ${descuento2:.2f} | Total a pagar: ${total2:.2f}")
