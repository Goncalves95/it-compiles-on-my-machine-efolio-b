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
            # ADICIONAR caso para os WHILE, FOR e vetores
            
            # Declaracao de variaveis
            case "Declaration":
                for decl in node["declarators"]:
                    self.generate(decl)
            
            # Inicializacoes 
            case "InitDeclarator":
                target = self.generate(node["target"])
                val = self.generate(node["value"])

                self.emit(f"{target} = {val}")

                return None
            
            # Operacoes Unarias
            case "UnaryOp":
                operand = self.generate(node["operand"])

                temp = self.new_temp()

                self.emit(f"{temp} = {node["op"]}{operand}")
            
            # If/Else !!! Esta com um erro na geracao de temporarios !!!
            case "If":
                if node["else"] is not None:
                    label_else = self.new_label()
                else:
                    label_else = None

                label_end = self.new_label()

                if label_else is None:
                    label_else = label_end

                condition = self.generate(node["condition"])

                self.emit(f"ifFalse {condition} goto {label_else}")

                self.generate(node["then"])

                self.emit(f"goto {label_end}")

                if node["else"] is not None:
                    self.emit(f"{label_else}")
                    self.generate(node["else"])

                self.emit(f"{label_end}")


            
            # -- Exibe validaco se no em falta
            case _:
                raise Exception(f"No nao identificado --> {node_type}")
            