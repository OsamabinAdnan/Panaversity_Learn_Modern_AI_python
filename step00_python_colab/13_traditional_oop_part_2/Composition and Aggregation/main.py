# Composition

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        return "Car starting",self.engine.start()

# Car and Engine demonstrate composition. The Car class creates and owns an instance of the Engine class. If the Car object is destroyed, the Engine object is also destroyed.

# Aggregation
class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = [] # University has departments but does not own them
    
    def add_department(self, department):
        self.departments.append(department)

# University and Department demonstrate aggregation. The University class contains a list of Department objects, but the Department objects can exist independently of the University object. The university does not exclusively own the Department.