class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        """
        Implementa la operación lógica AND.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a AND b
        """
        if(a == True and b == True):
            return True
        else:
            return False
        pass
    
    def OR(self, a, b):
        """
        Implementa la operación lógica OR.
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a OR b
        """
        if (a == False and b == False):
            return False
        else:
            return True
        pass
    
    def NOT(self, a):
        """
        Implementa la operación lógica NOT.
        
        Args:
            a (bool): Valor booleano
            
        Returns:
            bool: Resultado de NOT a
        """
        if (a == True):
            return False
        else:
            return True
        pass
    
    def XOR(self, a, b):
        """
        Implementa la operación lógica XOR (OR exclusivo).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XOR b
        """
        if (a == b):
            return False
        else:
            return True
        pass
    
    def NAND(self, a, b):
        """
        Implementa la operación lógica NAND (NOT AND).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NAND b
        """
        if(a == True and b == True):
            return False
        else:
            return True
        pass
    
    def NOR(self, a, b):
        """
        Implementa la operación lógica NOR (NOT OR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a NOR b
        """
        if(a == False and b == False):
            return True
        else:
            return False
        pass
    
    def XNOR(self, a, b):
        """
        Implementa la operación lógica XNOR (NOT XOR).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de a XNOR b
        """
        if(a == b):
            return True
        else:
            return False
        pass
    
    def implicacion(self, a, b):
        """
        Implementa la operación lógica de implicación (a -> b).
        
        Args:
            a (bool): Primer valor booleano (antecedente)
            b (bool): Segundo valor booleano (consecuente)
            
        Returns:
            bool: Resultado de la implicación
        """
        if(a == True and b == False):
            return False
        else:
            return True
        pass
    
    def bi_implicacion(self, a, b):
        """
        Implementa la operación lógica de bi-implicación (a <-> b).
        
        Args:
            a (bool): Primer valor booleano
            b (bool): Segundo valor booleano
            
        Returns:
            bool: Resultado de la bi-implicación
        """
        if(a == b):
            return True
        else:
            return False
        pass
    
    
