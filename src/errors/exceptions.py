from fastapi import HTTPException

class HTTPInternalException(HTTPException):
    status_code = 500
    
    def __init__(self, detail:str| None = None):
        if detail is not None:
            self.detail = detail
        super().__init__(self.status_code, detail)
    
class NotFoundException(HTTPInternalException):
    status_code = 404
    detail = 'Not found'
    
    
    