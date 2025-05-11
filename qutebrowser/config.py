config.load_autoconfig()

# Sobrescribimos los atajos de scroll
config.bind('zk', 'tab-next', mode='normal')
config.bind('zj', 'tab-prev', mode='normal')

config.bind('<Ctrl-1>', 'tab-focus 1')  # Ir a la pestaña 1
config.bind('<Ctrl-2>', 'tab-focus 2')  # Y así sucesivamente

