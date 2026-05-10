class TACGen:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []

    # Helpers

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"
    
    def emit(self, inst):
        self.code.append(inst)

    def print_code(self):
        for line in self.code:
            print(line)

    #-------------------------#
    # BASE DE PRODUCAO DA TAC #
    #-------------------------#

    def generate(self, node):
        node_type = node["type"]

        match node_type:
            # Programa
            case "Program":
                for item in node["items"]:
                    self.generate(item)  
            
            # Prototipos
            case "Prototype":
                pass

            # Declaracao de funcoes
            case "FunctionDef":
                name = node["name"]
                self.emit(f"\nfunc {name}:")

                # Parametros da funcao
                for param in node["params"]:
                    name = param["decl"]["name"]
                    self.emit(f"param {name}")

                # Corpo da funcao
                self.generate(node["body"])

                self.emit("endfunc")

            # Blocos de statments
            case "Block":
                for stat in node["statements"]:
                    self.generate(stat)

            # Return
            case "Return":
                value = self.generate(node["value"])
                self.emit(f"return {value}")

            # Numericos
            case "Number":
                return str(node["value"])
            
            # Identificadores
            case "Identifier":
                return node["name"]
            
            # Operadores Binarios  !!! Rever os agregadores AND e OR Estão aqui a entrar !!!
            case "BinaryOp":
                left = self.generate(node["left"])
                right = self.generate(node["right"])

                temp = self.new_temp()

                self.emit(f"{temp} = {left} {node["op"]} {right}")

                return temp
            
            # Call
            case "Call":
                args = node["args"]

                for arg in args:
                    arg_value = self.generate(arg)
                    self.emit(f"param {arg_value}")
                
                temp = self.new_temp()

                self.emit(f"{temp} = call {node["name"]}, {len(args)}")

                return temp
            
            # Call funcoes internas
            case "BuiltInCall":
                name = node["name"]

                if "escrever" in name:
                    for arg in node["args"]:
                        value = self.generate(arg)
                        self.emit(f"write {value}")
                elif "ler" in name:
                    temp = self.new_temp()
                    self.emit(f"{temp} = read")
                    return temp
            
            #
            # ADICIONAR caso para os IF/ELSE, WHILE, FOR e Assignacao, escalares e vetores
            
            # -- Exibe validaco se no em falta
            case _:
                raise Exception(f"No nao identificado --> {node_type}")
            