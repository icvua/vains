import thumbnailer as tn

test = tn.Thumbnailer()

# test.size = 1000, 0
# test.size_preset = 'half'
# test.frame = 10
# test.frame_preset = 'two_third'
# test.frame_float = 0.2
test.path = '/home/rapa/test/colored/scene01'
test.output = '/home/rapa/test/colored'
test.execute()
