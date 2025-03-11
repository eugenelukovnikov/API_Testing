
class Payload:

    @staticmethod
    def post():
        return {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    
    @staticmethod
    def put():
        return {
            "name": "Apple MacBook Pro 20",
            "data": {
                "year": 2020,
                "price": 1999.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
    
    @staticmethod
    def patch():
        return {
            "name": "Oops, I destroyed the name"
        }
