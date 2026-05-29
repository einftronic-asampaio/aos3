#pip install psutil
import psutil
# Monitorar o uso de CPU
print(f"Uso da CPU: {psutil.cpu_percent(interval=1)}%")
# Monitorar o uso de memória
mem = psutil.virtual_memory()
print(f"Memória usada: {mem.percent}%")
