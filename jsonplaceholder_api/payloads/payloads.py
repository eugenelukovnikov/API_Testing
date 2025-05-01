
class Payload:

    @staticmethod
    def post():
        return {
                'title': 'foo',
                'body': 'bar',
                'userId': 1
            }
    
    @staticmethod
    def put():
        return {
                'title': 'putted_title',
                'body': 'foo',
                'userId': 1
            }
    
    @staticmethod
    def patch():
        return {
                'title': 'patched_title',
            }