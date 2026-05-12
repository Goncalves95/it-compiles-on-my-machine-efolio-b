class TACGen:
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.str_count = 0
        self.code = []

    # Helpers

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"
    
    def new_str(self):
        self.str_count += 1
        return f"str{self.str_count}"
    
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

                self.emit(f"{temp} = {left} {node['op']} {right}")

                return temp
            
            # Call
            case "Call":
                args = node["args"]

                for arg in args:
                    arg_value = self.generate(arg)
                    self.emit(f"param {arg_value}")
                
                temp = self.new_temp()

                self.emit(f"{temp} = call {node['name']}, {len(args)}")

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
            
            # Declaracao de variaveis
            case "Declaration":
                for decl in node["declarators"]:
                    self.generate(decl)
            
            # Inicializacoes 
            case "InitDeclarator":
                # -- Variaveis declaradas nao inicializadas --
                if node["value"] is None:
                    return None
                
                target = self.generate(node["target"])
                val = self.generate(node["value"])

                self.emit(f"{target} = {val}")

                return None
            
            # Operacoes Unarias
            case "UnaryOp":
                operand = self.generate(node["operand"])

                temp = self.new_temp()

                self.emit(f"{temp} = {node['op']}{operand}")

                return temp
            
            # If/Else
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

            # Ciclo While
            case "While":
                label_start = self.new_label()
                label_end = self.new_label()

                # Inicio Loop
                self.emit(f"{label_start}:")

                # Condicao do While
                cond = self.generate(node["condition"])

                self.emit(f"ifFalse {cond} goto {label_end}")

                # Corpo do While
                self.generate(node["body"])

                self.emit(f"goto {label_start}")

                # Fim Loop
                self.emit(f"{label_end:}")

                return None
            
            # Assignação de valor simples
            case "Assignment":
                value = self.generate(node["value"])
                target = self.generate(node["target"])

                self.emit(f"{target} = {value}")

                return None
            
            # Ciclo For
            case "For":
                label_start = self.new_label()
                label_end = self.new_label()

                # Incializacao For
                self.generate(node["init"])

                self.emit(f"{label_start}:")

                # Condicao avaliada For
                cond = self.generate(node["condition"])

                self.emit(f"ifFalse {cond} goto {label_end}")

                # Corpo do For
                self.generate(node["body"])

                # Atualizacao Var For
                self.generate(node["update"])      

                # Label de retorno ao topo      
                self.emit(f"goto {label_start}")

                # Fim Loop
                self.emit(f"{label_end:}") 

            # Literais
            case "String":
                strid = self.new_str()

                self.emit(f"{strid} = \"{node["value"]}\"")

                return strid
            
            # Vetores
            case "ArrayAccess":
                indx = self.generate(node["index"])

                temp = self.new_temp()

                self.emit(f"{temp} = {node["name"]}[{indx}]")

                return temp

            
            # -- Exibe validaco se no em falta
            case _:
                raise Exception(f"No nao identificado --> {node_type}")
            
