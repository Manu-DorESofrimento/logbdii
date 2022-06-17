from configparser import ConfigParser


def load(file='data.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(file)
    data = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            data[param[0]] = param[1]
    else:
        raise Exception('Deu pau, não achei a seção {0} no arquivo {1}'.format(section, file))

    return data