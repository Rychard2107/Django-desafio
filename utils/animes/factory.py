from faker import Faker

fake = Faker('pt_BR')


def make_fake_anime():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'nome_anime': fake.sentence(nb_words=3),
        'resumo': fake.text(3000),
        'data_criacao': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'genero': fake.word(),
        'img_anime': {
            'url': 'https://loremflickr.com/320/240',
        },
        'episodios': fake.random_number(digits=2, fix_len=True),
    }
