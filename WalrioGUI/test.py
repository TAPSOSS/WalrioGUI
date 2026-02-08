class Greeter:
    """
    A class that greets people.
    """

    def greet(self, name: str) -> str:
        """
        Return a personalized greeting.

        Args:
            name (str): The name to greet.
            
        Returns:
            str: the greeting message.
        """
        return f"Hi {name}!"