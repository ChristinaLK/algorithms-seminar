import nose

from compare import *

triangle = [[1],[4,5],[2,4,7],[1,7,8,2]]

def test_compare_short():
	nose.tools.assert_equal([8, 12], compare(triangle[1],triangle[2]))
	nose.tools.assert_equal([6], compare(triangle[0],triangle[1]))