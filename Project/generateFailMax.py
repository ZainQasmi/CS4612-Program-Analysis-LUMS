from hypothesis import given, assume
import hypothesis.strategies as st
import maximum
import maximumCorrect



@given(st.lists(st.integers()))
def test_maxFunc(x):
    assume (len(x) > 0)
    assert maximum.maximum(x) == maximumCorrect.maximum(x)



if __name__ == '__main__':
    test_maxFunc()