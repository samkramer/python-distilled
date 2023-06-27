# 7.21 Class Decorators

def loud(cls):
    orig_noise = cls.noise
    def noise(self):
        return orig_noise(self).upper()
    cls.noise = noise
    return cls

def annoying(cls):
    orig_pedal = cls.pedal
    def pedal(self):
        return 3 * orig_pedal(self)
    cls.pedal = pedal
    return cls

@annoying
@loud
class Cyclist(object):
    def noise(self):
        return 'On your left!'
    def pedal(self):
        return 'Pedaling'

if __name__ == '__main__':  
    cyclist = Cyclist()
    print(cyclist.noise())
    print(cyclist.pedal())