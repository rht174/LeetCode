class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        num = ('2', '4', '6', '8')
        ch = ('b', 'd', 'f', 'h')
        
        if coordinates[0] in ch and coordinates[1] in num:
            return False
        
        elif coordinates[0] in ch and coordinates[1] not in num:
            return True
        
        elif coordinates[0] not in ch and coordinates[1] in num:
            return True
        
        else:
            return False