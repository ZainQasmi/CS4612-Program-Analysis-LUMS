from hypothesis import given, assume
import hypothesis.strategies as st
import mid
import midCorrect


@given(st.integers(), st.integers(),st.integers())
def test_midFunc(x,y,z):
    assume (x>0)
    assert mid.mid(x,y,z) == midCorrect.mid(x,y,z)



if __name__ == '__main__':
    test_midFunc()

