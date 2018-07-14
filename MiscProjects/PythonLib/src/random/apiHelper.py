'''
Created on Dec 23, 2012

@author: AAACHARY
'''
def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %(method.ljust(spacing),processFunc(str(getattr(object, method).__doc__))) for method in methodList])
    
if __name__ == "__main__":
    print info.__doc__
    collapse = 1
    spacing = 10
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %(method.ljust(spacing),processFunc(str(getattr(object, method).__doc__))) for method in methodList])
    