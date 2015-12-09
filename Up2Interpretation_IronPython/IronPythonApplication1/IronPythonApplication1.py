import clr
clr.AddReference('dotnetlib1')

import dotnetlib1


class SomeObj(object):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'SomeObj({}) @ {}'.format(
            self.val, id(self))

    def ToString(self):
        return str(self)


def genNObjects(n):
    for i in range(n):
        yield SomeObj(i)



if __name__ == '__main__':
    
    sep = '\n********* \n\n'

    dotnetlib1.Up2InterpretationCls.WriteToConsole('Just A String')
    print(sep)

    dotnetlib1.Up2InterpretationCls.WriteAllToConsole(
        ['A ', 'List ', 'of ', 'strings and stuff ..', 9, dotnetlib1.Up2InterpretationCls])
    print(sep)

    s = SomeObj(9);
    print('From Python: {}'.format(s))
    dotnetlib1.Up2InterpretationCls.WriteToConsole(s)
    print(sep)

    for o in genNObjects(4):
        print('From Python: {}'.format(o))
    print(sep)

    dotnetlib1.Up2InterpretationCls.WriteAllToConsole(genNObjects(4))
    print(sep)





