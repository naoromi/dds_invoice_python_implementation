import pandas as pd

class Item:
    def __init__(self, item_msrp_dataframe):
        self.item_msrp_dataframe = item_msrp_dataframe
        self.object_type = None
        self.texture = None
        self.name = None
        self.price = None
        self.quantity = None
        self.total = None

    def select_object_type(self):
        object_types = self.item_msrp_dataframe["object_type"].unique()
        for i, object_type in enumerate(object_types):
            print(f"{i}: {object_type}")
        
        try:
            object_type_index = int(input("Choose an object type (enter number): "))
            if 0 <= object_type_index < len(object_types):
                self.object_type = object_types[object_type_index]
                return True
            else:
                print("Invalid object type index. Please try again.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False

    def select_texture(self):
        textures = self.item_msrp_dataframe.loc[
            self.item_msrp_dataframe["object_type"] == self.object_type, 
            "object_texture"
        ].unique()
        
        for i, texture in enumerate(textures):
            print(f"{i}: {texture}")
        
        try:
            texture_index = int(input("Choose a texture (enter number): "))
            if 0 <= texture_index < len(textures):
                self.texture = textures[texture_index]
                return True
            else:
                print("Invalid texture index. Please try again.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False

    def select_name(self):
        object_names = self.item_msrp_dataframe.loc[
            self.item_msrp_dataframe["object_texture"] == self.texture, 
            "object_name"
        ].unique()
        
        for i, object_name in enumerate(object_names):
            print(f"{i}: {object_name}")
        
        try:
            object_name_index = int(input("Choose an object name (enter number): "))
            if 0 <= object_name_index < len(object_names):
                self.name = object_names[object_name_index]
                return True
            else:
                print("Invalid object name index. Please try again.")
                return False
        except ValueError:
            print("Please enter a valid number.")
            return False

    def set_quantity(self):
        try:
            self.quantity = int(input("Enter the item quantity: "))
            return True
        except ValueError:
            print("Please enter a valid number.")
            return False

    def calculate_price(self):
        full_model_name = f"{self.texture} - {self.name}"
        self.price = self.item_msrp_dataframe.loc[
            self.item_msrp_dataframe["full_model_name"].str.lower().str.replace(" ", "") == 
            full_model_name.lower().replace(" ", ""), 
            "msrp"
        ].values[0]
        self.total = self.price * self.quantity

    def add_item(self):
        if not self.select_object_type():
            return None
        if not self.select_texture():
            return None
        if not self.select_name():
            return None
        if not self.set_quantity():
            return None
        
        self.calculate_price()
        return {
            "item": f"{self.texture} - {self.name}",
            "quantity": self.quantity,
            "price": self.price,
            "total": self.total
        } 