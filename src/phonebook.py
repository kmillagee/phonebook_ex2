class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190', 'BOMBEIRO': '193'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        char_special = ['#', '@', '!', '$', '%', ""] #para reduzir a qtd de ifs, criei a lista para validação de chars especiais
        if isinstance(name,str) and isinstance(number,str): #inclsusão do metodo para validar se nome e número são strings
            if name in char_special:
                return "Nome invalido"
            if number in char_special:
                return "Número invalido"
            if name not in self.entries:
                self.entries[name] = number
                return 'Registro adicionado'
            return "Nome e número não cadastrados"
        return "Nome ou número não é um valor válido"

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        #foi realizada a refatoração para diminuir a quantidade de ifs, além das validações de None, caractere especial e cadastro inexistente
        char_special = ['#', '@', '!', '$', '%', ""]
        if isinstance(name, str):
            if name in char_special:
                return "Nome invalido"
            if name in self.entries:
                return f"{name}: {self.entries[name]}"
            else:
                return "Registro não encontrado"
        else:
            return "Nome não é um valor válido"

    def get_names(self):
        """
        :return: return all names in phonebook
        """
        #foi colocada a validação de resgitro vazio, além da criação de uma lista apenas com os nomes dos usuários cadastrados
        if self.entries == {}:
            return "Phonebook não possui registro"
        else:
            names = []
            for key in self.entries.keys():
                names.append(key)
            return names

    def get_numbers(self):
        """
        :return: return all numbers in phonebook
        """
        # foi colocada a validação de resgitro vazio, além da criação de uma lista apenas com os nomes dos usuários cadastrados
        if self.entries == {}:
            return "Phonebook não possui registro"
        else:
            values = []
            for value in self.entries.values():
                values.append(value)
            return values

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        #colocada a validação caso o phonebook já esteja vazio
        if self.entries == {}:
            return 'O phonebook está vazio'
        else:
            self.entries = {}
            return 'Dados do phonebook foram limpos'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        #foi incluída a validação para verificar se o nome é uma string
        if isinstance(search_name, str) and search_name is not None:
            for name, number in self.entries.items():
                if search_name == name:
                    return f"Registro encontrado: {name}: {number}"
            return "Registro não encontrado"
        return "Nome invalido"

    def get_phonebook_sorted(self):
        """
        :return: return phonebook in sorted order
        """
        #foi realizada a refatoração para criar uma lista de
        if self.entries == {}:
            return "Phonebook está vazio"
        else:
            lista = []
            for name, number in self.entries.items():
                lista.append([name, number])
            lista.sort()
            return lista

    def get_phonebook_reverse(self):
        """
        :return: return phonebook in reverse sorted order
        """
        if self.entries == {}:
            return "Phonebook está vazio"
        else:
            lista = []
            for name, number in self.entries.items():
                lista.append([name, number])
            lista.sort(reverse=True)
            return lista

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if isinstance(name, str) and (name is not None):
            if self.entries != {}:
                if name in self.entries:
                    self.entries.pop(name)
                    return "Registro removido"
                return "Registro não encontrado"
            return "Phonebook está vazio"
        return "Nome não pode ser invalido"


    def get_name_by_number(self, search_number):
        """
        Search all substring with search_name
        :param search_number: string with number for search
        :return: return list with results of search
        """
        if isinstance(search_number, str) and (search_number is not None):
            if self.entries != {}:
                for name, number in self.entries.items():
                    if search_number == number:
                        return f"Registro encontrado: {name}"
                return "Registro não encontrado"
            return "Phonebook está vazio"
        return "Número não pode ser invalido"

    def change_number(self, name, new_number):
        if name in self.entries:
            if new_number is not None:
                self.entries[new_number] = self.entries.pop(name)
                return "Número de telefone foi modificado"
            return "Não foi possível alterar número"
        return "Não foi possivel encontrar o número"

