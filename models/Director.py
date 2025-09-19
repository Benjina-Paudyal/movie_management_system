class Director:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    # --- GETTERS AND SETTER ---
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name:
            self.__name = new_name
        else:
            raise ValueError("Director name cannot be empty.")
        
    # --- CONVERT TO JSON ---
    def to_json(self):
        return {
            "id" : self.id,
            "name" : self.name
        }