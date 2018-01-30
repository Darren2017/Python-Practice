import string       #标识符检查
import keyword

alphas = string.letters + '_'
nums = string.digits
keywords = keyword.kwlist

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if myInput in keywords:
    print 'okey as a keyword'
else:
    if len(myInput) == 1:
        if myInput not in alphas:
            print 'invalid: remaining symbols must be alphanumeric'
        else:
            print "okay as an identifier" 
    else:
        if myInput[0] not in alphas:
            print '''invalid:first symbol must be alphabetic'''
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print '''invalid: remaining symbols must be alphanumeric'''
                    break
            else:
                print "okay as an identifier"