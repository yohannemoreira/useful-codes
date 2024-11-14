from jinja2 import Environment, FileSystemLoader

def snake_to_title_case(value):
    return ' '.join(word.capitalize() for word in value.split('_'))

# Carrega o template e adiciona o filtro ao ambiente Jinja2
env = Environment(loader=FileSystemLoader('templates'))
env.filters['snake_to_title'] = snake_to_title_case
