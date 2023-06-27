# 7.21 Class Decorators

_registry = {}

def register_decoder(cls):
    for mt in cls.mimetypes:
        _registry[mt] = cls
    return cls

# Factory function that uses registry
def create_decoder(mimetype):
    return _registry[mimetype]()

@register_decoder
class TextDecoder:
    mimetypes = ['text/plain']
    def decode(self, data):
        print("TextDecoder::decode")

@register_decoder
class HtmlDecoder:
    mimetypes = ['text/html']
    def decode(self, data):
        print("HtmlDecoder::decode")
        
@register_decoder
class ImageDecoder:
    mimetypes = ['image/png', 'image/jpg', 'image/gif']
    def decode(self, data):
        print("ImageDecoder::decode")
        
if __name__ == '__main__':  
    decoder = create_decoder('image/jpg')
    data = "Some data"
    decoder.decode(data)
    
