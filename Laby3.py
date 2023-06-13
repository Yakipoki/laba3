class Obj:
    def __init__(self, softness, material, color): 
        self._softness = softness
        self._material = material
        self._color = color

    def get_softness(self):
        return self._softness

    def get_age(self):
        return self._material

    def get_gender(self):
        return self._color


    def set_softness(self, softness):
        self._softness = softness

    def set_age(self, material):
        self._material = material

    def set_gender(self, color):
        self._color = color


cube = Obj(False, "metal", "green")




print(f"Объект => Куб \nМягкий => {cube._softness}\nМатериал => {cube._material}\nЦвет => {cube._color}")