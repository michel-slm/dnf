
import rpmUtils.updates

instlist = [('foo', 'i386', '0', '1', '1'),
            ('bar', 'noarch', '0', '2', '1'),
            ('baz', 'i686', '0', '2', '3'),
            ('baz', 'x86_64', '0','1','4'),
            ('foo', 'i686', '0', '1', '1')]

availlist = [('foo', 'i686', '0', '1', '3'),
             ('foo', 'i386', '0', '1', '3'),
             ('foo', 'i686', '0', '1', '2'),
             ('bar', 'noarch', '0', '2', '2'),
             ('baz', 'noarch', '0', '2', '4'),
             ('baz', 'i686', '0', '2', '4'),
             ('baz', 'x86_64', '0', '1', '5'),
             ('baz', 'ppc', '0', '1', '5')]
             
up = rpmUtils.updates.Updates(instlist, availlist)
up.exactarch=1
#up.myarch = 'ppc'
up.doUpdates()
up.condenseUpdates()
for tup in up.updatesdict.keys():
    (old_n, old_a, old_e, old_v, old_r) = tup
    for (n, a, e, v, r) in up.updatesdict[tup]:
        print '%s.%s %s:%s-%s updated by %s.%s %s:%s-%s' % (old_n, 
                                old_a, old_e, old_v, old_r, n, a, e, v, r)


        
