# Counting instances — class attributes vs instance attributes


class User:
    # Class attribute to count instances
    instance_count = 0

    def __init__(self, name):
        self.name = name  # Instance attribute
        User.instance_count += 1  # Increment the class attribute

    @classmethod
    def get_instance_count(cls):
        return cls.instance_count




user1 = User("Alice")   

user2 = User("Bob")

print(f"Total instances created: {User.get_instance_count()}")  # Output: Total instances created: 2    
