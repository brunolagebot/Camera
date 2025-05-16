import multiprocessing

# Gerenciador de filas para troca de frames entre processos
t_manager = multiprocessing.Manager()
frame_queue = t_manager.Queue(maxsize=10)
output_queue = t_manager.Queue(maxsize=10) 