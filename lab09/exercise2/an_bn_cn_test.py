from an_bn_cn import AnBnCn


def test_accept():
    an_bn_cn = AnBnCn()
    assert an_bn_cn.accept("")
    an_bn_cn.clear()
    assert an_bn_cn.accept("abc")
    an_bn_cn.clear()
    assert an_bn_cn.accept("aaaaabbbbbccccc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("aaaaabbbbcccc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("bac")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("ac")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("abbc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("abcabc")
    an_bn_cn.clear()


test_accept()
print("All tests passed!")
